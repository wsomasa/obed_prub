from io import BytesIO
from django.contrib import admin
from import_export import resources 
from django.http import HttpResponse
import csv
from .models import Paciente, Consulta, Cirugia, Documento, Contacto
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer,PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.units import inch


#modelos para imprimir reportes
def exportar_contactos_como_pdf(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="contactos.pdf"'
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    stylesN = styles['Normal']
    justified_style = ParagraphStyle(
        name='Justified',
        parent=styles['Normal'],
        aligment=TA_JUSTIFY,
        spaceAfter=12
    )

    for obj in queryset:
        elements.append(Paragraph(f"<b>Nombre:</b> {obj.nombre}", stylesN))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(f"<b>Email:</b> {obj.email}", stylesN))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(f"<b>Teléfono:</b> {obj.telefono}", stylesN))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(f"<b>Mensaje:</b> {obj.mensaje}", stylesN))
        elements.append(Spacer(1, 12))
        
        mensaje = Paragraph(obj.mensaje.replace("\n", "<br />"), justified_style)
        elements.append(mensaje)
        elements.append(Spacer(1, 12))     
        
        elements.append(Paragraph(f"<b>Fechar Creación:</b> {obj.fecha_creacion}", stylesN))
        elements.append(Spacer(1, 24))

        elements.append(PageBreak())

    doc.build(elements)
    return response

exportar_contactos_como_pdf.short_description = "Exportar seleccionados como PDF"

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'mensaje', 'fecha_creacion')
    search_fields = ('nombre',)
    list_filter = ('nombre',) 
    list_per_page = 4
    actions=[exportar_contactos_como_pdf]
    
admin.site.register(Contacto, ContactoAdmin)


#Funciones para guardar e imprimir historias, pacientes, consultas.

def exportar_pacientes_como_pdf(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="pacientes.pdf"'
    doc = SimpleDocTemplate(response, pagesize=landscape(letter))
    elements = []
    styles = getSampleStyleSheet()
    styleN = styles['Normal']

    data = [
        ['Nombre', 'Cédula', 'Fecha de Nacimiento', 'Edad', 'Sexo', 'Teléfono', 'Dirección']
    ]

    for obj in queryset:
        data.append([
            Paragraph(obj.nombre, styleN),
            Paragraph(obj.cedula_identidad, styleN),
            Paragraph(obj.fecha_nacimiento.strftime('%Y-%m-%d') if obj.fecha_nacimiento else '', styleN),
            Paragraph(str(obj.edad), styleN),
            Paragraph(obj.sexo, styleN),
            Paragraph(obj.telefono, styleN),
            Paragraph(obj.direccion, styleN)
        ])

    total_width = sum([1.5, 1.5, 1.5, 0.5, 0.5, 1.5, 3.5]) * inch

    # Si el ancho total de la tabla excede el ancho de la página, ajustar las columnas
    if total_width > letter[1]:
        factor = letter[1] / total_width
        colWidths = [width * factor for width in [1.5, 1.5, 1.5, 0.5, 0.5, 1.5, 3.5]]
    else:
        colWidths = [1.5 * inch, 1.5 * inch, 1.5 * inch, 0.5 * inch, 0.5 * inch, 1.5 * inch, 3.5 * inch]

    # Crear una tabla
    table = Table(data, colWidths=colWidths)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  
    ])
    table.setStyle(style)
    elements.append(table)
    doc.build(elements)
    return response

exportar_pacientes_como_pdf.short_description = "Exportar seleccionados como PDF"


class PacienteAdmin(admin.ModelAdmin):
    list_display = ('cedula_identidad', 'nombre', 'telefono', 'email', 'direccion')
    search_fields = ('nombre', 'cedula_identidad')
    list_filter = ('nombre',) 
    list_per_page = 4
    actions=[exportar_pacientes_como_pdf]
 
admin.site.register(Paciente, PacienteAdmin)

