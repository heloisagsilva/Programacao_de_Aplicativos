n = int(input("Digite um número inteiro positivo:"))
numero = 2 
divisores = 0 #divisores é a variável contadora 

while (numero <= n-1):
    if (n % numero == 0 ): #se n é divisível por número 
        divisores = divisores + 1
    numero = numero + 1

if (divisores == 0):
    print("é primo")
else: 
    print("não é primo")