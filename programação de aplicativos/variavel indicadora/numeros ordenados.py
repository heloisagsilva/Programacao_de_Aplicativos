n = int(input("Digite uma quantidade de números para ser analisados:"))
print("Informe um número:")
anterior = int(input())

i = 1 #leu um número 
ordenado = True 

while (i < n ) and (ordenado):
    print("informe um número:")
    atual = int (input ())
    i = i + 1 #leu mais um número 
    if (atual < anterior):
        ordenado = False 
    anterior = atual 
if (ordenado):
    print("sequência ordenada")
else:
    print("sequência não ordenada")