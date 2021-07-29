from django.db import models


# Create your models here.

class AlunosBSI(models.Model):
    nome = models.CharField('Nome', max_length=100)
    periodoIngresso = models.CharField('Período de Ingresso', max_length=100)
    nota = models.DecimalField('Nota - Web Avançado', decimal_places=2, max_digits=8)
    situacao = models.CharField('Situação', max_length=100)

    def __str__(self):
        return f'{self.nome}'
