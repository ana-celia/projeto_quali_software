from rest_framework import viewsets
from .models import Cliente, Endereco, Servico, Pedido, Relacao
from .serializers import (
    ClienteSerializer,
    EnderecoSerializer,
    ServicoSerializer,
    PedidoSerializer,
    RelacaoSerializer
)


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer


class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class RelacaoViewSet(viewsets.ModelViewSet):
    queryset = Relacao.objects.all()
    serializer_class = RelacaoSerializer
