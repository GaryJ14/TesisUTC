from django.http import JsonResponse
from django.shortcuts import redirect, render
from.models import Registro,Music
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password

# Create your views here.
def home(request):
    return render(request,"Frontend/home.html")

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = Registro.objects.get(email=email)
            if user.password == password:
                # Aquí podrías manejar la lógica de iniciar sesión correctamente
                messages.success(request, 'Inicio de sesión exitoso')
                return redirect('/')  # Redirige a la página principal u otra página
            else:
                messages.error(request, 'Contraseña incorrecta')
        except Registro.DoesNotExist:
            messages.error(request, 'El correo electrónico no está registrado')

    return render(request, 'Frontend/login.html')

def register(request):
    return render(request,"Frontend/register.html")

def albums(request):
    return render(request,"Frontend/albums.html")

def events(request):
    return render(request,"Frontend/events.html")


def contact(request):
    return render(request,"Frontend/contact.html")

 

#-----------------------USUARIOS-----------------------------------------------
def ListadoUsuarios(request):
    usuarios=Registro.objects.all()
    return render(request, 'Backend/ListadoUsuarios.html',{'usuarios': usuarios})

def guardarRegistro(request):
    nombre=request.POST['nombre']
    email=request.POST['email']
    password=request.POST['password']
    confirmPassword=request.POST['confirmPassword']
    nuevoRegistro=Registro.objects.create(nombre=nombre, email=email, password=password, confirmPassword=confirmPassword)
    messages.success(request, "Usuario registrado exitosamente")
    return redirect('/')

def eliminarUsuario (request,id):
    usuarioEliminar=Registro.objects.get(id=id)
    usuarioEliminar.delete()
    messages.success(request, "Género eliminado Correctamente")
    return redirect('ListadoUsuarios')

def guardarUsuario(request):
    nombre=request.POST['nombre']
    email=request.POST['email']
    password=request.POST['password']
    confirmPassword=request.POST['confirmPassword']
    nuevoRegistro=Registro.objects.create(nombre=nombre, email=email, password=password, confirmPassword=confirmPassword)
    messages.success(request, "Usuario registrado exitosamente")
    return redirect('ListadoUsuarios')

def procesarActualizacionUsuario(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    email=request.POST['email']
    password=request.POST['password']
    confirmPassword=request.POST['confirmPassword']
    UsuarioConsultado=Registro.objects.get(id=id)
    UsuarioConsultado.nombre=nombre
    UsuarioConsultado.email=email
    UsuarioConsultado.password=password
    UsuarioConsultado.confirmPassword=confirmPassword
    UsuarioConsultado.save()
    messages.success(request, 'Usuario actualizado exitosamente.')
    return redirect('ListadoUsuarios')

#----------------------------------------------------------Music----------------------------------------------------------

def ListadoMusic(request):
    musicas = Music.objects.all()
    return render(request, 'Backend/ListadoMusic.html', {'musicas': musicas})
def guardarMusic(request):
    id=request.POST['id']
    Titulo=request.POST['Titulo']
    Artista=request.POST['Artista']
    Album=request.POST['Album']
    Genero=request.POST['Genero']
    Audio=request.FILES.get('Audio')
    
    nuevoRegistro=Registro.objects.create(id=id,Titulo=Titulo,Artista=Artista,Album=Album,Genero=Genero,Audio=Audio)
    messages.success(request, "Musica registrada exitosamente")
    return redirect('Backend/ListadoMusic.html')

def eliminarMusic (request,id):
    musicaEliminar=Music.objects.get(id=id)
    musicaEliminar.delete()
    messages.success(request, "Musica eliminada Correctamente")
    return redirect('ListadoMusic')

def procesarActualizacionMusica(request):
    id=request.POST['id']
    Titulo=request.POST['Titulo']
    Artista=request.POST['Artista']
    Album=request.POST['Album']
    Genero=request.POST['Genero']
    Audio=request.FILES.get('Audio')
    MusicaConsultada=Music.objects.get(id=id)
    MusicaConsultada.Titulo=Titulo
    MusicaConsultada.Artista=Artista
    MusicaConsultada.Album=Album
    MusicaConsultada.Genero=Genero
    MusicaConsultada.Audio=Audio
    MusicaConsultada.save()
    messages.success(request, 'Musica actualizado exitosamente.')
    return redirect('ListadoMusic')
