from rest_framework import serializers
from .models import Cliente, Endereco, Servico, Pedido, Relacao


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = "__all__"


class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = "__all__"


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = "__all__"


class RelacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relacao
        fields = "__all__"
