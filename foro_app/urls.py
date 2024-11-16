from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    path('detalle_post/<int:pk>/', views.detalle_post, name='detalle_post'),
    path('nuevo_post/', views.nuevo_post, name='nuevo_post'),
]
