from Domain.Animal import Animal

class Acuaticos(Animal):
    def __init__(self, especie, dieta, edad, apodo):
        super().__init__(especie=especie, edad=edad, dieta=dieta)
        self.apodo = apodo

    def comunicarse(self):
        print(f"El {self.especie}, también llamado {self.apodo}, está haciendo burbujas.")

    def caminar(self):
        print(f"{self.apodo} se traslada por aletas.")

    def comer(self):
        print(f"El {self.especie} {self.apodo} está comiendo...")
        self.alimentarse()