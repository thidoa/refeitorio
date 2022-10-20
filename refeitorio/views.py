from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Aluno, Funcionario
from .forms import AlunoLogin, FuncionarioLogin, AlunoRegister, FuncionarioRegister

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    usuario = request.user

    if usuario.is_authenticated:
        if hasattr(usuario, 'aluno'):
            aluno = Aluno.objects.get(id=usuario.id)
            print(aluno.quentinha['segunda'])
            context = {
                "nome": aluno.nome,
            }
            return render(request, 'home_aluno.html', context)
        elif hasattr(usuario, 'funcionario'):
            context = {
                "nome": usuario.username
            }
            return render(request, 'home_funcionario.html', context)
        else:
            return redirect('/')
    else:
        return redirect('/')

def logout_view(request):
    logout(request)
    return redirect('/')

def login_aluno(request):
    form = AlunoLogin(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.login(request)
        return redirect('/home/')

    context = {
        'form': form,
    }

    return render(request, 'login_aluno.html', context)

def login_funcionario(request):
    form = FuncionarioLogin(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.login(request)
        return redirect('/home/')

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