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
    path('login', views.login_view, name='login'),
    path('events', views.events, name='events'),
    path('contact', views.contact, name='contact'),

    #USUARIOS
    path('ListadoUsuarios', views.ListadoUsuarios, name='ListadoUsuarios'),
    path('eliminarUsuario/<id>', views.eliminarUsuario,name='eliminarUsuario'),
    path('guardarUsuario/', views.guardarUsuario,name='guardarUsuario'),

    #Musica
    path('ListadoMusic/', views.ListadoMusic, name='ListadoMusic'),

    
    


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # type: ignore