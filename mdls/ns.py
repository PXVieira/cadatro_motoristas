# numeros e strings... tratamento de erros:
from rich import print


def n_int(n):
    while True:
        try:
            num = str(input(n))
            if num.isnumeric():
                num = int(num)
                return num
            else:
                print("[red]Erro! NaN[/]")
        except:
            print("[red]Erro! NaN[/]")


def n_intrng(n, i=1, f=3):
    try:
        num = str(input(n))
        if num.isnumeric():
            num = int(num)
            if num < i or num > f:
                print("[red]Erro![/] Escolha um valor entre as opções acima")
            else:
                return num
        else:
            print("[red]Erro! NaN[/]")
    except:
        print("[red]Erro! NaN[/]")


def n_float(n):
    try:
        num = str(input(n))
        if num.isnumeric():
            num = float(num)
            return num
        else:
            print("[red]Erro! NaN[/]")
    except:
        print("[red]Erro! NaN[/]")


def nome_str(s):
    try:
        nome = str(input(s)).title().strip()
        if nome.isnumeric():
            print(f"[red]Erro![/] {nome} Números não são aceitos")
        else:
            return nome
    except:
        print(f"[red]Erro![/] Valor inválido!")


def str_cpf(n):
    try:
        cpf = str(input(n)).strip().replace(".", "").replace("-", "")
        if cpf.isnumeric():
            return cpf
        else:
            print(f"[red]Erro![/] Valor inválido!")
    except:
        print(f"[red]Erro![/] Valor inválido!")


def str_SouN(sn):
    """
    Escolha sim ou não

    Args:
        sn (S/N): retorna sua escolha

    Returns:
        str: Sim ou Não
    """
    while True:
        try:
            soun = str(input(sn)).upper().strip()[0]
            if soun == "S":
                return soun
            elif soun == "N":
                continue
            else:
                print("Erro! S ou N")
        except:
            print("Erro!")


def cpf(c):
    while True:
        try:
            num = str_cpf(c)
            if len(num) < 11 or len(num) > 11:
                print(
                    f"{vermelho('CPF Inválido!')} O total de números não confere: {num} : {len(num)}"
                )
        except:
            print("CPF Inválido!")

        nove_dgts = num[:9]
        m1 = 10
        s1 = 0

        for i in nove_dgts:
            s1 += int(i) * m1
            m1 -= 1
        dgt1 = (s1 * 10) % 11
        dgt1 if dgt1 <= 9 else 0

        dez_dgts = nove_dgts + str(dgt1)
        m2 = 11
        s2 = 0

        for i in dez_dgts:
            s2 += int(i) * m2
            m2 -= 1
        dgt2 = (s2 * 10) % 11
        dgt2 if dgt2 <= 9 else 0

        comp1 = str(dgt1) + str(dgt2)
        comp2 = num[9:]
        t_or_f = True if comp1 == comp2 else False
        if t_or_f:
            return num
        else:
            print(vermelho("CPF Inválido!"))


# gerador de CPF:
def ge_cpf():
    from random import randint as rd

    rd_cpf = ""
    for i in range(9):
        rdn = rd(0, 9)
        rd_cpf += str(rdn)

    m1 = 10
    s1 = 0
    for i in rd_cpf:
        s1 += int(i) * m1
        m1 -= 1
    dg1 = (s1 * 10) % 11
    dg1 if dg1 <= 9 else 0

    d_dg = rd_cpf + str(dg1)
    m2 = 11
    s2 = 0
    for i in d_dg:
        s2 += int(i) * m2
        m2 -= 1
    dg2 = (s2 * 10) % 11
    dg2 if dg2 <= 9 else 0

    gen_cpf = str(rd_cpf) + str(dg1) + str(dg2)
    return print(gen_cpf)


def azul(txt):
    cor = f"[blue]{txt}[/]"
    return cor


def verde(txt):
    cor = f"[green]{txt}[/]"
    return cor


def vermelho(txt):
    cor = f"[red]{txt}[/]"
    return cor


def roxo(txt):
    cor = f"[purple]{txt}[/]"
    return cor


def amarelo(txt):
    cor = f"[yellow]{txt}[/]"
    return cor


def linha():
    t = print(f'{"-":-^66}')
    return t


def titulo(txt):
    linha()
    print(f"{txt:^66}")
    linha()
