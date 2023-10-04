class Dron:  # si
    def __init__(self, nombre):
        self.nombre = nombre
        self.primer_dato = None


class SistemaDron:  # si
    def __init__(self, nombre):
        self.nombre = nombre
        self.primer_dato = None


class SistemaAC:
    def __init__(self, sistema, altura, cantidad):
        self.sistema = sistema
        self.altura = altura
        self.cantidad = cantidad
        self.primer_dato = None


class SysAC:
    def __init__(self, altura, cantidad):
        self.altura = altura
        self.cantidad = cantidad
        self.primer_dato = None


class DronSys:
    def __init__(self, nombre):
        self.nombre = nombre
        self.primer_dato = None


class DronBusqueda:
    def __init__(self, valor):
        self.valor = valor
        self.primer_dato = None


# lista mensajes, entrada
class MmsSistema:  # en uso
    def __init__(self, nombre_mms, mms_sys):
        self.nombre_mms = nombre_mms
        self.mms_sys = mms_sys
        self.primer_dato = None


class MmsSistemaInstruccion:
    def __init__(self, mms_instr, dron_ins, altura_ins):
        self.mms_instr = mms_instr
        self.dron_ins = dron_ins
        self.altura_ins = altura_ins
        self.primer_dato = None


class Mms:
    def __init__(self, mms_dato):
        self.mms_dato = mms_dato
        self.primer_dato = None


class SizesIn:
    def __init__(self, size_ind):
        self.size_ind = size_ind
        self.primer_dato = None


class SizesInOtro:
    def __init__(self, size_otro):
        self.size_otro = size_otro
        self.primer_dato = None


class NuevosTamanos:
    def __init__(self, size_nuevo):
        self.size_nuevo = size_nuevo
        self.primer_dato = None


class MmsSistemaInstruccionOtro:
    def __init__(self, mms_instr, dron_ins, altura_ins):
        self.mms_instr = mms_instr
        self.dron_ins = dron_ins
        self.altura_ins = altura_ins
        self.primer_dato = None
