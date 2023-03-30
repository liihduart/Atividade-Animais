from django.urls import path
from .models import Categoria, Animal

urlpatterns = [
    path('', Categoria, name = 'Categoria'),
    path('', Animal, name = 'Animal'),

]