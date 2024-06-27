from django.shortcuts import render, get_object_or_404
from App_blog.models import Post

def blog(request):
    
    posts=Post.objects.all() #aquí importamos todos los post creados
    return render(request, 'blog/blog.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})
