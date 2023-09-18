class NodoDron:
    def __init__(self, dron):
        self.dron = dron
        self.siguiente = None


class ListaDrones:
    def __init__(self):
        self.primero = None

    def agregar_dron(self, dron):
        nuevo_nodo = NodoDron(dron)
        nuevo_nodo.siguiente = self.primero
        self.primero = nuevo_nodo

    def buscar_dron(self, nombre):
        pass
