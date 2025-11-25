import sys
import os

# Añadir la carpeta raíz del proyecto a sys.path para permitir imports de paquetes hermanos
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from vm.Terrestres import Terrestres
from vm.Acuaticos import Acuaticos
from vm.Aereos import Aereos

def crear_animal():
    print("\n¿Qué tipo de animal deseas crear?")
    print("1. Terrestre")
    print("2. Acuático")
    print("3. Aéreo")
    tipo = input("Selecciona una opción (1-3): ")

    especie = input("Especie: ")
    dieta = input("Dieta (carnívoro/carne, herbívoro/plantas, omnívoro/ambos): ")
    edad = int(input("Edad: "))
    apodo = input("Apodo: ")

    if tipo == "1":
        return Terrestres(especie, dieta, edad, apodo)
    elif tipo == "2":
        return Acuaticos(especie, dieta, edad, apodo)
    elif tipo == "3":
        return Aereos(especie, dieta, edad, apodo)
    else:
        print("Opción no válida.")
        return None

def mostrar_acciones(animal):
    print("\n¿Qué deseas que haga el animal?")
    print("1. Comunicarse")
    print("2. Caminar")
    print("3. Comer")
    print("4. Mostrar todo")
    opcion = input("Selecciona una opción (1-4): ")

    if opcion == "1":
        animal.comunicarse()
    elif opcion == "2":
        animal.caminar()
    elif opcion == "3":
        animal.comer()
    elif opcion == "4":
        animal.comunicarse()
        animal.caminar()
        animal.comer()
    else:
        print("Opción no válida.")

def main():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Crear nuevo animal")
        print("2. Salir")
        seleccion = input("Selecciona una opción: ")

        if seleccion == "1":
            animal = crear_animal()
            if animal:
                mostrar_acciones(animal)
        elif seleccion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()