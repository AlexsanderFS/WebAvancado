from django.shortcuts import render
from django.contrib import messages
from appDjangoDB.models import AlunosBSI


# Create your views here.

def index(request):

    alunos = AlunosBSI.objects.all()

    testChave = {
        'alunos': alunos
    }
    return render(request, 'index.html', testChave)


def alunos(request, id):

    aluno = AlunosBSI.objects.get(id=id)

    context = {
        'aluno': aluno
    }
    return render(request, 'alunos.html', context)