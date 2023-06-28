menu = '''
[d] Deposita
[s] Sacar
[e] Extrato
[q] Sair

=>'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while  True:
    opcao = input(menu)

    if  opcao == "d":
        valor  = float(input("Quanto deseja epositar? \n"))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: {valor: .2f} \n"
        else:
            print("O valor do deposito eve ser positivo. \n")

    elif opcao == "s":
        valor = float(input("Quanto deseja sacar? \n"))
        if saldo >= valor:
            if ((valor <= limite) and (numero_saques < LIMITE_SAQUES)):
                saldo -= valor
                numero_saques += 1
                extrato  += f"Saque: R$ {valor: .2f} \n"
            elif valor > limite:
                print("O limite máximo parsaques é e R$ 500,00 \n")
            elif numero_saques >= LIMITE_SAQUES:
                print("Limite de 3 saques diários atingido.  \n")
        else:
            print("Seu saldo é insuficiente. \n")

    elif opcao == "e":
        print((f"""
Extrato:
{extrato}

Saldo:
R$ {saldo}
              """).strip())

    elif opcao == "q":
        break

    else:
        print("Opção inválida.")