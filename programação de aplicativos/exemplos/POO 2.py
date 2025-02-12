class Conta: 
    numero = "00000-0"
    saldo = 0.0

    def __init(self, numero , saldoInicial):
        self.numero = numero 
        self. saldo = saldoInicial 

conta = Conta ("12345-1", 0)
print(conta.numero)
print(conta.saldo)