from django.shortcuts import render
from rest_framework.decorators import action, api_view
from rest_framework import viewsets, generics
from .models import Cliente, Pedido, Memoria, PlacaMae, Processador
from .serializers import ClienteSerializer, PedidoSerializer,MemoriaSerializer, PlacaMaeSerializer, ProcessadorSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
import json

class ProcessadorViewSet(viewsets.ModelViewSet):
    queryset = Processador.objects.all()
    serializer_class = ProcessadorSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PlacaMaeViewSet(viewsets.ModelViewSet):
    queryset = PlacaMae.objects.all()
    serializer_class = PlacaMaeSerializer

class MemoriaViewSet(viewsets.ModelViewSet):
    queryset = Memoria.objects.all()
    serializer_class = MemoriaSerializer   

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def create(self,request):
        memo = request.data['memorias']
        placa = request.data['placadevideo']
        querysetCliente = Cliente.objects.filter(id = request.data['cliente'])
        querysetPlacamae = PlacaMae.objects.get(id = request.data['placamae'])
        querysetProcessador = Processador.objects.get(id = request.data['processador'])

        total = 0
        for x in memo:
            try:
                memoria = Memoria.objects.get(id=x)
                total = total + memoria.tamanho
            except Exception as e:
                return Response({"status":"memoria nao cadastrada"}) 

        if querysetPlacamae.processadores != "BOTH" and querysetPlacamae.processadores != querysetProcessador.marca :
            return Response({"status":"porcessador incompativel"}) 

        if querysetPlacamae.qtdeslots < len(memo) :
            return Response({"status":"qtd memorias incompativel"}) 
                
        if querysetPlacamae.totaldememoria < total :
            return Response({"status":"total memorias incompativel"})

        if querysetPlacamae.videoIntegrado == False and placa == '' :
            return Response({"status":"placa obrigatoria"}) 

        if len(memo) == 0 :
            return Response({"status":"memorias insuficiente"}) 

        if not querysetPlacamae:
            return Response({"status":"placamae inexistentes"})

        if not querysetCliente:
            return Response({"status":"usuario inexistentes"})

        myPedido = Pedido.objects.create(placamae=querysetPlacamae,cliente=querysetCliente[0],placadevideo=placa,processador=querysetProcessador)

        for x in memo:
            memoria = Memoria.objects.get(id=x)
            if  memoria:
                myPedido.memorias.add(memoria)
                print(x)

        return Response({"status":"done"})