from django.contrib import admin
from .models import *

admin.site.register(Cliente)
admin.site.register(Endereco)
admin.site.register(Servico)
admin.site.register(Pedido)
admin.site.register(Relacao)