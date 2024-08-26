from mdls.data_class import *
from mdls.ns import *
from time import sleep
from os import system as lim


# cadastrar motorista
def cdt_moto():
    nome = nome_str("Nome: ")
    gerar = str_SouN("Gerar CPF? [S/N]: ")
    if gerar == "S":
        ge_cpf()
    ncpf = cpf("CPF: ")
    celu = n_int("Celular: ")

    try:
        moto = Motorista.create(name_moto=nome, cpf_moto=ncpf, cel_moto=celu)
        print("Cadastro relizado com sucesso!")
        sleep(0.5)
        lim("cls")
    except:
        print(f"Erro! Não foi possivel realizar o cadastro de {nome}!")


# cadastrar transportadora
def cdt_transportadora():
    transportadora = nome_str("Transportadora: ")
    placa = str(input("PLACA: ")).upper().strip()
    modelo_caminhao = nome_str("Modelo Caminhão: ")
    detalhes = str(input("Detalhes: ")).capitalize().strip()

    try:
        trans = Tranportadora.create(
            transportadora=transportadora,
            placa=placa,
            modelo_caminhao=modelo_caminhao,
            detalhes=detalhes,
        )
        print("Cadastro relizado com sucesso!")
        sleep(0.5)
        lim("cls")
    except:
        print(f"Erro! Não foi possivel realizar o cadastro de {transportadora}!")


# exibir cadastros / motorista e transpotadora
def exibir_cdt():
    try:
        moto = Motorista.select()
        print(f'{"ID":<6}{"NOME":<30}{"CPF":<15}{"CONTATO":<15}')
        for i in moto:
            print(f"{i.id:<6}{i.name_moto:<30}{i.cpf_moto:<15}{i.cel_moto:<15}")
        linha()

        trans = Tranportadora.select()
        print(f'{"ID":<6}{"TRANSP.":<30}{"PLACA":<15}{"MODELO":<15}')
        for i in trans:
            print(
                f"{i.id:<6}{i.transportadora:<30}{i.placa:<15}{i.modelo_caminhao:<15}"
            )
        linha()
    except Exception as e:
        print("Erro!", type(e), ":", e)
