from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('login/aluno/', views.login_aluno, name='login_aluno'),
    path('login/funcionario/', views.login_funcionario, name='login_funcionario'),
    path('registrar/aluno/', views.register_aluno, name='register_aluno'),
    path('registrar/funcionario/', views.register_funcionario, name='register_funcionario'),
    path('home/aluno/', views.home_aluno, name='home_aluno'),
    path('home/funcionario/', views.home_funcionario, name='home_funcionario'),
]