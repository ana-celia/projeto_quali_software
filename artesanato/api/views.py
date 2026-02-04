from rest_framework import viewsets, status
from .models import *
from .serializers import * 
from rest_framework.decorators import action
from rest_framework.response import Response


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer 

    # @action(detail=True, methods=["get"], url_path="valorRecebidoTotal")
    # def valorRecebido(self, request):
    #     try:
    #         cliente = request.data.get("cliente_id")
    #         pedidos = Pedido.objects.get(cliente=cliente)
    #         valor = 0
    #         for p in pedidos:
    #             valor += pedidos.valorTotal
    #             return Response({f"detail": "O valor recebido no total pelo cliente {cliente.nome} foi {valor}."})
    #     except pedidos.DoesNotExist:
    #         return Response({"detail": "Sem pedidos relacionados a este usuário."}, status=status.HTTP_404_NOT_FOUND)

        

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = Servicoerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class RelacaoViewSet(viewsets.ModelViewSet):
    queryset = Relacao.objects.all()
    serializer_class = RelacaoSerializer    
