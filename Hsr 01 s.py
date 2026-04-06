class motos:
    def __init__(self, nome, cilindrada):
        self.nome = nome
        self.cilindrada = cilindrada

    def apresentar(self):
        print(f"O modelo {self.nome} tem cilindrada {self.cilindrada}.")

# criando objeto
p1 = motos("CG 160", 14.7)

# chamando método
p1.apresentar()
