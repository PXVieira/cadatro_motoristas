from mdls.data_class import *
from mdls.ns import *
from time import sleep
from os import system as lim
from datetime import datetime as dt


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
    placa = str(input("Placa: ")).upper().strip()
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


# cadastrar responsável pela liberação
def cdt_responsavel():
    responsavel = nome_str("Responsável: ")
    identificacao = str(input("ID/RT: ")).upper().strip()
    setor = str(input("Setor: ")).upper().strip()
    ramal = str(input("Ramal: ")).capitalize().strip()

    try:
        resp = Responsavel.create(
            nome_responsavel=responsavel,
            identificacao=identificacao,
            setor=setor,
            ramal=ramal,
        )
        print("Cadastro relizado com sucesso!")
        sleep(0.5)
        lim("cls")
    except:
        print(f"Erro! Não foi possivel realizar o cadastro de {responsavel}!")


def cdt_entrada():
    while True:
        try:
            nome_moto = nome_str("Motorista: ")
            try:
                motorista = Motorista.get(Motorista.name_moto == nome_moto)
            except Motorista.DoesNotExist:
                print(f"Erro: Motorista '{nome_moto}' não encontrado.")
                continue

            placa_trans = str(input("Placa: ")).upper().strip()
            try:
                transportadora = Tranportadora.get(Tranportadora.placa == placa_trans)
            except Tranportadora.DoesNotExist:
                print(f"Erro: Caminhão com a placa '{placa_trans}' não encontrado.")
                continue

            nome_resp = nome_str("Nome Responsável: ")
            try:
                responsavel = Responsavel.get(Responsavel.nome_responsavel == nome_resp)
            except Responsavel.DoesNotExist:
                print(f"Erro: Responsável '{nome_resp}' não encontrado.")
                continue

            hora_entrada = dt.now()

            try:
                entrada = EntradaSaida.create(
                    nome_moto=nome_moto,
                    placa_trans=placa_trans,
                    nome_resp=nome_resp,
                    hora_entrada=hora_entrada,
                )
                print("Entrada relizada com sucesso!")
                sleep(0.5)
                lim("cls")
            except:
                print(f"Erro! Não foi possível realizar a entrada do {nome_moto}")

        except Exception as e:
            print(f"Erro ao registrar entrada: {e}")

        sair = str_SouN("Registrar nova entrada? [S/N]: ")
        if sair == "N":
            print("Saindo do sistema...")
            sleep(1)
            break
        elif sair == "S":
            continue
        else:
            print("Erro! Apenas S ou N")


def cdt_saida():
    while True:
        try:
            # Captura o ID do Motorista para identificar a entrada
            nome = nome_str("Motorista: ")

            # Tenta encontrar a última entrada do motorista que ainda não tenha saída registrada
            entrada = EntradaSaida.get(
                (EntradaSaida.nome_moto_id == nome)
                & (EntradaSaida.hora_saida.is_null(True))
            )

            # Captura a data e hora atuais para registrar a saída
            hora_saida = dt.now()

            # Atualiza o registro com a data e hora de saída
            entrada.hora_saida = hora_saida
            entrada.save()

            print("Saída registrada com sucesso!")

        except EntradaSaida.DoesNotExist:
            print("Erro: Nenhuma entrada encontrada para esse motorista.")
        except Exception as e:
            print(f"Erro ao registrar saída: {e}")

        sair = input("Registrar nova saída? [S/N]: ").upper()[0]
        if sair == "N":
            print("Saindo do sistema...")
            sleep(1)
            break
        elif sair == "S":
            continue
        else:
            print("Erro! Apenas S ou N")


# exbir cadastros de motoristas
def exibir_cdt_moto():
    try:
        moto = Motorista.select()
        print(f'{"ID":<6}{"NOME":<30}{"CPF":<15}{"CONTATO":<15}')
        for i in moto:
            print(f"{i.id:<6}{i.name_moto:<30}{i.cpf_moto:<15}{i.cel_moto:<15}")
        linha()

    except Exception as e:
        print("Erro!", type(e), ":", e)


# exbir cadastros de transportadoras
def exibir_cdt_trans():
    try:
        trans = Tranportadora.select()
        print(f'{"ID":<6}{"TRANSP.":<30}{"PLACA":<15}{"MODELO":<15}')
        for i in trans:
            print(
                f"{i.id:<6}{i.transportadora:<30}{i.placa:<15}{i.modelo_caminhao:<15}"
            )
        linha()

    except Exception as e:
        print("Erro!", type(e), ":", e)


# exbir cadastros de responsáveis
def exibir_cdt_resp():
    try:

        resp = Responsavel.select()
        print(f'{"ID":<6}{"NOME":<30}{"SETOR":<15}{"RAMAL":<15}')
        for i in resp:
            print(f"{i.id:<6}{i.nome_responsavel:<30}{i.setor:<15}{i.ramal:<15}")
        linha()

    except Exception as e:
        print("Erro!", type(e), ":", e)


# exibir entradas:
def exbir_entrada():
    try:
        titulo("REGISTROS DE ENTRADA")

        entrada = EntradaSaida.select()
        print(
            f'{"ID":<6}{"NOME":<30}{"RESPONSÁVEL":<25}{"HORA DA ENTRADA":<22}{"HORA SAÍDA":<22}'
        )
        for i in entrada:
            print(
                f"{i.id:<6}{i.nome_moto_id:<30}{i.nome_resp_id:<25}{i.hora_entrada.strftime('%d/%m/%Y %H:%M:%S'):<60}{i.hora_saida.strftime('%d/%m/%Y %H:%M:%S'):<60}"
            )

        linha()

    except Exception as e:
        print("Erro!", type(e), ":", e)


def exibir_cadastros():
    cadastros = [
        "Motoristas",
        "Transportadoras/Placas",
        "Resposnsáveis",
        "Entradas/Saídas",
        "Sair",
    ]
    while True:
        titulo("MENU DE CADASTROS")
        for i, v in enumerate(cadastros):
            print(f"{i + 1} → {verde(v)}")
        linha()

        e = n_intrng("Sua escolha: ", 1, 5)
        comandos = {
            1: lambda: exibir_cdt_moto(),
            2: lambda: exibir_cdt_trans(),
            3: lambda: exibir_cdt_resp(),
            4: lambda: exbir_entrada(),
        }
        try:
            comando = comandos.get(e)()
        except:
            if e == 5:
                break
