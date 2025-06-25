from listas.CursosTutor import CursosTutor

class Tutor: 
    def __init__(self, id_tutor, nombre, password):
        self.id_tutor = id_tutor
        self.nombre = nombre
        self.password = password
        self.cursos = CursosTutor()  # Lista de cursos al que el tutor está asignado