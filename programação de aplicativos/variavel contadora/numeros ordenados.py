n = int (input("uma quantidade de números para ser analisada:"))
print("informe um numero:")
anterior = int(input())

i = 1 #leu um número
ordenado = 0 #ordenado é a variável contadora 

while (i < n) and (ordenado == 0):
    print("informe o número")
    atual = int(input())
    i = i + 1 #leu mais um número 
    if (atual <=anterior):
        ordenado = ordenado + 1
    anterior = atual 

if (ordenado == 0):
    print("sequência ordenada")
else:
    print("sequência não ordenada")