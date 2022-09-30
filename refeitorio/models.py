from django.db import models

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