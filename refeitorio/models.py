from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Aluno(models.Model):
	nome = models.CharField(max_length=200, blank=False)
	matricula = models.CharField(max_length=20, blank=False)
	senha = models.CharField(max_length=200, blank=False)
	quentinha = models.JSONField()

class Funcionario(models.Model):
	nome = models.CharField(max_length=200, blank=False)
	siap = models.CharField(max_length=20, blank=False)
	senha = models.CharField(max_length=200, blank=False)

# Criei o Aluno_teste herdando do User

class Aluno_teste(User):
	User.username = models.CharField('Matrícula', max_length=100)
	nome = models.CharField('nome', max_length=100)