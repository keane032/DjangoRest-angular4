from rest_framework import serializers
from .models import Cliente
from .models import Pedido

# Serializers define the API representation.

class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id','procecador','placamae','placadevideo','memoria','cliente']

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    pedidos = serializers.StringRelatedField(many=True)
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'endereco','pedidos']
 