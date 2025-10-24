class Animal:
    def __init__(self, especie, edad, dieta):
        self._especie = especie
        self.edad = edad
        self._dieta = None
        self._asignar_dieta(dieta)

    @property
    def especie(self):
        return self._especie

    @property
    def dieta(self):
        return self._dieta

    def comunicarse(self):
        pass  # Método genérico

    def moverse(self):
        print("Animal moviéndose...")

    def alimentarse(self):
        if self._dieta == "Carnívoro":
            print(f"Por ser {self._dieta}, su alimentación se basa en carne")
        elif self._dieta == "Herbívoro":
            print(f"Por ser {self._dieta}, su alimentación se basa en plantas")
        elif self._dieta == "Omnívoro":
            print(f"Por ser {self._dieta}, su alimentación incluye tanto plantas como carne")
        else:
            print("Dieta desconocida")

    def _reproducirse(self):
        print("El animal se reproduce.")

    def _asignar_dieta(self, comida):
        comida = str(comida).lower().strip()
        if comida in ["carnívoro", "carnivoro", "carne"]:
            self._dieta = "Carnívoro"
        elif comida in ["herbívoro", "herbivoro", "plantas"]:
            self._dieta = "Herbívoro"
        elif comida in ["omnívoro", "omnivoro", "ambos"]:
            self._dieta = "Omnívoro"
        else:
            self._dieta = "Desconocida"
        print(f"DEBUG: Dieta asignada: {self._dieta} (entrada: {comida})")

    def _cambiardieta(self, nueva_dieta):
        self._asignar_dieta(nueva_dieta)
        print(f"La dieta ha sido actualizada a: {self._dieta}")

    def _agregar_especie(self, especie):
        self._especie = especie
        print(f"El animal es de especie: {especie}")