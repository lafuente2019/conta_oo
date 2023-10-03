class Conta:

    def __init__(self, numero, titular, saldo, limite):
        
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    @property
    def saldo(self):
        return self.__saldo
    @property
    def numero(self):
        return self.__numero
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    
    @property
    def titular(self):
        return self.__titutlar
    
    def extrato(self):
        print(f"O saldo da conta é {self.__saldo} para o titular {self.__titular}") 

    def depositar(self, valor):
        self.__saldo += valor

    def depositar_debido_limite(self, valor):
        self.__limite += valor    

    def sacar(self, valor):
        if (valor <= (self.__saldo + self.__limite)):
            self.__saldo -= valor
        else:
            print(f"saldo insuficiente, seu saldo é {self.__saldo + self.__limite}")    
    
    def excluir_conta(self):
        if self.__saldo > 0:
            print("Para cancelar sua conta primeira saque todos os valores de sua conta")
            print(f"Seu saldo em conta é: {self.__saldo}")
        else:
            self.__numero = 0
            self.__titular = 0
            self.__saldo = 0
            self.__limite = 0
            print("Sua conta foi excluida com sucesso")

    def transferencia(self, valor, destino):
         if self.__saldo >= valor:
            self.sacar(valor)   
            destino.depositar( valor)
            print("Tranferência realizada com sucesso")
         else:
             print(f"Saldo insuficiente, o saldo da sua conta é: {self.__saldo}")     
    
    @staticmethod
    def codigo_banco():
        return "001"    

