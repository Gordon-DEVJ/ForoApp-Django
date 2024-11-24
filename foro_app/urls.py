from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    path('detalle_post/<int:pk>/', views.detalle_post, name='detalle_post'),
    path('nuevo_post/', views.nuevo_post, name='nuevo_post'),
    path('detalle_proyecto/', views.detalle_proyecto, name="detalle_proyecto"),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_usuario, name='login_usuario'),
    path('logout/', views.logout_usuario, name='logout_usuario'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')
]
