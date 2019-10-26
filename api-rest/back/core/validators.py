from django.shortcuts import render
from rest_framework.decorators import action, api_view
from rest_framework import viewsets, generics
from rest_framework.exceptions import ParseError, NotFound
from .models import Cliente, Pedido, Memoria, PlacaMae, Processador
from .serializers import ClienteSerializer, PedidoSerializer,MemoriaSerializer, PlacaMaeSerializer, ProcessadorSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
import json

def pedidoValidator(memorias,placa_de_video,placa_mae,processador,cliente):
    total = 0
    for x in memorias:
        try:
            memoria = Memoria.objects.get(id=x)
            total = total + memoria.tamanho
        except Exception as e:
            raise NotFound({"erro":"mamoria nao cadastrada"})

    if placa_mae.processadores != "BOTH" and placa_mae.processadores != processador.marca :
        raise ParseError({"erro":"porcessador incompativel"}) 

    if placa_mae.qtd_eslots < len(memorias) :
        raise ParseError({"erro":"qtd memorias incompativel"}) 
            
    if placa_mae.total_memoria < total :
        raise ParseError({"erro":"total memorias incompativel"})

    if placa_mae.video_integrado == False and placa_de_video == '' :
        raise ParseError({"erro":"placa obrigatoria"}) 

    if len(memorias) == 0 :
        raise ParseError({"erro":"memorias insuficiente"}) 

    myPedido = Pedido.objects.create(placa_mae=placa_mae,cliente=cliente[0],placa_de_video=placa_de_video,processador=processador)

    for x in memorias:
        memoria = Memoria.objects.get(id=x)
        if  memoria:
            myPedido.memorias.add(memoria)
        
    response = PedidoSerializer(myPedido)
    return Response(response.data)