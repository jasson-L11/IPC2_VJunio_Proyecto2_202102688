from clases.Curso import Curso

class Cursos:
    def __init__(self):
        self.cursos = []

    def agregar_curso(self, nombre, codigo):
        nuevo_curso = Curso(nombre, codigo)
        self.cursos.append(nuevo_curso)

    def print_cursos(self):
        for curso in self.cursos:
            print(curso.__str__())