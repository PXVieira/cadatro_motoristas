from mdls.ns import *
from mdls.cadastros import *
from sys import exit
from time import sleep
from os import system as lim

menu = [
    "Cadatrar Motorista",
    "Transportadora",
    "Responsável Liberação",
    "Registrar Entrada",
    "Registrar Saída",
    "Exibir Cadastros",
    "Sair",
]
while True:
    titulo("MENU PRICIPAL")
    for i, v in enumerate(menu):
        print(f"{i + 1} → {verde(v)}")
    linha()

    e = n_intrng("Sua escolha: ", 1, 7)
    comandos = {
        1: lambda: cdt_moto(),
        2: lambda: cdt_transportadora(),
        3: lambda: cdt_responsavel(),
        4: lambda: cdt_entrada(),
        5: lambda: cdt_saida(),
        6: lambda: exibir_cadastros(),
    }
    try:
        comando = comandos.get(e)()
    except:
        if e == 7:
            exit("Sistema finalizado... Volte sempre!")
