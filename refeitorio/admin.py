from django.contrib import admin
from .models import Aluno, Aluno_teste, Funcionario

# Register your models here.

admin.site.register(Aluno)
admin.site.register(Funcionario)
admin.site.register(Aluno_teste)