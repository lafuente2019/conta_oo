class Conta:

    def __init__(self, numero, titular, saldo, limite):
        
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"O saldo da conta é {self.__saldo} para o titular {self.__titular}") 


    def depositar(self, valor):
        self.__saldo += valor

    def depositar_debido_limite(self, valor):
        self.__limite += valor    

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print(f"saldo insuficiente, seu saldo é {self.__saldo}")    
    
    def sacar_limite(self, valor):
        if self.__limite >= valor:
            self.__limite -= valor
        else:
            print("saldo do limite insuficiente")
    
    def cancelar_limite(self): 
        if self.__limite < 1000:
            valor = self.__limite
            valor -= 1000
            print("Para cancelar o limite primeiro vc precisa quitar seu debito")
            print(f"Seu debito atual é: {valor}")
        else:
            self.__limite = 0
            print("Cheque especial cancelado.")    

    def excluir_conta(self):
        if self.__saldo > 0:
            print("Para cancelar sua conta primeira saque todos os valores de sua conta")
            print(f"__saldo em conta: {self.__saldo}")
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

        

