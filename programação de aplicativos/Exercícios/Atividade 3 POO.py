import random

def jogo():
    opções = ['pedra', 'papel', 'tesoura']
    
    while True:
        
        print("Escolha:")
        print("0 - Pedra")
        print("1 - Papel")
        print("2 - Tesoura")
        
        try:
            jogador = int(input("Digite o número correspondente à sua escolha (0, 1 ou 2): "))
            
            if jogador < 0 or jogador > 2:
                print("Escolha inválida!")
                jogar_novamente = input("Você deseja tentar novamente? (Sim/Não): ").lower()
                if jogar_novamente == "não":
                    print("Obrigado por jogar!")
                    break 
                else:
                    continue  

            computador = random.randint(0, 2)
            print(f"Computador escolheu: {opções[computador]}")

            if jogador == computador:
                print("Empate!")
            elif (jogador == 0 and computador == 2) or \
                 (jogador == 1 and computador == 0) or \
                 (jogador == 2 and computador == 1):
                print("Você ganhou!")
            else:
                print("Você perdeu!")

            jogar_novamente = input("Deseja jogar novamente? (Sim/Não): ").lower()
            if jogar_novamente != 'sim':
                print("Obrigado por jogar!")
                break 
        
        except ValueError:
            print("Entrada inválida. Por favor, insira um número entre 0 e 2.")

jogo()
