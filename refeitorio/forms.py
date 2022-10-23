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
			"Segunda-feira": "0",
			"Terça-feira": "0",
			"Quarta-feira": "0",
			"Quinta-feira": "0",
			"Sexta-feira": "0",
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
	username = forms.CharField(label='Siap', required=True)
	senha = forms.CharField(label="Senha", strip=False, widget=forms.PasswordInput(), required=True)

	def save(self):
		data = self.cleaned_data
		senha_encriptada = encriptar_senha(data['senha'])
		funcionario = Funcionario(nome=data['nome'], username=data['username'], password=senha_encriptada)
		funcionario.save()

class FuncionarioLogin(forms.Form):
	siap = forms.CharField(label='Siap', max_length=255, required=True)
	senha = forms.CharField(label="Senha", strip=False, widget=forms.PasswordInput(), required=True)

	def login(self, request):
		data = self.cleaned_data

		if Funcionario.objects.filter(username=data['siap']).exists():
			funcionario = auth.authenticate(request, username=data['siap'], password=data['senha'])
			if funcionario != None:
				auth.login(request, funcionario)
				print('Funcionario Logado')