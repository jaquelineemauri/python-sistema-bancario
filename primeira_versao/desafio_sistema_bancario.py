menu = f"menu principal".upper().center(60) + """

Bem vindo ao seu gerenciador bancário.

Para navegar em nosso sistema, utilize uma das opções abaixo:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==> """

saldo = 0
limite = 500
qtd_saque = 0
extrato = ""
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor que deseja depositar: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Entrada de R$ {valor:.2f}\n"
            print(f'''O valor depositado foi de R$ {valor:.2f}.''')
        else:
            print("O valor desejado não foi identificado. Volte ao Menu Principal.")
        

    elif opcao == "s":
        valor = float(input("Informe o valor que deseja sacar: R$ "))

        saldo_excedido = valor > saldo
        limite_excedido = valor > limite
        saque_excedido = qtd_saque >= LIMITE_SAQUE

        if saldo_excedido:
            print("Saldo insuficiente para realizar a transação. Volte ao Menu Principal.")       

        elif saque_excedido:
            print("Operação não realizada. Limite de saque diário excedido. Agradecemos a preferência.")
        
        elif limite_excedido:
            print("O valor desejado superou o limite por saque. Volte ao Menu Principal.")
        
        elif valor > 0 and valor <= 500:
                saldo -= valor
                extrato += f"Saída de R$ {valor:.2f}\n"
                print(f'''O valor sacado foi de R$ {valor:.2f}.''')
                qtd_saque += 1
        
        else:
            print("Operação não realizada. Valor não identificado. Volte ao Menu Principal.")
    
    elif opcao == "e":
        if not extrato:
            print("Seu extrato de transações".upper().center(30))
            print("Não houve transações realizadas.")
            print(f"Saldo: R$ {saldo:.2f}")


        else:
            print("Seu extrato de transações")
            print(extrato)
            print(f"Saldo: R$ {saldo:.2f}")
    
    elif opcao == "q":
        print("Agradecemos a preferência e confiança em nosso gerenciador.")
        break

    else:
        print("Operação inválida. Por favor, selecione novamente a operação desejada.")