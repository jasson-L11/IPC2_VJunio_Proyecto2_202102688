from clases.Curso import Curso
from listas.Actividades import Actividades
from clases.Horario import Horario
class CursoTutor(Curso):
    def __init__(self, nombre, codigo):
        super().__init__(nombre, codigo)
        self.actividades =  Actividades # Lista de actividades del curso
        self.horario = Horario()


    def agregar_horario(self, hora_inicio, hora_fin):
        self.horario.inicio = hora_inicio
        self.horario.final = hora_fin

    def to_dict_horario(self):
        return {
            f'{self.codigo}-{self.nombre}': f'{self.horario.inicio} - {self.horario.final}'
                }