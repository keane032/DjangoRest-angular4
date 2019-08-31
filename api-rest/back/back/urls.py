from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import ClienteViewSet, PedidoViewSet, MemoriaViewSet, PlacaMaeViewSet, ProcecadorViewSet


router = routers.DefaultRouter()

router.register(r'clientes', ClienteViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'memoria',MemoriaViewSet)
router.register(r'placamae',PlacaMaeViewSet)
router.register(r'procecador', ProcecadorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
