from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.core.files import File
from .models import Aluno, Funcionario, Falta
from .forms import AlunoLogin, FuncionarioLogin, AlunoRegister, FuncionarioRegister
from datetime import datetime
from pytz import timezone
import calendar

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    usuario = request.user

    if usuario.is_authenticated:
        if hasattr(usuario, 'aluno'):
            aluno = Aluno.objects.get(id=usuario.id)

            if request.method == 'POST':
                hora_atual = datetime.now(timezone('America/Sao_Paulo')).time()
                hora_limite = datetime.strptime("16:30:00", "%H:%M:%S").time()

                if hora_atual > hora_limite:
                    context = {
                        "nome": aluno.nome,
                        "matricula": aluno.username,
                        "quentinhas": aluno.quentinha,
                        "mensagem": "Não é mais possível alterar as marcações, volte antes das 16:30"
                    }
                    return render(request, 'home_aluno.html', context)

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
                "quentinhas": aluno.quentinha,
                "mensagem": ""
            }

            return render(request, 'home_aluno.html', context)
        elif hasattr(usuario, 'funcionario'):
            funcionario = Funcionario.objects.get(id=usuario.id)
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

            alunos = Aluno.objects.filter(quentinha__contains={f'{dia_semana}': '1'})

            if request.method == 'POST':
                alunos_presentes = request.POST.getlist('alunos_presentes')

                for aluno in alunos:
                    if aluno.username not in alunos_presentes:
                        falta = Falta(aluno_faltante=aluno)
                        falta.save()
                
                return redirect('/')

            context = {
                "nome": funcionario.nome,
                "alunos_que_marcou": alunos
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

def teste(request):
    data = datetime.datetime.now()

    dia_mes_atual = []
    dia_calendario = []

    obj = calendar.Calendar(firstweekday = 6)
    for day in obj.itermonthdays(data.year, data.month):
        dia_mes_atual.append(day)
        #print(day)

    data_mes = calendar.Calendar(firstweekday = 6)
    for dia in data_mes.itermonthdates(data.year, data.month):
        data_dia = str(dia).split('-')
        dia_calendario.append(data_dia[-1])

    mes_completo = []

    for valor in range(len(dia_mes_atual)):
        mes_completo.append([dia_mes_atual[valor], dia_calendario[valor]])
   
    dias_semana = []
    semana_mes =[]
    contador = 0
    for dia in dia_calendario:
        if contador < 6:
            dias_semana.append(dia)
            contador+=1
        else:
            dias_semana.append(dia)
            semana_mes.append(dias_semana)
            dias_semana = []
            contador = 0
    
    context = {
        'dia_mes_atual': dia_mes_atual,
        'mes': semana_mes,
        'agora_vai': mes_completo,
    }
    return render(request, 'teste.html', context)

def faltas(request):
    usuario = request.user

    if usuario.is_authenticated:
        if hasattr(usuario, 'aluno'):
            aluno = Aluno.objects.get(id=usuario.id)
            
            faltas = Falta.objects.filter(aluno_faltante=aluno)

            if request.method == "POST":
                faltass = request.POST.getlist('justificativa')
                ids = request.POST.getlist('id_falta')
                arquivos = request.FILES.getlist('arquivo')
                cont = 0

                for id in ids:
                    falta = Falta.objects.get(id=id)
                    falta.justificativa = faltass[cont]

                    if len(arquivos) != 0:
                        falta.arquivo = arquivos[cont]

                    falta.save(update_fields=['justificativa', 'arquivo'])
                    cont += 1

                return redirect('/home/')

            
            context = {
                'faltas': faltas,
            }

            return render(request, 'aluno_faltas.html', context)

        elif hasattr(usuario, 'funcionario'):
            funcionario = Funcionario.objects.get(id=usuario.id)
            
            return render(request, 'home_funcionario.html', context)
    return redirect('/')


    #return render(request, 'faltas.html', context)

