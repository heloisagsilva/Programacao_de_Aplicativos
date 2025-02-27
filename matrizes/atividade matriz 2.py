# Função para imprimir o tabuleiro formatado
def imprime_tabuleiro(tabuleiro):
    for linha in tabuleiro:  # Para cada linha do tabuleiro
        print(" | ".join(linha))  # Junta e imprime os valores da linha
        print("-" * 9)  # Imprime uma linha de separação

# Lista para armazenar o tabuleiro
tabuleiro = []

# Solicita os valores para o tabuleiro
print("Digite os valores para o tabuleiro (use 'X', 'O' ou ' ' para espaços vazios):")

# Preenche o tabuleiro
for i in range(3):  # Para cada linha
    linha = []  # Cria uma linha vazia
    for j in range(3):  # Para cada coluna
        valor = input(f"Posição ({i+1}, {j+1}): ").upper()  # Pede o valor para a posição
        while valor not in ['X', 'O', ' ']:  # Verifica se o valor é válido
            print("Valor inválido! Digite 'X', 'O' ou ' ' (espaço vazio).")
            valor = input(f"Posição ({i+1}, {j+1}): ").upper()  # Pede novamente se for inválido
        linha.append(valor)  # Adiciona o valor à linha
    tabuleiro.append(linha)  # Adiciona a linha ao tabuleiro

# Exibe o tabuleiro
print("\nTabuleiro:")
imprime_tabuleiro(tabuleiro)  # Chama a função para imprimir o tabuleiro
