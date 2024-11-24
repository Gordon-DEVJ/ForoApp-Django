from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comentario
from django.template.loader import get_template
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

def lista_posts(request):
    posts = Post.objects.all().order_by('-fecha_creacion')
    return render(request, 'foro_app/lista_posts.html', {'posts': posts})

def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST' and request.user.is_authenticated:
        contenido = request.POST.get('contenido')
        Comentario.objects.create(post=post, autor=autor, contenido=contenido)
        return redirect('detalle_post', pk=post.pk)
    return render(request, 'foro_app/detalle_post.html', {'post': post})

def nuevo_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            titulo = request.POST.get('titulo')
            contenido = request.POST.get('contenido')
            Post.objects.create(titulo=titulo, contenido=contenido, author=request.user)
            return redirect('lista_posts')
        return render(request, 'foro_app/nuevo_post.html')
    else:
            messages.error(request, 'Debes iniciar sesión para publicar un post')
            return redirect('login_usuario')

def detalle_proyecto(request):
    return render(request, 'foro_app/detalle_proyecto.html')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente al registrarse
            messages.success(request, 'Cuenta creada con éxito')
            return redirect('lista_posts')
        else:
            messages.error(request, 'Error al crear cuenta')
    else:
        form = UserCreationForm()

    return render(request, 'foro_app/registro.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Sesión iniciada')
            return redirect('lista_posts')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'foro_app/login.html')

def logout_usuario(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión')
    return redirect('lista_posts')

def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                subject_template_name='foro_app/password_reset_subject.txt',
                email_template_name='foro_app/password_reset_email.html'
            )
            return redirect('password_reset_done')
    else:
        form = PasswordResetForm()
    return render(request, 'foro_app/password_reset_form.html', {'form': form})

class PasswordResetDoneView(PasswordResetDoneView):
    template_name = 'foro_app/password_reset_done.html'

class PasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'foro_app/password_reset_confirm.html'

class PasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'foro_app/password_reset_complete.html'