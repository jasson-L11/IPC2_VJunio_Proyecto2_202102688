from clases.Estudiante import Estudiante

class Estudiantes:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, nombre, carnet, password):
        nuevo_estudiante = Estudiante(nombre, carnet, password)
        self.estudiantes.append(nuevo_estudiante)


    def verificar_estudiante(self, carnet):
        for estudiante in self.estudiantes:
            if estudiante.carnet == carnet:
                return True
        return False

    def asignar_estudiante(self, carnet, codigo_curso, nombre_curso):
        for estudiante in self.estudiantes:
            if estudiante.carnet == carnet:
                estudiante.cursos.agregar_curso(nombre_curso, codigo_curso)