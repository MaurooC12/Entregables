# Author: Andrés Mauricio Cepeda Villanueva
# Homework: Implementar una clase de perro, cuyos métodos serían poder acariciar, sacar a pasear o dar de comer al perro y este será feliz.

class Perro:
    def __init__(self, nombrePerro, razaPerro):
        self.nombrePerro = nombrePerro
        self.razaPerro = razaPerro
        self.rascado = False
        self.alimentado = False
        self.paseado = False

    def Ladrar(self):
        print(f"{self.nombrePerro} es un perro de raza {self.razaPerro} y ¡Está ladrando! ")

    def rascar(self):
        self.rascado = True
        print(f"Le has rascado la panza a {self.nombrePerro}.")

    def darComer(self):
        self.alimentado = True
        print(f"Has dado de comer a {self.nombrePerro}.")

    def sacarPasear(self):
        self.paseado = True
        print(f"Has sacado a pasear a {self.nombrePerro}.")

    def estaFeliz(self):
        if self.rascado or self.alimentado or self.paseado:
            print(f"{self.nombrePerro} está feliz! :)")
        
opcionClase = input("BIENVENIDO - Por favor ingrese una de las dos opciones:\n 1 - Perro\n 2 - Salir\nOPCIÓN: ")
match opcionClase:
    case "1":
        nombrePerro = input("Por favor ingrese el nombre del perro: ")
        razaPerro = input("Por favor ingrese la raza del perro: ")
        accionPerro = Perro(nombrePerro, razaPerro)
        accionPerro.Ladrar()
        opcionPerroClase = input(f"¿Deseas realizar alguna acción con {nombrePerro}?\n 1. Rascar la panza\n 2. Dar de comer\n 3. Sacar a pasear\n 4. Ninguna\n OPCIÓN: ")
        match opcionPerroClase:
            case "1":
                miPerro = Perro(nombrePerro, any)
                miPerro.rascar()
                miPerro.estaFeliz()
            case "2":
                miPerro = Perro(nombrePerro, any)
                miPerro.darComer()
                miPerro.estaFeliz()
            case "3":
                miPerro = Perro(nombrePerro, any)
                miPerro.sacarPasear()
                miPerro.estaFeliz()
            case "4":
                exit
    case "2":
        exit