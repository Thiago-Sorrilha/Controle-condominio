# "c:/Users/thiago.sorrilha/Desktop/Projeto_Python/venv/Scripts/Activate.ps1
# "PS C:\Users\thiago.sorrilha\Desktop\Projeto_Python> python manage.py runserver

# python manage.py makemigrations usuarios
# python manage.py migrate
# http://127.0.0.1:8000/

# usuario admin: thiago_sorrilha@hotmail.com
# Senha:sorrilha


import sqlite3

connection = sqlite3.connect('db.sqlite3')
c = connection.cursor()

# SQL


def create_table():
    c.execute(
        'CREATE TABLE IF NOT EXISTS teste_tabela (id integer, teste_tabela text)')


create_table()


def dataentry():
    c.execute("INSERT INTO teste_tabela VALUES(1, 'Thiago')")


dataentry()
