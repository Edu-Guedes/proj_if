from django.urls import path
from . import views

urlpatterns = [
    path('projetos/', views.lista_projetos, name='lista_projetos'),
    path('projetos/<int:id>/', views.detalhe_projeto, name='detalhe_projeto'),
    path('alunos/<int:id>/', views.detalhe_aluno, name='detalhe_aluno'),
]
