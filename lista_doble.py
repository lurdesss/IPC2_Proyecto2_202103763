from nodo import Nodo


class ListaDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def vacia(self):
        return self.primero == None

    def agregar_al_final(self, dron):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dron)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dron)
            self.ultimo.anterior = aux
        self.size += 1

    def buscar_dron(self, nombre):
        nodo_actual = self.primero
        while nodo_actual:
            if nodo_actual.dato.nombre == nombre:
                return nodo_actual.dato
            nodo_actual = nodo_actual.siguiente
        return None

    def buscar_msg(self, nombre):
        nodo_actual = self.primero
        while nodo_actual:
            if nodo_actual.dato.msg == nombre:
                return nodo_actual.dato
            nodo_actual = nodo_actual.siguiente
        return None

    def buscar_nombre_mms(self, nombre):
        nodo_actual = self.primero
        while nodo_actual:
            if nodo_actual.dato.nombre_mms == nombre:
                return nodo_actual.dato
            nodo_actual = nodo_actual.siguiente
        return None

    def agregar_inicio(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = None
            self.primero = aux
        self.size += 1

    # tiempos optimos
    def suma_para_tiempos_optimos(self):
        nodo_dron = self.primero
        tamano = self.size
        suma = 0
        while nodo_dron:
            for i in range(tamano):
                suma += nodo_dron.dato.tiempo
                nodo_dron = nodo_dron.siguiente
            return suma

    def buscar_mms(self, nombre):
        nodo_actual = self.primero
        while nodo_actual:
            if nodo_actual.dato.mms_dato == nombre:
                return nodo_actual.dato
            nodo_actual = nodo_actual.siguiente
        return None

    def buscar_instru(self, nombre):
        nodo_actual = self.primero
        while nodo_actual:
            if nodo_actual.dato.mms_instr == nombre:
                return nodo_actual.dato
            nodo_actual = nodo_actual.siguiente
        return None

    def eliminar_final(self):
        if self.vacia():
            print("Lista vacía")
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.size = 0
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            self.size -= 1

    def eliminar_inicio(self):
        if self.vacia():
            print("Lista vacía")
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.size = 0
        else:
            self.primero = self.primero.siguiente
            self.primero.anterior = None
            self.size -= 1

    def tamano(self):
        return self.size

    def ordenamiento(self):
        if self.primero is None:
            return
        nodo_actual = self.primero
        while nodo_actual:
            menor = nodo_actual
            siguiente_nodo = nodo_actual.siguiente
            while siguiente_nodo:
                if siguiente_nodo.dato.nombre < menor.dato.nombre:
                    menor = siguiente_nodo
                siguiente_nodo = siguiente_nodo.siguiente
            if menor != nodo_actual:
                # Intercambia posicion nodo_actual y menor
                nodo_actual.dato.nombre, menor.dato.nombre = menor.dato.nombre, nodo_actual.dato.nombre
            nodo_actual = nodo_actual.siguiente
