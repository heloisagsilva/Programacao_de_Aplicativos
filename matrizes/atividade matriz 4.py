# Função para ler os tempos dos pilotos
def ler_tempos():
    tempos = []  # Lista que armazenará os tempos dos pilotos

    for i in range(4):  # Para cada piloto (4 pilotos)
        print(f"\nDigite os tempos do Piloto {i + 1}:")
        piloto_tempos = []  # Lista para armazenar os tempos de um piloto
        
        for j in range(4):  # Para cada volta (4 voltas)
            tempo = float(input(f"Volta {j + 1}: "))  # Lê o tempo da volta
            piloto_tempos.append(tempo)  # Adiciona o tempo na lista do piloto
        
        tempos.append(piloto_tempos)  # Adiciona os tempos do piloto na lista de tempos
    
    return tempos

# Função para exibir os tempos dos pilotos
def exibir_tempos(tempos):
    print("\nTempos dos Pilotos:")
    for i in range(4):
        print(f"Piloto {i + 1}: {tempos[i]}")  # Exibe os tempos de cada piloto

# Função para calcular o tempo total de cada piloto
def calcular_tempos_totais(tempos):
    print("\nTempos Totais dos Pilotos:")
    for i in range(4):
        tempo_total = sum(tempos[i])  # Soma os tempos das 4 voltas
        print(f"Piloto {i + 1}: {tempo_total:.2f} segundos")  # Exibe o tempo total com 2 casas decimais

# Função principal
def main():
    tempos = ler_tempos()  # Lê os tempos dos pilotos
    exibir_tempos(tempos)  # Exibe os tempos individuais
    calcular_tempos_totais(tempos)  # Calcula e exibe os tempos totais

# Inicia o programa
main()
