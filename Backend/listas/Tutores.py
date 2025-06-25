from clases.Tutor import Tutor

class Tutores:
    def __init__(self):
        self.tutores = []

    def agregar_tutor(self, nombre,  id_tutor, password):
        nuevo_tutor = Tutor(nombre, id_tutor, password)
        self.tutores.append(nuevo_tutor)

    def __len__(self):
        return len(self.tutores)
