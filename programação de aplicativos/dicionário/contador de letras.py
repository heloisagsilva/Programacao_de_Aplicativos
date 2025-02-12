texto = input("Digite um texto:")
contar = {}
for letra in texto:
    if letra in contar:
        contar[letra] = 1
    else:
        contar[letra] = 1

letramais = ''
for key in contar:
    if not letramais or contar [key] > contar[letramais]:
        letramais = key
        print (letramais)
