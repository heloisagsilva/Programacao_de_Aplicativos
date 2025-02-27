class TV():
    def __init__(self, cor, tamanho): # "self" é quando o codigo olha pra si mesmo 
        self.cor = cor
        self.ligada = False
        self.tamanho = tamanho
        self.canal = "Netflix"
        self.volume = 10 
    
    def mudar_canal(self):
        self.canal = "Disney+"

tv_sala = TV(cor = "preta", tamanho = 55)
tv_quarto = TV("branca", 60)
tv_sala.mudar_canal()

print(tv_sala.cor)   #imprime netflix 
print(tv_sala.tamanho)
print(tv_quarto.cor)
print(tv_quarto.volume)
