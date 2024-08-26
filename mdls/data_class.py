from peewee import *
from rich import print
from time import sleep
from os import system as lp
from tqdm import tqdm

db = SqliteDatabase("db_moto.db")


class Motorista(Model):
    name_moto = CharField()
    cpf_moto = CharField()
    cel_moto = CharField()

    class Meta:
        database = db


class Tranportadora(Model):
    transportadora = CharField()
    placa = CharField()
    modelo_caminhao = CharField()
    detalhes = TextField()

    class Meta:
        database = db


try:
    db.connect()
    print("Banco de dodos conectado com [green]sucesso![/]")
except:
    print("[red]Erro![/]")

try:
    db.create_tables([Motorista, Tranportadora])
    for i in tqdm(range(100), desc="Criando tabelas!"):
        sleep(0.01)
    lp("cls")
except:
    print("[red]Erro![/]")
