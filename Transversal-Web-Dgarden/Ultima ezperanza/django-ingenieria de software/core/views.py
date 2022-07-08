from distutils import core
from .models import *
from django .shortcuts import render, redirect
from .forms import promoform
from django.contrib.auth.decorators import login_required
from .forms import promonew
from .forms import productoform
from .forms import productonew
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, authenticate
from .forms import  CustomUserCreationForm
from django.contrib.auth.decorators import login_required





def Index (request):
    return render (request, 'core/Index.html')
    
def InicioSesion(request):
        return render (request, 'core/InicioSesion.html')

def Regist(request):
    return render (request, 'core/Regist.html')
    
@login_required(login_url='/InicioSesion')
def CarritoCompras(request):
    return render (request, 'core/CarritoCompras.html')

def CarritoComprasHistorial(request):
    return render (request, 'core/CarritoComprasHistorial.html')

def IniciosesionAdmin(request):
    return render (request, 'core/IniciosesionAdmin.html')
    
@login_required(login_url='/InicioSesion')
def crudproductos(request):
    return render (request, 'core/crudproductos.html')


def crudproductos2(request):
    return render (request, 'core/crudproductos2.html')

def Formulario(request):
    return render (request, 'core/Formulario.html')

def FormularioEmp(request):
    return render (request, 'core/FormularioEmp.html')

def IndexDescuento(request):
    return render (request, 'core/IndexDescuento.html')

def Suscribirse(request):
    return render (request, 'core/Suscribirse.html')

def Pago(request):
    return render (request, 'core/Pago.html')

def PagoSus(request):
    return render (request, 'core/PagoSus.html')

def crud2(request):
    return render (request, 'core/crud2.html')

def pagina (request):
    return render (request, 'core/pagina.html')
       
    
def logout(request):
    return render(request, 'logout.html')

@login_required(login_url='/InicioSesion')
def crud (request):
    contexto = {'promocion': promocion.objects.all()}
    return render (request, 'core/crud.html', contexto)    

@login_required(login_url='/InicioSesion')
def modificarSuscriptor(request, id):
    Sub = promocion.objects.get(idpromo=id)
    datos = {"form":promoform(instance=Sub)}
    if request.method == "POST":
        form = promoform(request.POST, instance=Sub)
        if form.is_valid:
            form.save()
            
            datos["mensaje"] = "suscriptor modificado!."
            datos['form'] = form
            return redirect (to= "Index")
            
    return render(request, 'core/modificar_suscriptores.html', datos)

@login_required(login_url='/InicioSesion')
def eliminarPromocion(request, id):
    vehiculo = promocion.objects.get(idpromo=id)
    vehiculo.delete()
    return redirect(to="Index")

@login_required(login_url='/InicioSesion')
def crear_promocion(request):
    datos = {"form":promonew()}
    if request.method == "POST":
        form = promonew(request.POST)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Vehiculo agregado!."
            return redirect (to= "Index")
    return render(request, 'core/crear_promocion.html', datos)


@login_required(login_url='/InicioSesion')
def crud_productos (request):
    contexto = {'producto': Producto.objects.all()}
    return render (request, 'core/crud_productos.html', contexto)   

@login_required(login_url='/InicioSesion')
def modificar_Producto(request, id):
    Sub = Producto.objects.get(IdProducto=id)
    datos = {"form":productoform(instance=Sub)}
    if request.method == "POST":
        form = productoform(request.POST, instance=Sub)
        if form.is_valid:
            form.save()
            
            datos["mensaje"] = "suscriptor modificado!."
            datos['form'] = form
            return redirect (to= "Index")

    return render(request, 'core/modificar_producto.html', datos)

@login_required(login_url='/InicioSesion')
def eliminarProducto(request, id):
    vehiculo = Producto.objects.get(IdProducto=id)
    vehiculo.delete()
    return redirect(to="Index")

@login_required(login_url='/InicioSesion')
def crear_producto(request):
    datos = {"form":productonew()}
    if request.method == "POST":
        form = productonew(request.POST)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Vehiculo agregado!."
            return redirect (to= "Index")
    return render(request, 'core/crear_producto.html', datos)


def Regist(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return render(request, 'core/Index.html', {'form':UserCreationForm()})
        else:
            data['form'] = formulario
    
    return render(request, 'core/Regist.html', {'form':UserCreationForm()})

