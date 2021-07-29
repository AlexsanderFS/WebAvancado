from django.contrib import admin
from .models import AlunosBSI


# Register your models here.

class AlunosBSIAdmin(admin.ModelAdmin):
    list_display = ('nome', 'periodoIngresso', 'nota', 'situacao')


admin.site.register(AlunosBSI, AlunosBSIAdmin)
