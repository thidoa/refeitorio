from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('login_aluno/', views.login_aluno, name ='login_aluno'),
    path('login_funcionario', views.login_funcionario, name='login_funcionario')
]