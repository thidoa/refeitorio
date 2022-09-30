from django import forms

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

class FuncionarioLogin(forms.Form):
	siap = forms.CharField(label='Siap', max_length=200, required=True)
	senha = forms.CharField(label='Senha', max_length=200, required=True)
