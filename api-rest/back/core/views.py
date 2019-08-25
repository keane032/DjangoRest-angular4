from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente, Pedido
from .serializers import ClienteSerializer, PedidoSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

# ViewSets define the view behavior.
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    # def retrieve(self, request, pk):
    #     queryset = Cliente.objects.all()
    #     user = get_object_or_404(queryset, nome=pk)
    #     serializer = ClienteSerializer(user)
    #     return Response(serializer.data)
   
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer