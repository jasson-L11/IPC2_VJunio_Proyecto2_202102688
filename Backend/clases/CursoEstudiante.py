from clases.Curso import Curso


class CursoEstudiante(Curso):
    def __init__(self, nombre, codigo):
        super().__init__(nombre, codigo)
