from clases.Actividad import Actividad

class Actividades:
    def __init__(self):
        self.actividades = []

    def agregar_actividad(self, nombre, carnet, puntos):
        nueva_actividad = Actividad(nombre, carnet, puntos)
        self.actividades.append(nueva_actividad)

    def __len__(self):
        return len(self.actividades)
    