from django.db import models
from django.contrib.auth.models import User

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