from clases.Tutor import Tutor

class Tutores:
    def __init__(self):
        self.tutores = []

    def agregar_tutor(self,id_tutor, nombre, password):
        nuevo_tutor = Tutor(id_tutor, nombre, password)
        self.tutores.append(nuevo_tutor)

    def __len__(self):
        return len(self.tutores)
    
    def verificar_tutor(self, id_tutor):
        for tutor in self.tutores:
            if tutor.id_tutor == id_tutor:
                return True
        return False


    def asignar_curso(self, id_tutor, codigo_curso, nombre_curso):
        for tutor in self.tutores:
            if tutor.id_tutor == id_tutor:
                tutor.cursos.agregar_curso(nombre_curso, codigo_curso)
    
    def delete_all_tutor(self):
        self.tutores = []

    def getAllTutores(self):
        return self.tutores
    