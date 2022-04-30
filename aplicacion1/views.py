from django.shortcuts import redirect, render
from .models import Cliente
from .forms import RegistroClienteForm, LoginForm, UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.views.defaults import page_not_found
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm



# Create your views here.


def index(request):
    return render (request, 'aplicacion1/index.html')

def contacto(request):
    return render (request, 'aplicacion1/contacto.html')

def productos(request):
    return render (request, 'aplicacion1/productos.html')

def estadisticas(request):
    return render (request, 'aplicacion1/estadisticas.html')

@login_required
def clientes(request):
    usuario=Cliente.objects.all()
    return render (request, 'aplicacion1/clientes.html', {"data":usuario})

#@login_required
@permission_required("is_staff")
def ingreso_clientes(request):
    form = RegistroClienteForm()

    if request.method == 'POST':
        
        form = RegistroClienteForm(request.POST)

        if form.is_valid():

            cliente=Cliente()
            cliente.nombre=form.cleaned_data["nombre"]
            cliente.apellido=form.cleaned_data["apellido"]
            cliente.correo=form.cleaned_data["correo"]
            cliente.telefono=form.cleaned_data["telefono"]
            cliente.ciudad=form.cleaned_data["direccion"]
            cliente.save()
            return redirect('ingreso_clientes')

        else:
            print('invalido')

    return render(request, 'aplicacion1/ingreso_clientes.html', {'form':form})


def login (request):
    if request.method == "POST":
        form = LoginForm(data = request.POST)
        
        if form.is_valid():
            usuario=form.cleaned_data["nombre"]
            clave=form.cleaned_data["password"]
            user=authenticate(request, username=usuario, password=clave)
            if user is not None:
                auth_login(request, user)
            return redirect ('bienvenido')
    else:
        form=LoginForm()
        return render (request, 'aplicacion1/login.html', {"form":form})

@login_required
def bienvenido (request):
    return render (request, 'aplicacion1/bienvenido.html')

def salir(request):
    logout(request)
    return redirect ("/login")

def custom_page_not_found_view(request, exception):
    return render(request, "404.html", {})

def register(request):
    form = UserRegisterForm()
    print("hola")
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado exitosamente.')
            return redirect('login')
    else:

        form = UserRegisterForm()
    context = {'form':form}
    return render(request, 'aplicacion1/register.html', context)