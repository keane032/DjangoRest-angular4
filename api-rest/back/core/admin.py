from django.contrib import admin
from .models import Cliente, Pedido, Memoria, PlacaMae, Processador
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Memoria)
admin.site.register(PlacaMae)
admin.site.register(Processador)
