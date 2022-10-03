from django.contrib import admin
from .models import Aluno, Funcionario

# Register your models here.

admin.site.register(Aluno)
admin.site.register(Funcionario)