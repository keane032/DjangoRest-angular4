from rest_framework import serializers
from .models import Cliente, PlacaMae
from .models import Pedido, Memoria, Processador   

class ProcessadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Processador
        fields = ['id','nome', 'marca']

class PlacaMaeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlacaMae
        fields = ['id','nome','processadores','qtdeslots','totaldememoria','videoIntegrado']

class MemoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Memoria
        fields = ['id','marca','tamanho']

class PedidoSerializer(serializers.ModelSerializer):
    memorias = MemoriaSerializer(many=True)
    placamae = PlacaMaeSerializer()
    processador = ProcessadorSerializer()
    class Meta:
        model = Pedido
        fields = ['id','placamae','processador','placadevideo','memorias','cliente']

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    pedidos = PedidoSerializer(many=True, read_only=True)
    class Meta:
        model = Cliente
        fields = ['id', 'nome','pedidos']
        