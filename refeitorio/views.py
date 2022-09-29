from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login_aluno(request):
    return render(request, 'login_aluno.html')

def login_funcionario(request):
    return render(request, 'login_funcionario.html')