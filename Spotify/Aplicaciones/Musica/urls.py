#Configurando el redireccionamiento
from django.urls import path
from . import views
# Crear un arreglo
urlpatterns=[
    path('', views.home),
    
]