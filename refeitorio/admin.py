from django.contrib import admin
from .models import Aluno, Funcionario, Falta

# Register your models here.

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'username')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
	list_display = ('nome', 'username')

@admin.register(Falta)
class FaltaAdmin(admin.ModelAdmin):
	list_display = ('aluno_faltante', 'data')