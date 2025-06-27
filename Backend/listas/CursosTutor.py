from clases.CursoTutor import CursoTutor

class CursosTutor:
    def __init__(self):
        self.cursos = []

    def agregar_curso(self, nombre, codigo):
        nuevo_curso = CursoTutor(nombre, codigo)
        self.cursos.append(nuevo_curso)

    def __len__(self):
        return len(self.cursos)
    
    def verificar_curso(self, codigo):
        for curso in self.cursos:
            if curso.codigo == codigo:
                return True
        return False
    
    def ingresar_hora(self, codigo, inicio, fin):
        for curso in self.cursos:
            if curso.codigo == codigo:
                curso.agregar_horario(inicio, fin)
                return