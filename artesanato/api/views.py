from rest_framework import viewsets, mixins
from .models import Cliente, Endereco, Servico, Pedido, Relacao
from .serializers import (
    ClienteSerializer,
    EnderecoSerializer,
    ServicoSerializer,
    PedidoSerializer,
    RelacaoSerializer
)


# SOLUÇÃO: BaseViewSet personalizado
class BaseViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """
    ViewSet base que combina mixins específicos.
    Reduz a cadeia de herança de 11 para 6 classes.
    """
    pass

# USAR BaseViewSet em vez de ModelViewSet
class ClienteViewSet(BaseViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class EnderecoViewSet(BaseViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer


class ServicoViewSet(BaseViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer


class PedidoViewSet(BaseViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class RelacaoViewSet(BaseViewSet):
    queryset = Relacao.objects.all()
    serializer_class = RelacaoSerializer
