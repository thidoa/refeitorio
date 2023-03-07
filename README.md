# Sistema para o refeitório do IFPB
Esse é um projeto de estudos que foi desenvolvido para automatizar processos relativos ao refeitório do IFPB campus Patos. Todo o projeto foi desenvolvido usando o framework Django + Bootstrap. 

## Requisitos
- Python 3.8+
- Banco de dados MySQL/MariaDB
- Git

## Rodando o projeto
Clone este repo:
```
git clone git@github.com:thidoa/refeitorio.git
```
Já estando no diretório do projeto instale as dependências:
```
pip install -r requirements.txt
```
Crie um banco de dados para o projeto e adicione um arquivo .env na raiz do projeto de acordo com o arquivo .env.example. depois crie as tabelas do banco com o comando:
```
python manage.py migrate
```
Após isso inicie a aplicação com
```
python manage.py runserver
```
