from django.shortcuts import render
from rest_framework.decorators import action, api_view
from rest_framework import viewsets, generics
from .models import Cliente, Pedido, Memoria, PlacaMae, Processador
from .serializers import ClienteSerializer, PedidoSerializer,MemoriaSerializer, PlacaMaeSerializer, ProcessadorSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
import json

class ProcessadorViewSet(viewsets.ModelViewSet):
    """
    create:
        Cadastra um novo processador.

    retrieve:
        Retorna uma instancia de procecador pelo id.

    list:
        Retorna todas processadores cadastrados.

    delete:
        Remove uma processador existente pelo id.

    """
    queryset = Processador.objects.all()
    serializer_class = ProcessadorSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    """
    create:
        Cadastra um novo cliente.

    retrieve:
        Retorna uma instancia de cliente pelo id.

    list:
        Retorna todos clientes.

    delete:
        Remove uma cliente existente pelo id.

    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PlacaMaeViewSet(viewsets.ModelViewSet):
    """
    create:
        Cadastra uma nova placa mae.

    retrieve:
        Retorna uma instancia de placa mae pelo id.

    list:
        Retorna todas placas .

    delete:
        Remove uma placa mae existente pelo id.

    """
    queryset = PlacaMae.objects.all()
    serializer_class = PlacaMaeSerializer

class MemoriaViewSet(viewsets.ModelViewSet):
    """
    create:
        Cadastra uma nova memoria.


    retrieve:
        Retorna uma instancia de memoria pelo id.

    list:
        Retorna todas memorias.

    delete:
        Remove uma memoria existente pelo id.

    """
    queryset = Memoria.objects.all()
    serializer_class = MemoriaSerializer   

class PedidoViewSet(viewsets.ModelViewSet):
    """
    create:
        Cadastra novo pedido.
        Cria um pedido passando os parametros:
            cliente(int),placamae(int),processador(int),placadevideo(string),memorias[int]
        

    retrieve:
        Retorna uma instancia de pedido pelo id.

    list:
        Retorna todos pedidos.

    delete:
        Remove um pedido existente pelo id.

    """
 
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def create(self,request):
        memorias = request.data['memorias']
        placa_de_video = request.data['placadevideo']
        cliente = Cliente.objects.filter(id = request.data['cliente'])
        placa_mae = PlacaMae.objects.get(id = request.data['placamae'])
        processador = Processador.objects.get(id = request.data['processador'])

        if not placa_mae:
            return Response({"status":"placamae inexistentes"})

        if not cliente:
            return Response({"status":"usuario inexistentes"})
        
        total = 0
        for x in memorias:
            try:
                memoria = Memoria.objects.get(id=x)
                total = total + memoria.tamanho
            except Exception as e:
                return Response({"status":"memoria nao cadastrada"}) 

        if placa_mae.processadores != "BOTH" and placa_mae.processadores != processador.marca :
            return Response({"status":"porcessador incompativel"}) 

        if placa_mae.qtd_eslots < len(memorias) :
            return Response({"status":"qtd memorias incompativel"}) 
                
        if placa_mae.total_memoria < total :
            return Response({"status":"total memorias incompativel"})

        if placa_mae.video_integrado == False and placa_de_video == '' :
            return Response({"status":"placa obrigatoria"}) 

        if len(memorias) == 0 :
            return Response({"status":"memorias insuficiente"}) 


        myPedido = Pedido.objects.create(placa_mae=placa_mae,cliente=cliente[0],placa_de_video=placa_de_video,processador=processador)

        for x in memorias:
            memoria = Memoria.objects.get(id=x)
            if  memoria:
                myPedido.memorias.add(memoria)
                print(x)
        response = PedidoSerializer(myPedido)
        return Response(response.data)