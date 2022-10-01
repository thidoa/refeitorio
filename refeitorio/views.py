from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Aluno, Funcionario
from .forms import AlunoLogin, FuncionarioLogin, AlunoRegister, FuncionarioRegister, AlunoRegisterTeste
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def index(request):
    return render(request, 'index.html')

# Modifiquei o login_aluno e o register aluno de acordo com as outras alterações

def login_aluno(request):
    form = AlunoLogin(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.login(request)

    context = {
        'form': form,
    }

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
    form = AlunoRegisterTeste(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()

    context = {
        'form': form,
    }
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