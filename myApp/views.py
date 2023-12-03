from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.

def index(request):
    title = 'Porfolio '
    return render(request, 'index.html', {
        'title': title
    })

def about(request):
    return render(request, 'about.html')

def experiencia(request):
    return render(request, 'experiencia.html')

def servicios(request):
    return render(request, 'servicios.html')

def contacto(request):
    return render(request, 'contacto.html')