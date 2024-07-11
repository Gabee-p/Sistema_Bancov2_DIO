import textwrap

def menu():
    menu = '''

    --------------------------------------------------------

    Bem vindo ao banco SP, escolha uma opção do menu abaixo:

    ====== MENU ======

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo usuário5
    [5] Nova conta
    [6] Listar contas
    [7] Sair

    ==================

    >> '''

    return input(menu)



def Depositar(saldo, valor, extrato, /):  
    if valor > 0:
        saldo += valor
        extrato += f"Depósito realizado: R$ {valor:.2f}. \n"
        print("\n>> Operação realizada com sucesso.")      
    else:
        print("\n>> ERRO: Valor inválido.\n")
    
    return saldo, extrato

def Sacar(*, saldo, vsaque, extrato, numero_saques, limite):
    if vsaque > limite:
        print("\n>> ERRO: Valor excede o limite de saque autorizado.")
    elif vsaque > saldo:
        print("\n>> ERRO: Saldo insuficiente.")
    elif vsaque <= 0:
        print("\n>> ERRO: Valor inválido.")
    else:
        saldo -= vsaque
        print("\n>> Operação realizada com sucesso.")
        numero_saques += 1
        extrato += (f"Saque realizado:    R$ {vsaque:.2f}. \n")  

    return saldo, extrato, numero_saques

def Exibir_extrato(saldo, extrato):
    if extrato == (""):
        print("\n>> Não foram realizadas movimentações.")
        print(f">> Saldo: R$ {saldo:.2f}.")

    else:
        print(extrato)
        print("\n                ***                          \n")
        print (f">> Saldo: R$ {saldo:.2f}.")

def Criar_usuario(usuarios):
    cpf = input("\nInforme o CPF - somente números: ")
    usuario = Filtrar_usuario(cpf,usuarios)

    if usuario:
        print("\n ERRO: Esse CPF já possui um usuário.")
        return
    
    nome = input("Informe o nome completo: ")
    data_nasc = input ("Informe a data de nascimento (dd-mm-aaaa): ")
    telefone = input("Informe o telefone: ")

    usuarios.append({"nome":nome, "data_nasc":data_nasc, "cpf":cpf, "telefone":telefone})
    
    print ("\n=== Usuário criado com sucesso! ===")

def Filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def Criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário - somente números: ")
    usuario = Filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n === Conta criada com sucesso ! ===")
        return {"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario}
    
    print("\n ERRO: Usuário não encontrado, fluxo de criação de conta encerrado!")

def Listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
    print("=" *70)
    print(textwrap.dedent(linha))

def main():
    
    AGENCIA = "0001"

    valor = 0.00
    saldo  = 0.00
    limite = 500.00
    vsaque = 0.00
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            print("\n--------------------------------------------------------")
            print("Depósito:\n")
            valor = float(input("Insira o valor desejado: R$  "))
            saldo, extrato = Depositar(saldo, valor, extrato)

        elif opcao == "2":
            print("\n--------------------------------------------------------")
            print("Saque:\n")

            if numero_saques >= 3:
                print("\n>> Você excedeu o limite de saques diários!")
            
            else:
                vsaque = float(input("Insira o valor para saque: R$  "))
                saldo, extrato, numero_saques = Sacar(vsaque = vsaque, saldo = saldo, extrato = extrato, numero_saques = numero_saques, limite = limite)

        elif opcao == "3":
            print("\n--------------------------------------------------------")
            print("Extrato:\n")

            Exibir_extrato(saldo, extrato)
        
        elif opcao == "4":
            Criar_usuario(usuarios)
        
        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = Criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            Listar_contas(contas)

        elif opcao == "7":
            break

        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")

    print("\nO banco SP agradece sua visita, volte sempre!\n")
    print ("---------------------------------------")

main()
