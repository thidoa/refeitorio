from django import forms
from .models import Aluno_teste
from .encrypting import encriptar_senha
from django.contrib import auth

class FuncionarioRegister(forms.Form):
	nome = forms.CharField(label='Nome ', required=True, max_length=200)
	siap = forms.CharField(label='Siap', required=True, max_length=20)
	senha = forms.CharField(label='Senha', required=True, max_length=200)

class AlunoRegister(forms.Form):
	nome = forms.CharField(label='Nome', required=True, max_length=200)
	matricula = forms.CharField(label='Matricula', required=True, max_length=20)
	senha = forms.CharField(label='Senha', required=True, max_length=200)
	quentinha = forms.JSONField(required=True)

class AlunoLogin(forms.Form):
	matricula = forms.CharField(label='Matricula', max_length=20, required=True)
	senha = forms.CharField(label='Senha', max_length=200, required=True)

# Adicionei uma função para fazer login

	def login(self, request):
		data = self.cleaned_data
		
		if Aluno_teste.objects.filter(username=data['matricula']).exists():
			aluno = auth.authenticate(request, username=data['matricula'], password=data['senha'])
			print('passei aluno')
			if aluno != None:
				print('passei if')
				auth.login(request, aluno)
				print("logado")
			


class FuncionarioLogin(forms.Form):
	siap = forms.CharField(label='Siap', max_length=200, required=True)
	senha = forms.CharField(label='Senha', max_length=200, required=True)

# criei o formulário de cadastrar o aluno com uma função para salvar, e criei um arquivo encrypting.py para encriptar as senhas

class AlunoRegisterTeste(forms.Form):
	nome = forms.CharField(label='Nome', required=True)
	username = forms.CharField(label='Matricula', required=True)
	senha = forms.CharField(label="Senha", strip=False, widget=forms.PasswordInput())

	def save(self):
		data = self.cleaned_data
		senha_encriptada = encriptar_senha(data['senha'])
		aluno = Aluno_teste(nome=data['nome'], username=data['username'], password=senha_encriptada)
		aluno.save()

