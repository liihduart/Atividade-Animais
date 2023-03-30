from django.db import models

# Create your models here.

class Categoria(models.Model):
    name = models.CharField(max_length= 100)

    def __str__(self):
        return self.name


class Animal(models.Model):
    nome = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=100, decimal_places = 2)
    altura = models.DecimalField(max_digits= 100, decimal_places = 2)
    descrição = models.CharField(max_length=50)
    imagem = models.ImageField()
    categoria = models.ManyToManyField('Categoria', related_name='Animal')

    def __str__(self):
        return self.nome

