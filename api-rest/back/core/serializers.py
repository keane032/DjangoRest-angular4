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
        fields = ['id','nome','processadores','qtd_eslots','total_memoria','video_integrado']

class MemoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Memoria
        fields = ['id','marca','tamanho']

class PedidoSerializer(serializers.ModelSerializer):
    memorias = MemoriaSerializer(many=True)
    placa_mae = PlacaMaeSerializer()
    processador = ProcessadorSerializer()
    class Meta:
        model = Pedido
        fields = ['id','placa_mae','processador','placa_de_video','memorias','cliente']

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    pedidos = PedidoSerializer(many=True, read_only=True)
    class Meta:
        model = Cliente
        fields = ['id', 'nome','pedidos']
        