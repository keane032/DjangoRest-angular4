from rest_framework import serializers
from .models import Cliente, PlacaMae
from .models import Pedido, Memoria , Procecador   

class ProcecadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Procecador
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
    class Meta:
        model = Pedido
        fields = ['id','procecador','placamae','placadevideo','memorias','cliente']

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    pedidos = PedidoSerializer(many=True, read_only=True)
    class Meta:
        model = Cliente
        fields = ['id', 'nome','pedidos']
        