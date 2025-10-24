from Domain.Animal import Animal

class Terrestres(Animal):
    def __init__(self, especie, dieta, edad, apodo):
        super().__init__(especie, edad, dieta)
        self.apodo = apodo

    def comunicarse(self):
        print(f"El {self.especie}, también llamado {self.apodo}, está diciendo hola.")

    def caminar(self):
        print(f"{self.apodo} se traslada por patas.")

    def comer(self):
        self.alimentarse()
        print(f"El terrestre es {self.dieta}, por lo que digiere carne, plantas o ambos.")