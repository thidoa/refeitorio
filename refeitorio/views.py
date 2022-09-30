from django.shortcuts import render, redirect
from .models import Aluno, Funcionario
from .forms import AlunoLogin, FuncionarioLogin, AlunoRegister, FuncionarioRegister

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login_aluno(request):
    context = {}

    if request.method == 'POST':
        pass
    else:
        form = AlunoLogin()
        context['form'] = form
    
    return render(request, 'login_aluno.html', context)

def login_funcionario(request):
    context = {}

    if request.method == 'POST':
        pass
    else:
        form = FuncionarioLogin()
        context['form'] = form

    return render(request, 'login_funcionario.html', context)

def register_aluno(request):
    context = {}

    if request.method == 'POST':
        pass
    else:
        form = AlunoRegister()
        context['form'] = form

    return render(request, 'register_aluno.html', context)

def register_funcionario(request):
    context = {}

    if request.method == 'POST':
        pass 
    else:
        form = FuncionarioRegister()
        context['form'] = form

    return render(request, 'register_funcionario.html', context)