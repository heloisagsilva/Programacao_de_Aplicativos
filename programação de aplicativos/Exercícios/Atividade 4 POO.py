string = input("Digite um texto:") 
inversa = ""

stringlower = string.lower()
pontuacao = [".",",",":",";","!","?"]

for p in pontuacao:
    stringlower = stringlower.replace(p, "")

for x in stringlower:
       inversa = x + inversa 
print(inversa)

if stringlower == inversa:
        print("É palíndromo")
    
else:
        print("Não é palíndromo")


