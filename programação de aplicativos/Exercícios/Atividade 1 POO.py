class Pessoa:
    nome = ""
    idade = 0
    peso = 0
    altura = 0
    def envelhecer (self, ano):
        self.idade  += ano 

    def engordar (self, kg):
        self.peso += kg

    def emagrecer (self, kg):
        self.peso -= kg

    def crescer (self, cm):
        if (self.idade <21):
            self.altura += (0.05*cm)

if __name__ == '__main__':     
    pessoa = Pessoa()
    pessoa.nome = "larão"
    pessoa.idade = 10
    pessoa.peso = 40
    pessoa.altura = 1.55 

    print("Nome:", pessoa.nome, "Idade:", pessoa.idade, "Peso:", pessoa.peso,  "Altura:", pessoa.altura)
    pessoa.envelhecer(5)
    pessoa.engordar(6)
    pessoa.crescer(5)
    print("Nome:", pessoa.nome, "Idade:", pessoa.idade, "Peso:", pessoa.peso,  "Altura:", pessoa.altura)
    pessoa.emagrecer(4)
    print("Nome:", pessoa.nome, "Idade:", pessoa.idade, "Peso:", pessoa.peso,  "Altura:", pessoa.altura)