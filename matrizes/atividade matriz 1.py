# Função para ler a matriz
def leMatriz(dimensao):
    mat = [[] for i in range(dimensao)]  # Cria uma lista de listas para a matriz

    for i in range(dimensao):  # Para cada linha
        for j in range(dimensao):  # Para cada coluna
            num = int(input("("+ str(i+1) +","+ str(j+1)+"): "))  # Lê o valor
            mat[i].append(num)  # Adiciona o número à linha
    return mat

# Função para imprimir a matriz
def imprimeMatriz(mat):
    for linha in mat:  # Para cada linha da matriz
        for numero in linha:  # Para cada número na linha
            print(numero, end=" ")  # Imprime o número na mesma linha
        print()  # Pula para a próxima linha

# Lê a dimensão da matriz
dimensao = int(input("Digite a dimensão da matriz: "))

# Lê a matriz
mat = leMatriz(dimensao)

# Contador de posições não nulas
nao_nulas = 0

# Conta as posições não nulas
for i in range(dimensao):
    for j in range(dimensao):
        if mat[i][j] != 0:  # Se o valor não for zero
            nao_nulas += 1  # Incrementa o contador

# Exibe o número de posições não nulas
print(f"O número de posições não nulas na matriz é: {nao_nulas}")
