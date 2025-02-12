class Conta:
    numero = "00000-0"
    saldo = 0.0 

    def deposito (self, valor):
        if (self.saldo > 0 ):
            self.saldo += valor 

    def saque (self,valor):
        if (self.saldo >+valor):   
            self.saldo -= valor    
        else:
             print ("saldo insulficiente!" )

if __name__ == '__main__':
    conta = Conta()
    conta.saldo = 20
    conta.numero = "13131-2"
    conta.deposito (10)
    conta.saque(50)
    print(conta.saldo)
    print(conta.numero)