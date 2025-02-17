def leNumeroInt():
    numero = input("Digite um número inteiro: ")
    return int(numero)

def positivo (numero):
    if (numero + numero >= 1):
        print ("é positivo")

def negativo (numero):
    if (numero + numero <= -1):
        print ("é negativo")

def zero (numero):
    if (numero + numero == 0):
        print ("é zero")
    return numero 

numero = int(input("Digite um numero:"))

positivo(numero)
negativo(numero)
zero(numero)
