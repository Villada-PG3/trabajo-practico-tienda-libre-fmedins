from django.shortcuts import render

def home(request):
    return render(request, 'tiendalibre/home.html')


def acerca_de_mi(request):
    return render(request, 'tiendalibre/acercaDeMi.html')