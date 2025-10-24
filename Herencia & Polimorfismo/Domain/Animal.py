class Animal:
    def __init__(self, especie, edad, dieta):
        self._especie = especie
        self.edad = edad
        self.dieta = dieta

    @property
    def especie(self):
        return self._especie

    def comunicarse(self):
        pass  # Método genérico

    def moverse(self):
        print("Animal moviéndose...")

    def alimentarse(self):
        print("El animal se alimenta según su dieta:", self.dieta)

    def _reproducirse(self):
        print("El animal se reproduce.")

    def _asignar_dieta(self, comida):
        comida = comida.lower()
        if comida == "carne":
            self.dieta = "Carnívoro"
        elif comida == "plantas":
            self.dieta = "Herbívoro"
        elif comida == "ambos":
            self.dieta = "Omnívoro"
        else:
            self.dieta = "Desconocida"

    def _cambiardieta(self, nueva_dieta):
        self._asignar_dieta(nueva_dieta)
        print(f"La dieta ha sido actualizada a: {self.dieta}")

    def _agregar_especie(self, especie):
        self._especie = especie
        print(f"El animal es de especie: {especie}")