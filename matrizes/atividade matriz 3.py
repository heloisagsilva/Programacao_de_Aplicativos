# Inicializa o vetor que representa as 50 poltronas, todas inicialmente disponíveis (0)
poltronas = [0] * 50

# Função para exibir o status das poltronas (0 - disponível, 1 - vendida)
def exibir_poltronas():
    print("Status das Poltronas:")
    for i in range(50):
        status = "Disponível" if poltronas[i] == 0 else "Vendida"
        print(f"Poltrona {i+1}: {status}")

# Função para realizar a venda de uma passagem
def vender_passagem():
    exibir_poltronas()
    poltrona = int(input("Digite o número da poltrona para venda (1 a 50): ")) - 1  # Ajuste para índice 0
    if poltrona < 0 or poltrona >= 50:
        print("Número de poltrona inválido! Digite um número entre 1 e 50.")
        return
    
    # Verifica se a poltrona já está ocupada
    if poltronas[poltrona] == 1:
        print(f"A poltrona {poltrona+1} já foi vendida. Escolha outra poltrona.")
    else:
        # Marca a poltrona como vendida
        poltronas[poltrona] = 1
        print(f"Passagem vendida com sucesso para a poltrona {poltrona+1}!")

# Função principal
def main():
    while True:
        print("\n1 - Vender passagem")
        print("2 - Exibir status das poltronas")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            vender_passagem()
        elif opcao == "2":
            exibir_poltronas()
        elif opcao == "3":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Inicia o programa
main()
