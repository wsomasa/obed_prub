from django.core.management.base import BaseCommand
from models import HistoriaGeneral, Consulta, Cirugia, Archivo, Documento

class Command(BaseCommand):
    help = 'Carga los datos de los modelos existentes en HistoriaGeneral'

    def handle(self, *args, **options):
        # Obtener datos de Consulta
        consultas = Consulta.objects.all()
        for consulta in consultas:
            # Crear una nueva instancia de HistoriaGeneral y llenar los campos relevantes
            historia_general = HistoriaGeneral(
                paciente=consulta.paciente,
                fecha_consulta=consulta.fecha,
                motivo_consulta=consulta.motivo,
                diagnostico_consulta=consulta.diagnostico,
                tratamiento_consulta=consulta.tratamiento,
            )
            historia_general.save()

        cirugias = Cirugia.objects.all()
        for cirugia in cirugias:
            # Crear una nueva instancia de HistoriaGeneral y llenar los campos relevantes
            historia_general = HistoriaGeneral(
                paciente=cirugia.paciente,
                fecha_cirugia=cirugia.fecha,
                tipo_cirugia=cirugia.tipo,
                resultado_cirugia=cirugia.resultado,
            )
            historia_general.save()
        documentos = Documento.objects.all()
        for documento in documentos:
            historia_general = HistoriaGeneral(
                paciente=Documento.paciente, 
                fecha_documento=documento.fecha,
                tipo_documento=documento.tipo,
                descripcion_documento=documento.descripcion,
            )
            historia_general.save()
        
        archivos = Archivo.objects.all()
        for archivo in archivos:
            historia_general = HistoriaGeneral(
                paciente=Archivo.consulta_relacionada.paciente, 
                archivo=Archivo.archivo,
            )
            historia_general.save()
            
        # Repetir el mismo proceso para otros modelos como Cirugia, Archivo y Documento
        # Puedes personalizar este proceso según tus necesidades
