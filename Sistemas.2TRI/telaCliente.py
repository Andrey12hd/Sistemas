import getpass
import csv
from conta import Conta

# INICIALIZAÇÃO DE VARIÁVEIS
contas = []
agencia = int(input("Digite a agência: "))
numero_conta = input("Digite sua conta corrente: ")
senha = getpass.getpass("Digite a senha: ")
contaEncontrada = None
acesso_liberado = False

def lerArquivo():
    with open('contas.csv', newline='', encoding='utf-8', errors='ignore') as lerContas:
        leitor = csv.reader(lerContas, delimiter=',')
        for linha in leitor:
            conta = Conta(int(linha[0]), linha[1], linha[2], float(linha[3]), linha[4])
            contas.append(conta)

def encontrarContaCorrente():
    global contaEncontrada
    for conta in contas:
        if numero_conta == conta.numero:
            contaEncontrada = conta  # Referência direta

def verificarAcesso():
    global acesso_liberado
    if contaEncontrada is None:
        print("Dados incorretos")
    else:
        if senha == contaEncontrada.senha and agencia == contaEncontrada.agencia:
            acesso_liberado = True
            print("Acesso liberado")
        else:
            print("Dados incorretos")

def procurarConta(numero):
    for conta in contas:
        if conta.numero == numero:
            return conta
    return None

def salvarArquivo():
    with open('contas.csv', 'w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo, delimiter=',')
        for conta in contas:
            escritor.writerow([conta.agencia, conta.numero, conta.titular, conta.saldo, conta.senha])

# Executar login
lerArquivo()
encontrarContaCorrente()
verificarAcesso()

# liberar o acesso ao menu de transações
if acesso_liberado:
    while True:
        print("\n--- MENU ---")
        print("1 - Extrato")
        print("2 - Saque")
        print("3 - Depósito")
        print("4 - Pix")
        print("0 - Sair")
        
        try:
            transacao = int(input("Digite a opção: "))
        except ValueError:
            print("Entrada inválida. Tente novamente.")
            continue

        if transacao == 1:
            print(f"O saldo da conta é R$ {contaEncontrada.extrato():.2f}")
        
        elif transacao == 2:
            valor = float(input("Digite o valor do saque: "))
            if contaEncontrada.sacar(valor):
                print("Saque efetuado com sucesso!")
                salvarArquivo()
            else:
                print("Saque negado. Consulte seu extrato!")
        
        elif transacao == 3:
            valor = float(input("Digite o valor do depósito: "))
            if contaEncontrada.deposito(valor):
                print(f"Depósito de R$ {valor:.2f} efetuado com sucesso!")
                salvarArquivo()
            else:
                print("Não foi possível realizar o depósito")
        
        elif transacao == 4:
            valor = float(input("Digite o valor do PIX: "))
            destino_numero = input("Digite o número da conta de destino: ")
            contaDestino = procurarConta(destino_numero)
            if contaDestino:
                if contaEncontrada.sacar(valor):
                    contaDestino.deposito(valor)
                    print(f"PIX de R$ {valor:.2f} enviado com sucesso para {contaDestino.titular}")
                    salvarArquivo()
                else:
                    print("Saldo insuficiente para o PIX.")
            else:
                print("Conta de destino não encontrada.")
        
        elif transacao == 0:
            print("Saindo do sistema. Até logo!")
            break
        
        else:
            print("Opção inválida.")
