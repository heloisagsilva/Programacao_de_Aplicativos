texto = input("Digite um texto:")
pontuacao = [".",",",":",";","!","?"]

# remove os sinais de pontuação 
for p in pontuacao:
    texto = texto.replace(p," ")

    # split devolve lista com palavras como itens 
    numero_palavras = len(texto) #se tirarmos o ".split()" o programa contará as letras 
    print("numeros de palavras:", numero_palavras)