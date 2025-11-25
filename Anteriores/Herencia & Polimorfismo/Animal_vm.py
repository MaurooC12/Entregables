from Domain.Animal import Animal
from Observable import Observable

class AnimalViewModel:
    def __init__(self, vm: Animal):
        self.vm = vm
        self.vm.especie = Observable(vm.especie)
        self.vm.edad = Observable(vm.edad)
        self.error = Observable(None)
        self.mensaje = Observable(None)

    def especie(self, espe):
        try:
            self.error.value = None
            self.vm._agregar_especie(espe)
        except Exception as exc:
            self.error.value = str(exc)

    def edad(self, edad):
        try:
            self.error.value = None
            self.vm.edad.value = edad
        except Exception as exc:
            self.error.value = str(exc)