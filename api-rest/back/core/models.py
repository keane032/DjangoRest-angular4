from django.db import models
from rest_framework import serializers


class Cliente(models.Model):
    nome = models.CharField(max_length=50)

class Processador(models.Model):
    nome = models.CharField(max_length=50)  
    marca = models.CharField(max_length=50) 

class Memoria(models.Model):
    marca = models.CharField(max_length=50)
    tamanho = models.IntegerField()

class PlacaMae(models.Model):
    nome = models.CharField(max_length=50)
    processadores = models.CharField(max_length=50)
    qtd_eslots = models.IntegerField()
    total_memoria = models.IntegerField()
    video_integrado = models.BooleanField() 

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='pedidos', on_delete=models.CASCADE)
    memorias = models.ManyToManyField(Memoria)
    processador = models.ForeignKey(Processador, related_name='procecador', on_delete=models.CASCADE)
    placa_mae = models.ForeignKey(PlacaMae, related_name='placamae', on_delete=models.CASCADE)
    placa_de_video = models.CharField(max_length=50)
        
