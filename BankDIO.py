menu = """
Banco DIO
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
LIMITE_DO_SAQUE = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Operacao nao realizada! O valor informado e invalido!")
    elif opcao == "s":
        valor = float(input("Informe o valor a ser sacado: "))

        if valor > saldo:
            print("Operacao nao realizada! O saldo e insificiente!")
        elif valor > LIMITE_DO_SAQUE:
            print("Operacao nao realizada! O valor maximo por operacao exedido!")
        elif numero_de_saques >= LIMITE_DE_SAQUES:
            print("Operacao nao realizada! Limite de saques atingido!")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saques += 1
        else:
            print("Operacao nao realizada! O valor informado e invalido!")
    elif opcao == "e":
        print("#####Extrato#####")
        print("Nao ha operacoes!" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
    elif opcao == "q":
        break
    else:
        print("Opcao invalida! Tente novamente!")