#Configurando el redireccionamiento
from django.urls import path
from . import views
# Crear un arreglo
urlpatterns=[
    path('', views.home),
    path('login', views.login,name='login'),
    path('register', views.register,name='register'),
    path('guardarRegistro/', views.guardarRegistro,name='guardarRegistro'),

    path('albums', views.albums,name='albums'),
    path('login', views.login_view, name='login'),
]