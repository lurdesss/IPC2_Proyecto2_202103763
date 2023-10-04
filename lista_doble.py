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

    def agregar_inicio(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = None
            self.primero = aux
        self.size += 1

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
    # def ordenar(self):
    #     nodo_actual = self.primero
    #     while nodo_actual:

    # def ordenar_lista(self):
    #     nodo_actual = self.primero
    #     while nodo_actual:
    #         i = 97
    #         for caracter in nodo_actual.dato.nombre:
    #             ascii = ord(caracter)
    #             # for j in range(self.size):
    #             while i in ascii and i < 122:
    #                 return nodo_actual.dato
    #             i += 1
    #             nodo_actual = nodo_actual.siguiente

    #             # else:
    #             #     # self.primero = self.ultimo
    #             #     aux = self.ultimo
    #             #     self.ultimo = aux.siguiente
    #             #     self.ultimo.anterior = aux
    #         break

    # # def ordenar_lista(self):
    # #     nodo_actual = self.primero
    # #     while nodo_actual:
    # #         i = 65
    # #         j = 97
    # #         for caracter in nodo_actual.dato.nombre:
    # #             ascii = ord(caracter)
    # #             for j in range(self.size):
    # #             if ascii == 68 in caracter:
    # #                 return nodo_actual.dato
    # #             print("es ordenado")
    # #             i += 1
    # #             nodo_actual = nodo_actual.siguiente
    # #         else:
    # #             print("no es valido")

    # #             else:
    # #                 # self.primero = self.ultimo
    # #                 aux = self.ultimo
    # #                 self.ultimo = aux.siguiente
    # #                 self.ultimo.anterior = aux
    # #         break

    def ordenar_lista(self):
        nodo_actual = self.primero
        while nodo_actual:
            if "Dron" in nodo_actual.dato.nombre:
                return nodo_actual.dato
            # print(nodo_actual.dato.nombre)
            else:
                aux = self.ultimo
                self.ultimo = aux.siguiente
                self.ultimo.anterior = aux
            self.size += 1

        else:
            print("no es un nombre valido")

    # def ordenar_lista(self):
    #     nodo_actual = self.primero
    #     while nodo_actual:
    #         if "Dron" in nodo_actual.dato.nombre:
    #             return nodo_actual.dato
    #         nodo_actual = nodo_actual.siguiente
    #     else:
    #         print("no es un nombre valido")

    def tamano(self):
        return self.size
