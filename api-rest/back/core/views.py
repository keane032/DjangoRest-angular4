from django.shortcuts import render
from rest_framework.decorators import action, api_view
from rest_framework import viewsets, generics
from .models import Cliente, Pedido, Memoria, PlacaMae, Procecador
from .serializers import ClienteSerializer, PedidoSerializer,MemoriaSerializer, PlacaMaeSerializer, ProcecadorSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
import json

class ProcecadorViewSet(viewsets.ModelViewSet):
    queryset = Procecador.objects.all()
    serializer_class = ProcecadorSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
  
    @action(detail=False)
    def getdetail(self, request):
        print("=================//===============")
        print(request.data)
        return Response({'status':'done'})

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
        querysetCliente = Cliente.objects.filter(id = request.data['cliente'])
        
        print(querysetCliente[0])

        myPedido = Pedido.objects.create(cliente=querysetCliente[0],placadevideo="wqeeeee",procecador="qwe",placamae="wqe")
        print(myPedido)
        memoria = Memoria.objects.filter(id=memo)
        myPedido.memorias.add(memoria[0])
        print(memo)
        print(memoria)
        # pedidos = []
        # pedidos.append(data)
        # me = MemoriaSerializer(data=request.data['memoria'])
       
        # if newCliete.is_valid():
        #     print(newCliete)
        return Response({"status":"done"})

        # if data.is_valid():

        #     print(data.data)
        #     memo = MemoriaSerializer(data=data.data['memoria'])
        #     print(memo)
        #     data.save()
        # return Response(data.is_valid())


    # @action(detail=True,methods=['post'])
    # def criarpedido(self, request, pk):
    #     print(request.data)
    #     return Response({'status': 'ok'})