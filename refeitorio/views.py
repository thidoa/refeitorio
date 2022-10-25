from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Aluno, Funcionario
from .forms import AlunoLogin, FuncionarioLogin, AlunoRegister, FuncionarioRegister
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    usuario = request.user

    if usuario.is_authenticated:
        if hasattr(usuario, 'aluno'):
            aluno = Aluno.objects.get(id=usuario.id)

            if request.method == 'POST':
                dias = request.POST.getlist('dias_da_semana')

                for dia in aluno.quentinha.keys():
                    if dia in dias:
                        aluno.quentinha[dia] = '1'
                    else:
                        aluno.quentinha[dia] = '0'

                aluno.save(update_fields=['quentinha'])    
                return redirect('/')

            context = {
                "nome": aluno.nome,
                "matricula": aluno.username,
                "quentinhas": aluno.quentinha
            }

            return render(request, 'home_aluno.html', context)
        elif hasattr(usuario, 'funcionario'):
            alunos = Aluno.objects.all()
        
            dias = [
                'Segunda-feira',
                'Terça-feira',
                'Quarta-feira',
                'Quinta-feira',
                'Sexta-feira',
                'Sábado',
                'Domingo'
            ]

            indece_semana = datetime.now().weekday()
            dia_semana = dias[indece_semana]

            print(dia_semana)
            alunos_que_marcou = []
            
            for aluno in alunos:
                if(aluno.quentinha[dia_semana] == '1'):
                    alunos_que_marcou.append(aluno)


            context = {
                "nome": usuario.username,
                "alunos_que_marcou": alunos_que_marcou
            }
            return render(request, 'home_funcionario.html', context)
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
        return redirect('/login/funcionario/')

    context = {
        'form': form,
    }

    return render(request, 'register_funcionario.html', context)