from django.contrib import admin
from .models import Produto, Cliente, AlunosBSI


# Register your models here.


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')


class AlunosBSIAdmin(admin.ModelAdmin):
    list_display = ('nome', 'periodoIngresso', 'nota', 'situacao')


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente)
admin.site.register(AlunosBSI, AlunosBSIAdmin)
