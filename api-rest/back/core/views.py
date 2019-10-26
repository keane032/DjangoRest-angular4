from django.shortcuts import render
from rest_framework.decorators import action, api_view
from rest_framework import viewsets, generics
from rest_framework.exceptions import ParseError, NotFound
from .models import Cliente, Pedido, Memoria, PlacaMae, Processador
from .serializers import ClienteSerializer, PedidoSerializer,MemoriaSerializer, PlacaMaeSerializer, ProcessadorSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .validators import pedidoValidator
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

        cliente = Cliente.objects.filter(id = request.data['cliente'])
        
        placa_de_video = request.data['placadevideo']

        if not placa_de_video:
            raise ParseError({"erro":"insira o nome da placa de video"})

        if type(placa_de_video) != str:
            raise ParseError({"erro":"placa de video apenas aceita string"})
        
        if not cliente:
            raise ParseError({"erro":"user nao existe"})

        try:
            memorias = request.data['memorias']
            placa_mae = PlacaMae.objects.get(id = request.data['placamae'])
            processador = Processador.objects.get(id = request.data['processador'])
        except Exception as e:
            raise ParseError({"erro":e})
        
        return pedidoValidator(memorias=memorias,placa_de_video=placa_de_video,placa_mae=placa_mae,processador=processador,cliente=cliente)

       