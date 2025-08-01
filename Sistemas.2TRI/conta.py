class Conta:
    def __init__(self, agencia, numero, titular, saldo, senha):
        self.__agencia = agencia
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__senha = senha

    # Métodos de acesso
    @property
    def numero(self):
        return self.__numero

    @property
    def agencia(self):
        return self.__agencia

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, nova_senha):
        self.__senha = nova_senha

    # Métodos de operação
    def extrato(self):
        return self.__saldo

    def sacar(self, valor):
        if valor <= 0 or valor > self.__saldo:
            return False
        self.__saldo -= valor
        return True     

    def deposito(self, valor):
        if valor <= 0:
            return False
        self.__saldo += valor
        return True 

    def transferir(self, valor, conta_destino):
        if valor <= 0 or valor > self.__saldo:
            return False    
        self.__saldo -= valor
        conta_destino.deposito(valor)
        return True
