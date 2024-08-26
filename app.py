from mdls.ns import *
from mdls.cadastros import *
from sys import exit
from time import sleep
from os import system as lim

menu = ["Cadatrar motorista", "Transportadora", "Exibir Cadastros", "Sair"]
while True:
    titulo("MENU PRICIPAL")
    for i, v in enumerate(menu):
        print(f"{i + 1} → {verde(v)}")
    linha()

    e = n_intrng("Sua escolha: ", 1, 4)
    comandos = {
        1: lambda: cdt_moto(),
        2: lambda: cdt_transportadora(),
        3: lambda: exibir_cdt(),
    }
    try:
        comando = comandos.get(e)()
    except:
        if e == 4:
            exit("Sistema finalizado... Volte sempre!")

# while True:
#     titulo("MENU PRICIPAL")
#     for i, v in enumerate(menu):
#         print(f"{i + 1} → {verde(v)}")
#     linha()
#     e = n_intrng("Sua escolha: ")

#     if e == 1:
#         sleep(0.5)
#         lp("cls")
#         titulo(f"{menu[0]}")
#         cdt_moto()

#     elif e == 2:
#         sleep(0.5)
#         lp("cls")
#         titulo(f"{menu[1]}")
#         exibir_cdt()

#     else:
#         sleep(0.5)
#         lp("cls")
#         titulo(f"{menu[2]}")
#         exit("Sistema finalizado... Volte sempre!")
