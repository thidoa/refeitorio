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
    path('faltas/', views.faltas, name='faltas'),
    path('quentinhas_extras/', views.quentinhas_extras, name='quentinhas_extras'),
]