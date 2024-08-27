from peewee import *
from rich import print
from time import sleep
from os import system as lp
from tqdm import tqdm

db = SqliteDatabase("db_moto.db")


class Motorista(Model):
    name_moto = CharField()
    cpf_moto = CharField(unique=True)
    cel_moto = CharField()

    class Meta:
        database = db


class Tranportadora(Model):
    transportadora = CharField()
    placa = CharField(unique=True)
    modelo_caminhao = CharField()
    detalhes = TextField()

    class Meta:
        database = db


class Responsavel(Model):
    nome_responsavel = CharField(unique=True)
    identificacao = CharField(unique=True)
    setor = CharField()
    ramal = CharField()

    class Meta:
        database = db


class EntradaSaida(Model):
    nome_moto = ForeignKeyField(Motorista, backref="entrada")
    placa_trans = ForeignKeyField(Tranportadora, backref="entrada")
    nome_resp = ForeignKeyField(Responsavel, backref="entrada")
    hora_entrada = DateTimeField()
    hora_saida = DateTimeField(null=True)  # Campo para registrar a saída

    class Meta:
        database = db


try:
    db.connect()
    print("Banco de dodos conectado com [green]sucesso![/]")
except:
    print("[red]Erro![/]")

try:
    db.create_tables([Motorista, Tranportadora, Responsavel, EntradaSaida])
    for i in tqdm(range(100), desc="Criando tabelas!"):
        sleep(0.01)
    lp("cls")
except:
    print("[red]Erro![/]")
