from django.contrib import admin
from .models import Cliente, Endereco, Servico, Pedido, Relacao

admin.site.register(Cliente)
admin.site.register(Endereco)
admin.site.register(Servico)
admin.site.register(Pedido)
admin.site.register(Relacao)
