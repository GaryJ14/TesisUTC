from django.http import JsonResponse
from django.shortcuts import redirect, render
from.models import Registro
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request,"Frontend/home.html")

def login(request):
    return render(request,"Frontend/login.html")

def register(request):
    return render(request,"Frontend/register.html")

def guardarRegistro(request):
    nombre=request.POST['nombre']
    email=request.POST['email']
    password=request.POST['password']
    nuevoRegistro=Registro.objects.create(nombre=nombre, email=email, password=password)
    messages.success(request, "Usuario registrado exitosamente")
    return redirect('/')

def albums(request):
    return render(request,"Frontend/albums.html")

