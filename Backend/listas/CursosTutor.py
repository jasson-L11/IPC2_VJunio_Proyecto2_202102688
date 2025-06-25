from clases.CursoTutor import CursoTutor

class CursosTutor:
    def __init__(self):
        self.cursos = []

    def agregar_curso(self, nombre, codigo):
        nuevo_curso = CursoTutor(nombre, codigo)
        self.cursos.append(nuevo_curso)

    def __len__(self):
        return len(self.cursos)