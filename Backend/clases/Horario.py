class Horario:
    def __init__(self):
        self.inicio = None
        self.final = None

    def actualizar_horario(self, inicio, final):
        self.inicio = inicio
        self.final = final