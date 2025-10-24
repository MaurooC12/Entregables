from Domain.Animal import Animal

class Aereos(Animal):
    def __init__(self, especie, dieta, edad, apodo):
        super().__init__(especie=especie, edad=edad, dieta=dieta)
        self.apodo = apodo

    def comunicarse(self):
        print(f"El {self.especie}, también llamado {self.apodo}, está diciendo hola.")

    def caminar(self):
        print(f"{self.apodo} se traslada por alas.")

    def comer(self):
        print(f"El {self.especie} {self.apodo} está comiendo...")
        self.alimentarse()