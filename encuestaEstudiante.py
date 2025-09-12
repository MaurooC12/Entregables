# Author: Mauricio Cepeda Villanueva
# Encuesta Proyecto python, donde se entrevistará a un total de 10 estudiantes para recopilar ideas sobre los proyectos que se pueden realizar. 

class Encuesta:
    def agregarRespuesta(self, respuesta):
        self.respuestas.append(respuesta)

    def mostrarResultados(self, estudiantes):
        print("\nRESULTADOS:")
        for estudiante, respuesta in zip(estudiantes, self.respuestas):
            print(f"{estudiante.nombreEstudiante} de {estudiante.carreraEstudiante}")
            for preg, resp in zip(self.preguntas, respuesta):
                print(f"  {preg}: {resp}")  
            print()
        print("------------------------------------------------")
    def __init__(self, preguntas):
        self.preguntas = preguntas  
        self.respuestas = []        
    
class Estudiante:
    def __init__(self, nombreEstudiante, carreraEstudiante, respuestaProyecto):
        self.nombreEstudiante = nombreEstudiante
        self.carreraEstudiante = carreraEstudiante
        self.respuestaProyecto = respuestaProyecto


if __name__ == "__main__":
    preguntas = [
        "¿Qué tema es de su interés para el proyecto?",
        "¿Sabe trabajar en equipo?",
        "¿Tiene disponibilidad de tiempo?",
        "¿Qué nivel tiene en python? (1) Mucho, 2) Medio, 3) Bajo)",
        "Ingrese su número de celular para contactarlo más fácil: "
    ]
    encuesta = Encuesta(preguntas)
    print("IDEAS PROYECTO PYTHON")
    estudiantes = []
    while True:
        nombre = input("\tPor favor ingrese su nombre: ")
        carrera = input(f"\t{nombre} a qué carrera pertenece: ")
        respuestas = []
        for pregunta in preguntas:
            resp = input(f"  {pregunta} ")
            respuestas.append(resp)
        estudiante = Estudiante(nombre, carrera, respuestas)
        estudiantes.append(estudiante)
        encuesta.agregarRespuesta(respuestas)
        continuar = input("¿Desea añadir otro estudiante? 1. Sí  2. No: ")
        if continuar.strip() != "1":
            break
    encuesta.mostrarResultados(estudiantes)

