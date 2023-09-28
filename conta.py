class Conta:

    def __init__(self, numero, titular, saldo, limite):
        
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f"O saldo da conta é {self.saldo} para o titular {self.titular}") 

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def aumentar_limite(self, valor):
        self.limite += valor

    def diminuir_limite(self, valor):
        self.limite -= valor

    def cancelar_limite(self):
        self.limite = 0       

    def excluir_conta(self):
        self.numero = None
        self.titular = None
        self.saldo = None
        self.limite = None
        print("Sua conta foi excluida com sucesso")

        

