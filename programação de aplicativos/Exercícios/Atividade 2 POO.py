def adjacente_iguais(numero):
    numero_str = str(numero)
    for i in range (len(numero_str) - 1):
        if numero_str[1] == numero_str[i + 1]:
            return True 
        return False 
    
i = 0

while( i < 3):
 
    numero = int(input("Digite um número inteiro:"))

    if adjacente_iguais(numero):
        print("Os números digitados são adjacentes!!")
    else:
        print("Os números digitados não são adjacentes!!")
    
    i = i + 1
    