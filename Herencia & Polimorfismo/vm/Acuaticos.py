from Domain.Animal import Animal

class Acuaticos(Animal):
    def __init__(self, especie, dieta, edad, apodo):
        super().__init__(especie, edad, dieta)
        self.apodo = apodo

    def comunicarse(self):
        print(f"El {self.especie}, también llamado {self.apodo}, está haciendo burbujas.")

    def caminar(self):
        print(f"{self.apodo} se traslada por aletas.")

    def comer(self):
        self.alimentarse()
        print(f"El acuático es {self.dieta}, por lo que digiere carne, plantas o ambos.")