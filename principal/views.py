from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .forms import ClienteForm


from .models import Habitacion, Empresa, Cliente, Comedor, Proveedor, Venta




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


###################################################     Empresa        #######################################################################

@login_required
def listar_empresa(request):
    empresas = Empresa.objects.all()
    return render(request, 'funcs/empresa/empresa.html', {'empresas': empresas})

@login_required
def crear_empresa(request):
    if request.method == 'POST':
        nombre_empresa = request.POST['nombre_empresa']
        rut_empresa = request.POST['rut_empresa']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        email = request.POST['email']
        usuario = request.POST['usuario']
        contraseña = request.POST['contraseña']

        nueva_empresa = Empresa(
            nombre_empresa=nombre_empresa,
            rut_empresa=rut_empresa,
            direccion=direccion,
            telefono=telefono,
            email=email,
            usuario=usuario,
            contraseña=contraseña
        )
        nueva_empresa.save()
        return redirect('listar_empresa')
    return render(request, 'funcs/empresa/crear_empresa.html')


@login_required
def editar_empresa(request, id):
    empresa = get_object_or_404(Empresa, id=id)
    if request.method == 'POST':
        empresa.nombre_empresa = request.POST.get('nombre_empresa')
        empresa.rut_empresa = request.POST.get('rut_empresa')
        empresa.direccion = request.POST.get('direccion')
        empresa.telefono = request.POST.get('telefono')
        empresa.email = request.POST.get('email')
        empresa.usuario = request.POST.get('usuario')
        empresa.contraseña = request.POST.get('contraseña')
        empresa.save()
        return redirect('listar_empresa')
    return render(request, 'funcs/empresa/editar_empresa.html', {'empresa': empresa})


@login_required
def eliminar_empresa(request, id):
    empresa = get_object_or_404(Empresa, id=id)
    if request.method == 'POST':
        empresa.delete()
        return redirect('listar_empresa')
    return render(request, 'funcs/empresa/eliminar_empresa.html', {'empresa': empresa})


###################################################     Empresa        #######################################################################


###################################################     Cliente        #######################################################################



def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'funcs/clientes/cliente.html', {'clientes': clientes})


def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')  
    else:
        form = ClienteForm() 
    return render(request, 'funcs/clientes/crear_cliente.html', {'form': form})


def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)  
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')  
    else:
        form = ClienteForm(instance=cliente)  
    return render(request, 'funcs/clientes/editar_cliente.html', {'form': form})


def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'funcs/clientes/eliminar_cliente.html', {'cliente': cliente})










###################################################     Cliente        #######################################################################


###################################################     Platos         #######################################################################


def listar_platos(request):
    platos = Comedor.objects.all()
    return render(request, 'funcs/platos/platos.html', {'platos': platos})


def crear_plato(request):
    if request.method == 'POST':
        nombre_plato = request.POST.get('nombre_plato')
        tipo_servicio = request.POST.get('tipo_servicio')
        precio = request.POST.get('precio')
        descripcion = request.POST.get('descripcion')
        
        nuevo_plato = Comedor(
            nombre_plato=nombre_plato,
            tipo_servicio=tipo_servicio,
            precio=precio,
            descripcion=descripcion
        )
        nuevo_plato.save()
        return redirect('listar_platos')
    return render(request, 'funcs/platos/crear_platos.html')


def editar_plato(request, id):
    plato = get_object_or_404(Comedor, id=id)
    if request.method == 'POST':
        plato.nombre_plato = request.POST.get('nombre_plato')
        plato.tipo_servicio = request.POST.get('tipo_servicio')
        plato.precio = request.POST.get('precio')
        plato.descripcion = request.POST.get('descripcion')
        plato.save()
        return redirect('listar_platos')
    return render(request, 'funcs/platos/editar_platos.html', {'plato': plato})


def eliminar_plato(request, id):
    plato = get_object_or_404(Comedor, id=id)
    if request.method == 'POST':
        plato.delete()
        return redirect('listar_platos')
    return render(request, 'funcs/platos/eliminar_platos.html', {'plato': plato})






###################################################     Platos         #######################################################################


###################################################     Proveedor       #######################################################################

def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'funcs/proveedor/proveedor.html', {'proveedores': proveedores})

def crear_proveedor(request):
    if request.method == 'POST':
        nombre_proveedor = request.POST.get('nombre_proveedor')
        rut_proveedor = request.POST.get('rut_proveedor')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        rubro = request.POST.get('rubro')  
        Proveedor.objects.create(
            nombre_proveedor=nombre_proveedor,
            rut_proveedor=rut_proveedor,
            direccion=direccion,
            telefono=telefono,
            email=email,
            rubro=rubro
        )
        return redirect('listar_proveedores')
    return render(request, 'funcs/proveedor/crear_proveedor.html')


def editar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.nombre_proveedor = request.POST.get('nombre_proveedor')
        proveedor.rut_proveedor = request.POST.get('rut_proveedor')
        proveedor.direccion = request.POST.get('direccion')
        proveedor.telefono = request.POST.get('telefono')
        proveedor.email = request.POST.get('email')
        proveedor.rubro = request.POST.get('rubro')
        proveedor.save()
        return redirect('listar_proveedores')
    return render(request, 'funcs/proveedor/editar_proveedor.html', {'proveedor': proveedor})


def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('listar_proveedores')
    return render(request, 'funcs/proveedor/eliminar_proveedor.html', {'proveedor': proveedor})







###################################################     Proveedor       #######################################################################


###################################################     Ventas          #######################################################################

def listar_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'funcs/ventas/ventas.html', {'ventas': ventas})

def crear_venta(request):
    clientes = Cliente.objects.all()
    platos = Comedor.objects.all()
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        plato_id = request.POST.get('plato')
        cliente = get_object_or_404(Cliente, pk=cliente_id)
        plato = get_object_or_404(Comedor, pk=plato_id)
        Venta.objects.create(cliente=cliente, plato=plato)
        return redirect('listar_ventas')
    return render(request, 'funcs/ventas/crear_venta.html', {'clientes': clientes, 'platos': platos})

def eliminar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('listar_ventas')
    return render(request, 'funcs/ventas/eliminar_venta.html', {'venta': venta})



###################################################     Ventas          #######################################################################