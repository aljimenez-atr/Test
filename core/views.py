from django.shortcuts import render, redirect
from .models import Vehiculo
from .forms import VehiculoForm

# Create your views here.
# Listado de vehiculos

def volver(request):
    return redirect(to="home")

def momo(request):
    return redirect(to="home")

def home(request):
    vehiculos = Vehiculo.objects.all()
    datos = {
        'vehiculos': vehiculos
    }
    return render(request, 'core/home.html', datos)

# Formulario para crear vehiculo
def add_vehiculo(request):

        return render(request, 'core/add_vehiculo.html')
#
def edit_vehiculo(request, pk):
    vehiculo = Vehiculo.objects.get(patente=pk)

    if request.method == 'POST':
        formulario_edit = VehiculoForm(data=request.POST, instance=vehiculo)
        if formulario_edit.is_valid:
            formulario_edit.save()
            return redirect(to="home")
    else:
        datos = {
            'form': VehiculoForm(instance=vehiculo) 
        }
        return render(request, 'core/edit_vehiculo.html', datos)

def delete_vehiculo(request, pk):
    vehiculo = Vehiculo.objects.get(patente=pk)
    vehiculo.delete()
    return redirect(to="home")

def blog(request):
    return render(request, 'core/blog.html')