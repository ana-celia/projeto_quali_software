from django.contrib import admin
from .models import *

admin.site.register(Livro)
admin.site.register(Usuario)
admin.site.register(Autor)
admin.site.register(Editora)
admin.site.register(Emprestimo)
admin.site.register(Reserva)