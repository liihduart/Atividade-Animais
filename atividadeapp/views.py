from django.shortcuts import render
from .models import Categoria, Animal
# Create your views here.

def index(request):
    return render ('index.html')
                  
def Categoria(request):
    return render()

def Animal(request):
    return render()
