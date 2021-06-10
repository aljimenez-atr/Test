from django.shortcuts import render, redirect


# Create your views here.
# Listado de vehiculos

def menu(request):
    return render(request,'core/menu.html')