from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.

def index(request):
    title = 'Porfolio '
    return render(request, 'index.html', {
        'title': title
    })