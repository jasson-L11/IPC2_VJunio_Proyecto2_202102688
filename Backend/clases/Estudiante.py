from listas.CursosEstudiante import CursosEstudiante

class Estudiante:
    def __init__(self, nombre, carnet, password):
        self.nombre = nombre
        self.carnet = carnet
        self.password = password
        self.cursos = CursosEstudiante()  # Lista de cursos en los que el estudiante está inscrito
