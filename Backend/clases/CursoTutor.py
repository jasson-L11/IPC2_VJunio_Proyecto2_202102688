from clases.Curso import Curso
from listas.Actividades import Actividades
from clases.Horario import Horario
class CursoTutor(Curso):
    def __init__(self, nombre, codigo):
        super().__init__(nombre, codigo)
        self.actividades =  Actividades # Lista de actividades del curso
        self.horario = Horario()