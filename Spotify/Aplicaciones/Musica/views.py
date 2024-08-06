from django.http import JsonResponse
from django.shortcuts import redirect, render
from.models import Registro,Music
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request,"Frontend/home.html")

def login(request):
    return render(request,"Frontend/login.html")

def register(request):
    return render(request,"Frontend/register.html")

def albums(request):
    return render(request,"Frontend/albums.html")

def events(request):
    return render(request,"Frontend/events.html")


def contact(request):
    return render(request,"Frontend/contact.html")

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = Registro.objects.get(email=email)
            if user.password == password:
                # Aquí podrías manejar la lógica de iniciar sesión correctamente
                messages.success(request, 'Inicio de sesión exitoso')
                return redirect('home')  # Redirige a la página principal u otra página
            else:
                messages.error(request, 'Contraseña incorrecta')
        except Registro.DoesNotExist:
            messages.error(request, 'El correo electrónico no está registrado')

    return render(request, 'Frontend/login.html')

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


#----------------------------------------------------------Music----------------------------------------------------------

def ListadoMusic(request):
    musicas = Music.objects.all()
    return render(request, 'Backend/ListadoMusic.html', {'musicas': musicas})
