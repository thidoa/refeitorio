from django import forms
from .models import Aluno, Funcionario
from .encrypting import encriptar_senha
from django.contrib import auth

class AlunoRegister(forms.Form):
	nome = forms.CharField(label='Nome', required=True)
	username = forms.CharField(label='Matricula', required=True)
	senha = forms.CharField(label="Senha", strip=False, widget=forms.PasswordInput(), required=True)

	def save(self):
		quentinha = {
			"segunda": "0",
			"terça": "0",
			"quarta": "0",
			"quinta": "0",
			"sexta": "0",
		}
		data = self.cleaned_data
		senha_encriptada = encriptar_senha(data['senha'])
		aluno = Aluno(nome=data['nome'], username=data['username'], password=senha_encriptada, quentinha=quentinha)
		aluno.save()

class AlunoLogin(forms.Form):
	matricula = forms.CharField(label='Matrícula', max_length=255, required=True)
	senha = forms.CharField(label="Senha", strip=False, widget=forms.PasswordInput(), required=True)

	def login(self, request):
		data = self.cleaned_data
		
		if Aluno.objects.filter(username=data['matricula']).exists():
			aluno = auth.authenticate(request, username=data['matricula'], password=data['senha'])
			if aluno != None:
				auth.login(request, aluno)
				print('Aluno Logado')

class FuncionarioRegister(forms.Form):
	nome = forms.CharField(label='Nome', required=True)
	username = forms.CharField(label='Matrícula', required=True)
	senha = forms.CharField(label="Senha", strip=False, widget=forms.PasswordInput(), required=True)

	def save(self):
		data = self.cleaned_data
		senha_encriptada = encriptar_senha(data['senha'])
		funcionario = Funcionario(nome=data['nome'], username=data['username'], password=senha_encriptada)
		funcionario.save()

class FuncionarioLogin(forms.Form):
	matricula = forms.CharField(label='Matrícula', max_length=255, required=True)
	senha = forms.CharField(label="Senha", strip=False, widget=forms.PasswordInput(), required=True)

	def login(self, request):
		data = self.cleaned_data

		if Funcionario.objects.filter(username=data['matricula']).exists():
			funcionario = auth.authenticate(request, username=data['matricula'], password=data['senha'])
			if funcionario != None:
				auth.login(request, funcionario)
				print('Funcionario Logado')