def exportar_cirugia_como_pdf(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="cirugia.pdf"'

    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()
    styleN = styles['Normal']
    justified_style = ParagraphStyle(
        name='Justified',
        parent=styles['Normal'],
        alignmente=TA_JUSTIFY,
        spaceAfter=12
    )

    for obj in queryset:
        elements.append(Paragraph(f"<b>Nombre:</b> {obj.paciente}", styleN))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(f"<b>Fecha:</b> {obj.fecha}", styleN))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(f"<b>Tipo:</b> {obj.tipo}", styleN))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph("<b>Resultado:</b>", styleN))
        elements.append(Spacer(1, 12))
        resultado = Paragraph(obj.resultado.replace("\n", "<br />"), justified_style)
        elements.append(resultado)
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(f"<b>Médicos:</b> {obj.medicos}", styleN))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(f"<b>Enfermeros:</b> {obj.enfermeros}", styleN))
        elements.append(Spacer(1, 24))
        elements.append(Paragraph(f"<b>Personal externo:</b> {obj.personal_externo}", styleN))
        elements.append(Spacer(1, 24))
        elements.append(PageBreak())  # Añadir salto de página después de cada registro

    doc.build(elements)
    return response

exportar_cirugia_como_pdf.short_description = "Exportar seleccionados como PDF"


class CirugiaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'fecha', 'tipo', 'resultado', 'medicos', 'enfermeros', 'personal_externo' )
    search_fields = ('paciente__nombre', 'paciente__cedula_identidad') #Modelo ForeignKey: Si paciente es un campo ForeignKey que apunta a otro modelo (supongamos un modelo Paciente), entonces no puedes usar directamente paciente en search_fields para hacer búsquedas de texto. Necesitarías especificar un campo de texto dentro del modelo Paciente. Por ejemplo, si Paciente tiene un campo llamado nombre, deberías cambiar paciente a paciente__nombre.
    list_per_page = 4
    list_filter = ('tipo', 'paciente',) 
    date_hierarchy ="fecha"
    actions=[exportar_cirugia_como_pdf]

admin.site.register(Cirugia, CirugiaAdmin)


def exportar_consulta_como_pdf(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="consulta.pdf"'
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    stylesN = styles['Normal']
    justified_style = ParagraphStyle(
        name='Justified',
        parent=styles['Normal'],
        aligmente=TA_JUSTIFY,
        spaceAfter=12
    )

    for obj in queryset:
        elements.append(Paragraph(f"<b>Paciente:</b> {obj.paciente}", stylesN))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(f"<b>Fecha:</b> {obj.fecha}", stylesN))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(f"<b>Motivo:</b> {obj.motivo}", stylesN))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(f"<b>Diagnostico:</b> {obj.diagnostico}", stylesN))
        elements.append(Spacer(1, 12))       
        diagnostico = Paragraph(obj.diagnostico.replace("\n", "<b />"), justified_style)
        elements.append(diagnostico)
        elements.append(Spacer(1, 12))     
        elements.append(Paragraph(f"<b>Tratamiento Indicado:</b> {obj.tratamiento}", stylesN))
        elements.append(Spacer(1, 12))
        tratamiento = Paragraph(obj.tratamiento.replace("\n", "</b />"), justified_style)
        elements.append(tratamiento)
        elements.append(Spacer(1, 12))     
        elements.append(Paragraph(f"<b>Documento Adjunto:</b> {obj.archivos}", stylesN))
        elements.append(Spacer(1, 24))
        elements.append(Paragraph(f"<b>Proxima Consula:</b> {obj.proxima_consulta}", stylesN))
        elements.append(Spacer(1, 24))
        elements.append(PageBreak())

    doc.build(elements)
    return response

exportar_consulta_como_pdf.short_description = "Exportar seleccionados como PDF"


class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'fecha', 'motivo', 'diagnostico', 'tratamiento', 'archivos', 'proxima_consulta')
    search_fields = ('paciente__nombre', 'paciente__cedula_identidad')
    list_filter = ('fecha',)
    date_hierarchy ="fecha" #monstramos el año y los meses de las consultas 
    actions=[exportar_consulta_como_pdf]

admin.site.register(Consulta, ConsultaAdmin)

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'tipo', 'archivo', 'descripcion')
    search_fields = ('paciente__nombre', 'paciente__cedula_identidad')
    list_per_page = 4


admin.site.site_title = "Historia de pacientes"
admin.site.site_header = "Registro y Control de Traumatología"
admin.site.index_title = "Modulos"









