from django.shortcuts import render, redirect
from .models import Aluno, Funcionario
from .forms import AlunoLogin, FuncionarioLogin, AlunoRegister, FuncionarioRegister
from django.contrib.auth.hashers import make_password

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
        nome = request.POST['nome']
        matricula = request.POST['matricula']
        senha = request.POST['senha']
        quentinha = request.POST['quentinha']

        password_hash = make_password(password=senha, hasher='argon2')

        aluno = Aluno(nome=nome, matricula=matricula, quentinha=quentinha, senha=password_hash)
        aluno.save()

        return render(request, 'index.html')
    else:
        form = AlunoRegister()
        context['form'] = form

    return render(request, 'register_aluno.html', context)

def register_funcionario(request):
    context = {}

    if request.method == 'POST':
        nome = request.POST['nome']
        siap = request.POST['siap']
        senha = request.POST['senha']
        
        password_hash = make_password(password=senha, hasher='argon2')

        funcionario = Funcionario(nome=nome, siap=siap, senha=password_hash)
        funcionario.save()

        return render(request, 'index.html')
    else:
        form = FuncionarioRegister()
        context['form'] = form

    return render(request, 'register_funcionario.html', context)