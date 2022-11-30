from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.core.files import File
from .models import Aluno, Funcionario, Falta
from .forms import AlunoLogin, FuncionarioLogin, AlunoRegister, FuncionarioRegister
from datetime import datetime
from pytz import timezone
import calendar
from django.contrib import messages


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
                hora_limite = datetime.strptime("23:00:00", "%H:%M:%S").time()

                if hora_atual > hora_limite:
                    context = {
                        "nome": aluno.nome,
                        "matricula": aluno.username,
                        "quentinhas": aluno.quentinha,
                    }
                    messages.error(request, 'Não é mais possível alterar as marcações, volte antes das 16:30')
                    return render(request, 'home_aluno.html', context)
                else:
                    messages.success(request, 'Aterações realizadas com sucesso!!')
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
                messages.success(request, 'Presença cadastrada com sucesso!!')
                alunos_presentes = request.POST.getlist('alunos_presentes')

                for aluno in alunos:
                    if aluno.username not in alunos_presentes:
                        falta = Falta(aluno_faltante=aluno)
                        falta.save()
                
                return redirect('/')

            context = {
                "nome": funcionario.nome,
                "alunos_que_marcou": alunos,
            }
            return render(request, 'home_funcionario.html', context)
    return redirect('/')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso!!')
    return redirect('/')

def login_aluno(request):
    form = AlunoLogin(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        # messages.error(request, 'teste realizado com sucesso!')
        if form.login(request) == True:
            messages.success(request, 'Login realizado com sucesso!!')
            return redirect('/home/')
        else:
            messages.error(request, 'Senha ou Matrícula errada!!')
        

    context = {
        'form': form,
    }
    return render(request, 'login_aluno.html', context)

def login_funcionario(request):
    form = FuncionarioLogin(request.POST or None)

    if request.method == "POST" and form.is_valid():
        if form.login(request) == True:
            messages.success(request, 'Login realizado com sucesso!!')
            return redirect('/home/')
        else:
            messages.error(request, 'Senha ou Siap errada!!')

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
    data = datetime.now()

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
                messages.success(request, 'Justificativas enviadas com sucesso com sucesso!!')
                return redirect('/home/')

            
            context = {
                'faltas': faltas,
                'tot': len(faltas)
            }

            return render(request, 'aluno_faltas.html', context)

        elif hasattr(usuario, 'funcionario'):
            faltas = Falta.objects.all()
            dados = {}
            
            for falta in faltas:
                if falta.aluno_faltante in dados.keys():
                    dados[falta.aluno_faltante] += 1
                else:
                    dados[falta.aluno_faltante] = 1

            context = {
                'alunos': dados
            }

            return render(request, 'funcionario_faltas.html', context)
    return redirect('/')

def faltas_aluno(request, id):
    usuario = request.user

    if usuario.is_authenticated and hasattr(usuario, 'funcionario'):
        aluno = Aluno.objects.get(id=id)
        faltas = Falta.objects.filter(aluno_faltante=aluno)

        if request.method == 'POST':
            falta = get_object_or_404(faltas, id=request.POST['id'])
            falta.delete()
            messages.success(request, 'Falta deletada!!')

        context = {
            'faltas': faltas,
            'id': id,
            'aluno': aluno
        }

        return render(request, 'falta.html', context)
    return redirect('/')
def quentinhas_extras(request):
    usuario = request.user

    if usuario.is_authenticated and hasattr(usuario, 'funcionario'):
        dias = [
            'Segunda-feira',
            'Terça-feira',
            'Quarta-feira',
            'Quinta-feira',
            'Sexta-feira',
            'Sábado',
            'Domingo'
        ]
        dias_uteis = [
            'Segunda-feira',
            'Terça-feira',
            'Quarta-feira',
            'Quinta-feira',
            'Sexta-feira',
        ]

        indece_semana = datetime.now().weekday()
        dia_semana = dias[indece_semana]

        alunos = Aluno.objects.filter(quentinha__contains={f'{dia_semana}': '1'})


        hora_atual = datetime.now(timezone('America/Sao_Paulo')).time()
        inicio_almoco = datetime.strptime("11:00:00", "%H:%M:%S").time()
        fim_almoco = datetime.strptime("13:30:00", "%H:%M:%S").time()
        quentinhas_extras = 0
        total_quentinhas = 220

        if dia_semana in dias_uteis and (hora_atual >= inicio_almoco and hora_atual <= fim_almoco):
            try:
                with open('total_de_quentinhas', encoding="utf-8") as f:
                    dados = f.read().split(' ')
            except:
                with open('total_de_quentinhas', 'w', encoding="utf-8") as f:
                    f.write(f'{total_quentinhas - len(alunos)} {dia_semana}')
                dados = f'{total_quentinhas - len(alunos)} {dia_semana}'.split(' ')
            else:
                if dados[1] != dia_semana:
                    with open('total_de_quentinhas', 'w', encoding="utf-8") as f:
                        f.write(f'{total_quentinhas - len(alunos)} {dia_semana}')
            if request.method == 'POST' and int(dados[0]) > 0:
                quentinhas_extras = int(dados[0]) - 1
                with open('total_de_quentinhas', 'w', encoding="utf-8") as f:
                    f.write(f'{quentinhas_extras} {dia_semana}')
            else:
                quentinhas_extras = int(dados[0])
        else:
            messages.error(request, 'Só é possível acessar as quentinhas extras entre 11:00 e 13:30')
            quentinhas_extras = 0

        context = {
            'quentinhas_extras': quentinhas_extras,
        }

        return render(request, 'quentinhas_extras.html', context)
    return redirect('/')