from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index),
    path('login/aluno/', views.login_aluno, name='login_aluno'),
    path('login/funcionario/', views.login_funcionario, name='login_funcionario'),
    path('registrar/aluno/', views.register_aluno, name='register_aluno'),
    path('registrar/funcionario/', views.register_funcionario, name='register_funcionario'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('home/faltas/', views.faltas, name='faltas'),
    path('faltas/<int:id>', views.faltas_aluno, name='faltas_aluno'),
    path('home/quentinhas/extras/', views.quentinhas_extras, name='quentinhas_extras'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)