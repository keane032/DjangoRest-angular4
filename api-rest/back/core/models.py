from django.db import models
from rest_framework import serializers
# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='pedidos', on_delete=models.CASCADE)
    procecador = models.CharField(max_length=50)
    placamae = models.CharField(max_length=50)
    placadevideo = models.CharField(max_length=50)
    memoria = models.CharField(max_length=50)
   