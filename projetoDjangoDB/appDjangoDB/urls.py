from django.urls import path
from appDjangoDB.views import index, produto, alunos

urlpatterns = [
    path('', index, name="index"),
    path('produto/<int:id>', produto, name='produto'),
    path('alunos/<int:id>', alunos, name='alunos'),
]
