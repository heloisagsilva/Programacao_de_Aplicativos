n = int (input ("Digite uma quantidade de números para ser analisada:"))
print("Informe um número:")
anterior = int(input())

ordenado = True #ordenado é a variável indicadora 

for i in range (n-1):
    print("informe um número:")
    atual = int (input ())
    if atual < anterior:
        ordenado = False 
        break
    anterior = atual 
    
if (ordenado):
    print("sequência ordenada")
else:
    print("sequência não ordenada")