from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('login/aluno/', views.login_aluno, name='login_aluno'),
    path('login/funcionario/', views.login_funcionario, name='login_funcionario'),
    path('registrar/aluno/', views.register_aluno, name='register_aluno'),
    path('registrar/funcionario/', views.register_funcionario, name='register_funcionario'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('teste/', views.teste, name='teste'),
    path('home/faltas/', views.faltas, name='faltas'),
    path('faltas/<int:id>', views.faltas_aluno, name='faltas_aluno'),
    path('comentarios_aluno/', views.comentarios_aluno, name='comentarios_aluno'),
    path('comentarios_funcionario/', views.comentarios_funcionario, name='comentarios_funcionario'),
]