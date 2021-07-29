from django.shortcuts import render
from django.contrib import messages
from appDjangoDB.models import Produto
from appDjangoDB.models import AlunosBSI


# Create your views here.

def index(request):

    produtos = Produto.objects.all()
    alunos = AlunosBSI.objects.all()

    testChave = {
        'produtos': produtos,
        'alunos': alunos
    }
    return render(request, 'index.html', testChave)


def produto(request, id):

    produto = Produto.objects.get(id=id)

    context = {
        'produto': produto
    }
    return render(request, 'produto.html', context)


def alunos(request, id):

    aluno = AlunosBSI.objects.get(id=id)

    context = {
        'aluno': aluno
    }
    return render(request, 'alunos.html', context)