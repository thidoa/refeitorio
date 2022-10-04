from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Aluno, Funcionario
from .forms import AlunoLogin, FuncionarioLogin, AlunoRegister, FuncionarioRegister

# Create your views here.

def index(request):
    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def home_aluno(request):
    aluno = request.user

    if aluno.is_authenticated:
        context = {
            "nome": aluno.username
        }
        return render(request, 'home_aluno.html', context)
    else:
        return redirect('/')

def home_funcionario(request):
    funcionario = request.user

    if funcionario.is_authenticated:
        context = {
            "nome": funcionario.username
        }
        return render(request, 'home_funcionario.html', context)
    else:
        return redirect('/')

def login_aluno(request):
    form = AlunoLogin(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.login(request)
        return redirect('/home/aluno/')

    context = {
        'form': form,
    }

    return render(request, 'login_aluno.html', context)

def login_funcionario(request):
    form = FuncionarioLogin(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.login(request)
        return redirect('/home/funcionario/')

    context = {
        'form': form,
    }

    return render(request, 'login_funcionario.html', context)

def register_aluno(request):
    form = AlunoRegister(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('/login/aluno/')

    context = {
        'form': form,
    }
    return render(request, 'register_aluno.html', context)

def register_funcionario(request):
    form = FuncionarioRegister(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('/login/funcionario')

    context = {
        'form': form,
    }

    return render(request, 'register_funcionario.html', context)