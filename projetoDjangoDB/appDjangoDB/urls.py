from django.urls import path
from appDjangoDB.views import index, alunos

urlpatterns = [
    path('', index, name="index"),
    path('alunos/<int:id>', alunos, name='alunos'),
]
