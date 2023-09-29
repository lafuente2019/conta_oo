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

    def depositar_debido_limite(self, valor):
        self.saldo += valor    

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print(f"Saldo insuficiente, seu saldo é {self.saldo}")    
    
    def sacar_limite(self, valor):
        if self.limite >= valor:
            self.limite -= valor
        else:
            print("Saldo do limite insuficiente")
    
    def cancelar_limite(self): 
        if self.limite < 1000:
            valor = self.limite
            valor -= 1000
            print("Para cancelar o limite primeiro vc precisa quitar seu debito")
            print(f"Seu debito atual é: {valor}")
        else:
            self.limite = 0
            print("Cheque especial cancelado.")    

    def excluir_conta(self):
        if self.saldo > 0:
            print("Para cancelar sua conta primeira saque todos os valores de sua conta")
            print(f"Saldo em conta: {self.saldo}")
        else:
            self.numero = 0
            self.titular = 0
            self.saldo = 0
            self.limite = 0
            print("Sua conta foi excluida com sucesso")

        

