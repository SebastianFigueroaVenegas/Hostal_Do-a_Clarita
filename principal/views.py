from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

from .models import Habitacion




################################################### principal #######################################################################

def base(request):
    return render(request, 'base.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')  
        else:
            messages.error(request, "Credenciales incorrectas.")
    return render(request, 'login.html')

def logout_vista(request):
    logout(request)
    return redirect('login') 

@login_required
def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = form.cleaned_data['is_staff']  # Toma el valor del formulario
            user.save()
            messages.success(request, 'Cuenta creada exitosamente.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})





###################################################     Principal      #######################################################################


###################################################     Habitacion     #######################################################################

@login_required
def listar_habitaciones(request):
    habitaciones = Habitacion.objects.all()
    return render(request, 'funcs/habitacion/habitacion.html', {'habitaciones': habitaciones})


@login_required
def crear_habitacion(request):
    if request.method == 'POST':
        numero_habitacion = request.POST.get('numero_habitacion')
        tipo_cama = request.POST.get('tipo_cama')
        accesorios = request.POST.get('accesorios')
        precio = request.POST.get('precio')
        estado = request.POST.get('estado')
        
        nueva_habitacion = Habitacion(
            numero_habitacion=numero_habitacion,
            tipo_cama=tipo_cama,
            accesorios=accesorios,
            precio=precio,
            estado=estado
        )
        nueva_habitacion.save()
        return redirect('listar_habitaciones')
    return render(request, 'funcs/habitacion/crear_habitacion.html')


@login_required
def editar_habitacion(request, id):
    habitacion = get_object_or_404(Habitacion, id=id)
    if request.method == 'POST':
        habitacion.numero_habitacion = request.POST.get('numero_habitacion')
        habitacion.tipo_cama = request.POST.get('tipo_cama')
        habitacion.accesorios = request.POST.get('accesorios')
        habitacion.precio = request.POST.get('precio')
        habitacion.estado = request.POST.get('estado')
        habitacion.save()
        return redirect('listar_habitaciones')
    return render(request, 'funcs/habitacion/editar_habitacion.html', {'habitacion': habitacion})


@login_required
def eliminar_habitacion(request, id):
    habitacion = get_object_or_404(Habitacion, id=id)
    if request.method == 'POST':
        habitacion.delete()
        return redirect('listar_habitaciones')
    return render(request, 'funcs/habitacion/eliminar_habitacion.html', {'habitacion': habitacion})


###################################################     Habitacion     #######################################################################