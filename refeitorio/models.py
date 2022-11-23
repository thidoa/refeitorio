from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Aluno(User):
	User.username = models.CharField('Matrícula', max_length=255)
	nome = models.CharField('Nome', max_length=255)
	quentinha = models.JSONField()

	def __str__(self):
		return self.nome

class Funcionario(User):
	User.username = models.CharField('Siap', max_length=255)
	nome = models.CharField('Nome', max_length=255)

	def __str__(self):
		return self.nome

class Falta(models.Model):
	aluno_faltante = models.ForeignKey(Aluno, on_delete=models.CASCADE)
	data = models.DateField(default=date.today)
	justificativa = models.TextField(blank=True, null=True)
	arquivo = models.FileField(upload_to='uploads/', blank=True, default='null')

	def __str__(self):
		return self.aluno_faltante.nome