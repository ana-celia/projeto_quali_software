from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import ClienteViewSet, EnderecoViewSet, ServicoViewSet, PedidoViewSet, RelacaoViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

routerServicos = routers.DefaultRouter()
routerServicos.register("cliente", ClienteViewSet)
routerServicos.register("endereco", EnderecoViewSet)
routerServicos.register("servico", ServicoViewSet)
routerServicos.register("pedido", PedidoViewSet)
routerServicos.register("relacao", RelacaoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('servico/', include(routerServicos.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
