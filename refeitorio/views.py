from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import logout
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

    usuario = request.user
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


        data = datetime.now()

        dia_atual = data.day

        dia_mes_atual = []
        dia_calendario = []

        obj = calendar.Calendar(firstweekday = 6)
        for day in obj.itermonthdays(data.year, data.month):
            dia_mes_atual.append(day)

        data_mes = calendar.Calendar(firstweekday = 6)
        for dia in data_mes.itermonthdates(data.year, data.month):
            data_dia = str(dia).split('-')
            dia_calendario.append(data_dia[-1])

        mes_completo = []

        mescompleto2 = []

        for valor in range(len(dia_mes_atual)):
            mes_completo.append([dia_mes_atual[valor], dia_calendario[valor]])


        dias_semana2 = []
        semana_mes2 =[]
        contador2 = 0
        for dia in mes_completo:
            if contador2 < 6:
                dias_semana2.append(dia)
                contador2+=1
            else:
                dias_semana2.append(dia)
                semana_mes2.append(dias_semana2)
                dias_semana2 = []
                contador2 = 0


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

        semana_atual = 0
        for i in range(len(semana_mes)):
            if str(dia_atual) in semana_mes[i]:
                semana_atual = semana_mes[i]

        semana_quentinha = []
        for i in range(len(semana_atual)):
            if i != 0 and i != len(semana_atual):
                semana_quentinha.append(semana_atual[i])

        teste = []
        lista_menor = []
        c = 0
        for quentinha in aluno.quentinha:
            lista_menor = [semana_quentinha[c] ,aluno.quentinha[quentinha]]
            teste.append(lista_menor)
            c += 1

        print(teste)

        context = {
            'dia_mes_atual': dia_mes_atual,
            'mes': semana_mes,
            'agora_vai': mes_completo,
            'mes2': semana_mes2,
            'dia_atual': dia_atual,
            'semana_atual': semana_atual,
            "quentinhas": aluno.quentinha,
            'teste': teste,
        }

        print(semana_atual)


    return render(request, 'teste.html', context)

def faltas(request):
    faltas = Falta.objects.all()

    context = {
        'faltas': faltas,
    }

    return render(request, 'faltas.html', context)

