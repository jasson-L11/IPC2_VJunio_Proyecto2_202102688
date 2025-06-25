from clases.Estudiante import Estudiante

class Estudiantes:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, carnet, password):
        nuevo_estudiante = Estudiante(carnet, password)
        self.estudiantes.append(nuevo_estudiante)        