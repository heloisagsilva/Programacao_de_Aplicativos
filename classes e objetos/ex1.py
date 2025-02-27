class TV():
    def __init__(self): # "self" é quando o codigo olha pra si mesmo 
        self.cor = "preta"
        self.ligada = False
        self.tamanho = 55
        self.canal = "Netflix"
        self.volume = 10 
    

tv_sala = TV()
tv_quarto = TV()

print(tv_quarto.canal) #imprime netflix 
print(tv_sala.canal)   #imprime netflix 
print(tv_sala.cor)
print(tv_sala.tamanho)
print(tv_sala.volume)
