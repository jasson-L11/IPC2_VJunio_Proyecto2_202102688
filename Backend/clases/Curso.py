class Curso:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        return f"Curso(nombre={self.nombre}, codigo={self.codigo})"

    def __repr__(self):
        return self.__str__()