from datetime import datetime
from pytz import timezone

dias_da_semana = [
	'Segunda-feira',
	'Terça-feira',
	'Quarta-feira',
	'Quinta-feira',
	'Sexta-feira',
	'Sábado',
	'Domingo'
]
dias_uteis = [
	'Segunda-feira',
	'Terça-feira',
	'Quarta-feira',
	'Quinta-feira',
	'Sexta-feira',
	'Domingo'
]


def hora_atual():
	return datetime.now(timezone('America/Sao_Paulo')).time()

def hora_limite_marcacoes():
	return datetime.strptime("23:00:00", "%H:%M:%S").time()

def dia_de_hoje():
	indece_semana = datetime.now().weekday()
	return dias_da_semana[indece_semana]

def inicio_almoco():
	return datetime.strptime("08:00:00", "%H:%M:%S").time()

def fim_almoco():
	return datetime.strptime("23:00:00", "%H:%M:%S").time()

def dia_util():
	return dia_de_hoje() in dias_uteis