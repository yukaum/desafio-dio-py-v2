def menu():
    menu = """
------------------ MENU ------------------
    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    
    [n] Novo Usuario
    [c] Nova Conta Corrente

    [q] Sair

    =>"""
    return input(menu)


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print("\n>>> Erro ao processar a operação. Limite de saques excedido.")

    elif valor > limite:
        print("\n>>> Erro ao processar a operação. Valor de saque excede o limite.")

    elif valor > saldo:
        print("\n >>> Erro ao processar a operação. Não há saldo suficiente.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f} \n"
        numero_saques += 1
        print("\n >>> Operação realizada com sucesso!")
        
    else:
        print("\n>>> Erro ao processar a operação. Valor de saque inválido.")

    return saldo, extrato, numero_saques


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f} \n"
        print("\n>>> Operação realizada com sucesso!")
    else:
        print("\n>>> Erro ao processar a operação. Valor de depósito inválido.")

    return saldo, extrato


def imprimir_extrato(saldo, /, *, extrato):
    print("================= EXTRATO =================")

    if extrato == "":
        print("\n >>> Não foram realizadas movimentações. \n\n=================")

    else:
        print(extrato)
        print("===========================================")
        print(f"Saldo: R$ {saldo:.2f}")
        print("===========================================")


def criar_usuario(clientes):
    cpf = int(input("Informe CFP (apenas números): "))
    
    for cliente in clientes:
        if cpf == cliente["cpf"]:
            print("\n>>> Usuário já cadastrado!")
            return

    nome = input("Nome Completo: ").strip()
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ").strip()
    endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})

    print("\n>>> Cliente cadastrado com sucesso.")
    
    return clientes


def criar_conta_corrente(contas, clientes, agencia, numero_conta):
    cpf = int(input("Informe CFP (apenas números): "))
    
    for cliente in clientes:
        if cpf == cliente["cpf"]:
            contas.append({"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente})
            numero_conta += 1
            print("\n>>> Conta criada com sucesso.")
            return
        
    print("\n>>> Cliente não encontrado.")
        
           
def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    clientes = []
    contas = []
    AGENCIA = "0001"
    numero_conta = 1

    while True:

        opcao = menu()

        if opcao == "d":
            deposito = float(input("Insira o valor do depósito: "))
            saldo, extrato = depositar(saldo, deposito, extrato)

        elif opcao == "s":
            saque = float(input("Insira o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            imprimir_extrato(saldo, extrato=extrato)

        elif opcao == "n":
            criar_usuario(clientes)
            
        elif opcao == "c":
            criar_conta_corrente(contas, clientes, AGENCIA, numero_conta)
              
        elif opcao == "q":
            break

        else:
            print(
                "\n>>> Operação inválida, por favor selecione novamente a operação desejada."
            )


main()
