saldo_inicial= 1000
saldo = saldo_inicial
limite = 500
agencia = "0001"
ultimo_numero_conta = 1
extrato =""
messagem=""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas= []
status=False
messagem += "messagem:".center(26)+"\n"
messagem += "--------------------------"
def menu():
    menu ="""
 --------Menu--------
 1 - Sacar
 2 - Depositar
 3 - Extrato
 4 - Novo usuário
 5 - Nova conta
 6 - Lista usuário
 7 - Lista conta
 8 - Sair
---------------------
"""
    return menu
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato+= f"Deposito de: R${valor:.2f}\n".replace(".",",")
    else:
        print("Opelração falhou")
    return saldo, extrato
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor < 0:
            print(messagem)
            print("Digite um valor inteiro e \npositivo.")
    elif valor > saldo:
            print(messagem)
            print("Saldo insuficiente".center(26))
    elif valor > limite:
            print(messagem)
            print("O valor passa do limite de \nsaque por operação, limite\n por saque é 500 reais.")
    elif numero_saques == LIMITE_SAQUES:
            print(messagem)
            print("Número de saque excedido \npor dia.".center(26))
    else:
        saldo = saldo - valor
        numero_saques = numero_saques+1
        extrato += f"saque de:    R${valor:.2f}\n".replace(".",",")
        print("Saque realizado com sucesso.")
    return saldo, extrato, numero_saques
def extratos(saldo, /, *, extrato):
    print(f"Saldo anterior R${saldo_inicial:.2f}")
    print("Extrato do dia".center(24))
    print("------------------------")
    print(extrato)
    if not extrato:
        print("sem movimentação no dia")
        print(extrato)
    print("------------------------")
    print(f"Saldo atual:  R${saldo:.2f}".center(20)) 
def filtrar_usuario(cpf, usuarios):
     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
     return usuarios_filtrados[0] if usuarios_filtrados else None
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números)")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Já existe usuário com esse CPF")
        return
    nome = input("Informe seu nome completo")
    data_nascimento = input("informe a data de nascimento (dd-mm-aaaa):")
    lagadouro = input("informe o lagadouro")
    numero = input("informe o número da casa")
    bairro = input("informe o bairro")
    cidade = input("informe a cidade")
    sigla = input("informe o estado")
    endereco = f"{lagadouro}, {numero} - {bairro} - {cidade}/{sigla}"
    print(endereco)
    usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco":endereco})
    print("usuario criado com sucesso")
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("informe o Cpf do usuário")
    usuario = filtrar_usuario(cpf,usuarios)
    if usuario:
        print("Conta criada com sucesso")
        status = True
        return contas.append({"agencia":agencia, "numero_conta": numero_conta, "usuario": usuario}) , status
    print("usuario não enoontrado")
def lista_contas(contas):
    linha = f"agência".center(10)+"Conta".center(10)+"Titular".center(30)+"\n"
    print(linha)
    for conta in contas:
        linha = f"{conta['agencia']}".center(10)
        linha += f"{conta['numero_conta']}".center(10)
        linha += f"{conta['usuario']['nome']}"
        
        print(linha)
def lista_usuarios(usuarios):
    linha = f"CPF".center(12)+"Nome".center(30)+"Data nascimento".center(18)+"Endereço"+"\n"
    print(linha)
    for usuario in usuarios:
        linha = f"{usuario['cpf']}".center(12)
        linha += f"{usuario['nome']}".center(30)
        linha += f"{usuario['data_nascimento']}".center(18)
        linha += f"{usuario['endereco']}"
        print(linha)

while True:
    opcao = input(menu())
    if opcao == "1":
        valor = int(input("Digite o valor de saque"))
        saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques,limite_saques=LIMITE_SAQUES)
    elif opcao == "2" :
        valor = int(input("Digite o valor do deposito"))
        saldo, extrato =depositar(saldo, valor, extrato)
    elif opcao == "3":
       extratos(saldo, extrato=extrato)
    elif opcao == "4":
        criar_usuario(usuarios)
    elif opcao == "5":
        status = criar_conta(agencia,ultimo_numero_conta, usuarios)
        if status:
            ultimo_numero_conta+=1
            status = False
    elif opcao == "6":
        lista_usuarios(usuarios)
    elif opcao == "7":
        lista_contas(contas)
    elif opcao == "8":
         break
    else:
        print(messagem)
        print("Digite uma opção valida.".center(26))