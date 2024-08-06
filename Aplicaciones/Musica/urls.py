#Configurando el redireccionamiento
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
# Crear un arreglo
urlpatterns=[
    path('', views.home),
    path('login', views.login,name='login'),

    path('register', views.register,name='register'),
    path('guardarRegistro/', views.guardarRegistro,name='guardarRegistro'),

    path('albums', views.albums,name='albums'),
    path('events', views.events, name='events'),
    path('contact', views.contact, name='contact'),

    #USUARIOS
    path('ListadoUsuarios', views.ListadoUsuarios, name='ListadoUsuarios'),
    path('eliminarUsuario/<id>', views.eliminarUsuario,name='eliminarUsuario'),
    path('guardarUsuario/', views.guardarUsuario,name='guardarUsuario'),
    path('procesarActualizacionUsuario/', views.procesarActualizacionUsuario,name='procesarActualizacionUsuario'),


    #Musica
    path('ListadoMusic/', views.ListadoMusic, name='ListadoMusic'),
    path('eliminarMusic/<id>', views.eliminarMusic,name='eliminarMusic'),
    path('guardarMusic/', views.guardarMusic,name='guardarMusic'),
    path('procesarActualizacionMusica/', views.procesarActualizacionMusica,name='procesarActualizacionMusica'),

    
    


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # type: ignore