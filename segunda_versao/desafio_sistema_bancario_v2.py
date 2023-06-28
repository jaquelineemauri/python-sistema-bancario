def menu_principal():
    menu_principal = f"""\n======================== MENU PRINCIPAL ========================

    Bem vindo ao seu gerenciador bancário.

    Para navegar em nosso sistema, utilize uma das opções abaixo:
    [u]\t Novo Usuário
    [c]\t Nova Conta
    [l]\t Listas Contas
    [d]\t Depositar
    [s]\t Sacar
    [e]\t Extrato
    [q]\t Sair

    ==> """
    return input(menu_principal)

def criar_usuario(usuarios):
    cpf = input("Informe um CPF válido (somente os números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nCPF já existe em nosso sistema.")
        
        return
    nome = input("Informe seu nome completo: ")
    data_nasc = input("Informe sua data de nascimento (aa-mm-aaaa): ")
    endereco = input("""Informe seu endereço (Logradouro, nº - Bairro - Cidade/UF): """)

    usuarios.append({"nome":nome, "data_nasc":data_nasc, "cpf":cpf, "endereco":endereco})

    print("\nUsuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("\nInforme seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta cadastrada com sucesso.")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário de conta não encontrado. Verifique seu cadastro de usuário.")


def listar_contas(contas):
    for conta in contas:
        pessoa = f"""
            Titular:\t{conta['usuario']['nome']}
            Agência:\t{conta['agencia']}
            C/C.:\t\t{conta['numero_conta']}        
        """
        print(pessoa)


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Entrada de R$\t {valor:.2f}\n"
        print(f'''\nO valor depositado foi de R$ {valor:.2f}.\n''')
    else:
        print("O valor desejado não foi identificado. Volte ao Menu Principal.\n")
    
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saque, limite_saque):
    saldo_excedido = valor > saldo
    limite_excedido = valor > limite
    saque_excedido = numero_saque >= limite_saque

    if saldo_excedido:
        print("\nSaldo insuficiente para realizar a transação. Volte ao Menu Principal.\n")       

    elif saque_excedido:
        print("\nOperação não realizada. Limite de saque diário excedido. Agradecemos a preferência.\n")
        
    elif limite_excedido:
        print("\nO valor desejado superou o limite por saque. Volte ao Menu Principal.\n")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saída de R$\t {valor:.2f}\n"
        numero_saque += 1
        print(f'''\nO valor sacado foi de R$ {valor:.2f}.\n''')
        
    else:
        print("\nOperação não realizada. Valor não identificado. Volte ao Menu Principal.\n")

    return saldo, extrato, numero_saque


def exibir_extrato(saldo, /, *, extrato):
        print("\nSeu extrato de transações\n".upper().center(60))
        print("Não houve transações realizadas." if not extrato else extrato)
        print(f"\nSaldo: R$\t {saldo:.2f}\n")


def menu():
    saldo = 0
    limite = 500
    numero_saque = 0
    extrato = ""
    LIMITE_SAQUE = 3
# Agurmentos para as novas funções
    AGENCIA = "0001"
    usuarios = []
    contas = []
#Argumento criado para a conta sequêncial
    numero_conta = 1

    while True:
        opcao = menu_principal()

        if opcao == "d":
            valor = float(input("\nInforme o valor que deseja depositar:\t R$ "))

            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            valor = float(input("\nInforme o valor que deseja sacar:\t R$ "))

            saldo, extrato, numero_saque = sacar(saldo=saldo,
                                                 valor=valor,
                                                extrato=extrato,
                                                limite=limite,
                                                numero_saque=numero_saque,
                                                limite_saque=LIMITE_SAQUE)
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "q":
            print("\nAgradecemos a preferência e confiança em nosso gerenciador.\n")
            break

        else:
            print("\nOperação inválida. Por favor, selecione novamente a operação desejada.\n")

menu()