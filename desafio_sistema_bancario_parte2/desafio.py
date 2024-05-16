import textwrap

def menu():
    menu = """\n
    ================= MENU =================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def verificaUsuario(cpf, usuarios):
    verifica = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return verifica[0] if verifica else None

def retornaNomeUsuario(cpf, usuarios):
    verifica = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return verifica[0]["nome"] if verifica else None

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(valor, saldo, limite, numero_saques, limite_saques, extrato):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

    return

def novaConta(contas, usuarios, agencia):
    print("\n============= CRIAR CONTA =============")
    usuario = input("\nDigite o cpf do usuário: ")

    verifica_usuario = verificaUsuario(cpf=usuario, usuarios=usuarios)

    if not verifica_usuario:
        print("\nA conta precisa de um usuário cadastrado!")
        return
    
    numero_conta = len(contas) + 1

    contas.append({
        "agencia": agencia,
        "conta": numero_conta,
        "usuario": usuario
    })

    print("\nConta criada com sucesso!")

    return contas

def listarContas(contas, usuarios):
    print("\n============ LISTA DE CONTAS =============")

    if not contas:
        print("\nNão há contas a serem listadas.")
        print("\n==========================================")
        return

    for conta in contas:
        usuario = verificaUsuario(conta["usuario"], usuarios)
        print("\n   Agência: " + conta["agencia"])
        print("   Conta: " + str(conta["conta"]))
        print("   Usuário: " + usuario["nome"] + "\n")

    print("==========================================")
    return

def novoUsuario(usuarios):
    cpf = input("Informe o CPF (utilize apenas números): ")

    usuario = verificaUsuario(cpf=cpf, usuarios=usuarios)
    if usuario:
        print("\nEste usuário já está cadastrado!")
        return usuarios

    nome = input("Informe seu nome: ")
    nascimento = input("Informe sua data de nascimento: ")
    endereco = input("Informe seu endereço: (ex: Logradouro, número, bairro, cidade/Sigla Estado): ")

    usuarios.append({
        "cpf": cpf,
        "nome": nome,
        "nascimento": nascimento,
        "endereco": endereco
    })

    return usuarios

def main():
    LIMITE_SAQUES = 3
    NUMERO_AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0

    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo=saldo, valor=valor, extrato=extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = sacar(
                valor=valor,
                saldo=saldo,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
                extrato=extrato
            )

        elif opcao == "e":
            exibir_extrato(saldo=saldo, extrato=extrato)

        elif opcao == "nu":
            cadastra_usuario = novoUsuario(usuarios=usuarios)
            usuarios = cadastra_usuario

        elif opcao == "nc":
            cadastra_conta = novaConta(
                contas=contas,
                usuarios=usuarios,
                agencia=NUMERO_AGENCIA
            )
            contas = cadastra_conta
        
        elif opcao == "lc":
            listarContas(contas=contas, usuarios=usuarios)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()