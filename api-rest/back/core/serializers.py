from rest_framework import serializers
from .models import Cliente
from .models import Pedido

# Serializers define the API representation.

class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id','procecador','placamae','placadevideo','memoria']

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
   
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'endereco']
 