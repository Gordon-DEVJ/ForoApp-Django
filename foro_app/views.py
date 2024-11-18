from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comentario
from django.template.loader import get_template
from django.http import HttpResponse

def lista_posts(request):
    posts = Post.objects.all().order_by('-fecha_creacion')
    return render(request, 'foro_app/lista_posts.html', {'posts': posts})

def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        autor = request.POST.get('autor')
        contenido = request.POST.get('contenido')
        Comentario.objects.create(post=post, autor=autor, contenido=contenido)
        return redirect('detalle_post', pk=post.pk)
    return render(request, 'foro_app/detalle_post.html', {'post': post})

def nuevo_post(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        contenido = request.POST.get('contenido')
        Post.objects.create(titulo=titulo, contenido=contenido)
        return redirect('lista_posts')
    return render(request, 'foro_app/nuevo_post.html')

def detalle_proyecto(request):
    return render(request, 'foro_app/detalle_proyecto.html')