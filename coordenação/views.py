from django.shortcuts import render, get_object_or_404
from .models import Projeto, Aluno


def lista_projetos(request):
    projetos = Projeto.objects.all()
    return render(request,'coordenação/lista_projetos.html',{'projetos': projetos})

def detalhe_projeto(request, id):
    projeto = get_object_or_404(Projeto, id=id)

    return render(
        request,'coordenação/detalhe_projeto.html',{'projeto': projeto})


def detalhe_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)

    return render(request,'coordenação/detalhe_aluno.html',{'aluno': aluno})