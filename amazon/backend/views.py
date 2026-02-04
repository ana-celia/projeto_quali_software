from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente, Produto
from .serializers import ClienteSerializer, ProdutoSerializer 

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer 

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
