import xml.etree.ElementTree as ET
from lista_doble import *
from clases_nodo import *

import graphviz


class Analizador:
    def __init__(self, ruta):
        self.datos_en_xml = ET.parse(ruta).getroot()
        self.lista_drones = ListaDoble()  # drones en sistema
        self.lista_sistemas = ListaDoble()  # sistemas uno a uno
        self.lista_mms_sys = ListaDoble()  # mms sistema
        self.lista_mms_solo = ListaDoble()  # mms
        self.lista_mms_inst = ListaDoble()  # sistema dron dato
        self.lista_altura_cantidad = ListaDoble()  # solo altura cantidad
        self.lista_sac = ListaDoble()  # sistema altura cantidad
        self.lista_drones_en_sys = ListaDoble()
        self.lista_busqueda = ListaDoble()  # para busqueda
        self.lista_ordenada = ListaDoble()
        self.tamanos_individuales = ListaDoble()  # tamanos de mms
        self.tamanos_sin_final = ListaDoble()
        self.lista_mms_inst_otro = ListaDoble()
        # self.tamanos_reales = ListaDoble()

    def cargar_dron(self):
        # datos_en_xml = ET.parse(ruta).getroot()
        for etiqueta_lista_drones in self.datos_en_xml.findall('listaDrones'):
            for etiqueta_dron in etiqueta_lista_drones.findall('dron'):
                dron = Dron(etiqueta_dron.text)
                self.lista_drones.agregar_al_final(dron)
                tamano = self.lista_drones.size
            print("imprimiendo size")
            print(tamano)
            print("imprimiendo lista de drones")
            nodo_dron = self.lista_drones.primero
            while nodo_dron:
                print(nodo_dron.dato.nombre)
                nodo_dron = nodo_dron.siguiente

            return self.lista_drones

    def mostrar_drones(self):
        print("lista de drones.......")
        nodo_dron = self.lista_drones.primero
        while nodo_dron:
            print(f"dron : {nodo_dron.dato.nombre}")
            nodo_dron = nodo_dron.siguiente
        print("se ha terminado")

    def cargar_lista_sistemas_drones(self):
        # datos_en_xml = ET.parse(ruta).getroot()
        for etiqueta_lista_sistemas_drones in self.datos_en_xml.findall('listaSistemasDrones'):
            for etiqueta_sistemas_drones in etiqueta_lista_sistemas_drones.findall('sistemaDrones'):
                atributo_nombre = etiqueta_sistemas_drones.get('nombre')
                nuevo_sistema = SistemaDron(atributo_nombre)
                self.lista_sistemas.agregar_al_final(nuevo_sistema)
                tamanox = self.lista_sistemas.size

            print("imprimiendo size")
            print(tamanox)
            print("imprimiendo lista de sistemas")
            nodo_dron = self.lista_sistemas.primero
            while nodo_dron:
                print(nodo_dron.dato.nombre)
                nodo_dron = nodo_dron.siguiente
            return self.lista_sistemas

    def cargar_altura_cantidad(self):
        for etiqueta_lista_sistemas_drones in self.datos_en_xml.findall('listaSistemasDrones'):
            for etiqueta_sistemas_drones in etiqueta_lista_sistemas_drones.findall('sistemaDrones'):
                for a_max in etiqueta_sistemas_drones.findall('alturaMaxima'):
                    altura_maxima = a_max.text
                    for c_dron in etiqueta_sistemas_drones.findall('cantidadDrones'):
                        cantidad_drones = c_dron.text
                        nuevalista = SysAC(altura_maxima, cantidad_drones)
                        self.lista_altura_cantidad.agregar_al_final(nuevalista)
                    #     tamanoy = self.lista_altura_cantidad.size
                    # print("imprimiendo size de altura cantidad")
                    # print(tamanoy)
                    print("imprimiendo altura maxima")
                    nodo_dron = self.lista_altura_cantidad.primero
                    while nodo_dron:
                        print(nodo_dron.dato.altura)
                        nodo_dron = nodo_dron.siguiente
                    print("imprimiendo cantidad")
                    nodo_dron = self.lista_altura_cantidad.primero
                    while nodo_dron:
                        print(nodo_dron.dato.cantidad)
                        nodo_dron = nodo_dron.siguiente
            return self.lista_altura_cantidad

    def cargar_sac(self):
        for etiqueta_lista_sistemas_drones in self.datos_en_xml.findall('listaSistemasDrones'):
            for etiqueta_sistemas_drones in etiqueta_lista_sistemas_drones.findall('sistemaDrones'):
                atributo_nombre = etiqueta_sistemas_drones.get('nombre')
                for a_max in etiqueta_sistemas_drones.findall('alturaMaxima'):
                    altura_maxima = a_max.text
                    for c_dron in etiqueta_sistemas_drones.findall('cantidadDrones'):
                        cantidad_drones = c_dron.text
                        nuevalista = SistemaAC(
                            atributo_nombre, altura_maxima, cantidad_drones)
                        self.lista_sac.agregar_al_final(nuevalista)
                    #     tamanoy = self.lista_sac.size
                    # print("imprimiendo size de altura cantidad sac")
                    # print(tamanoy)
                    print("imprimiendo sistema sac")
                    nodo_dron = self.lista_sac.primero
                    while nodo_dron:
                        print(nodo_dron.dato.sistema)
                        nodo_dron = nodo_dron.siguiente
                    print("imprimiendo altura maxima sac")
                    nodo_dron = self.lista_sac.primero
                    while nodo_dron:
                        print(nodo_dron.dato.altura)
                        nodo_dron = nodo_dron.siguiente
                    print("imprimiendo cantidad sac")
                    nodo_dron = self.lista_sac.primero
                    while nodo_dron:
                        print(nodo_dron.dato.cantidad)
                        nodo_dron = nodo_dron.siguiente
            return self.lista_sac

    def cargar_lista_drones_sys(self):
        # datos_en_xml = ET.parse(ruta).getroot()
        for etiqueta_lista_sistemas_drones in self.datos_en_xml.findall('listaSistemasDrones'):
            for etiqueta_sistemas_drones in etiqueta_lista_sistemas_drones.findall('sistemaDrones'):
                for etiqueta_contenido in etiqueta_sistemas_drones.findall('contenido'):
                    for etiqueta_dron in etiqueta_contenido.findall('dron'):
                        dron_en = DronSys(etiqueta_dron.text)
                        self.lista_drones_en_sys.agregar_al_final(dron_en)
                    print("imprimiendo drones en sys")
                    nodo_dron = self.lista_drones_en_sys.primero
                    while nodo_dron:
                        print(nodo_dron.dato.nombre)
                        nodo_dron = nodo_dron.siguiente
            return self.lista_sistemas

    def mostrar_drones_en_sys(self):
        print("lista de drones en sys prueba.......")
        nodo_dron = self.lista_drones_en_sys.primero
        while nodo_dron:
            print(f"dron : {nodo_dron.dato.nombre}")
            nodo_dron = nodo_dron.siguiente
        print("se ha terminado ...")

    # def traendo_tamanos(self):
    #     nodo_instr = self.lista_mms_inst.ultimo
    #     nodo_sms = self.lista_mms_solo.primero
    #     tamano_sms = self.lista_mms_solo.size
    #     while nodo_sms:
    #         contador = 1
    #         # es_otro = False
    #         for i in range(tamano_sms-1):
    #             while nodo_instr:
    #                 valor1 = nodo_sms.dato.mms_dato
    #                 if not self.lista_mms_inst.buscar_mms(valor1):
    #                     contador += 1
    #                 nodo_instr = nodo_instr.anterior
    #                 a_lista = SizesIn(contador)
    #                 self.tamanos_individuales.agregar_inicio(a_lista)
    #                 # nuevo_size = contador
    #                 # else:
    #                 #     nuevo_size = contador
    #                 #     a_lista = SizesIn(nuevo_size)
    #                 #     self.tamanos_individuales.agregar_inicio(a_lista)
    #                 # contador = 1
    #                 # es_otro = True
    #                 break
    #             nodo_sms = nodo_sms.siguiente
    #         # if es_otro:
    #         #     nuevo_size = contador
    #         #     a_lista = SizesIn(nuevo_size)
    #         #     self.tamanos_individuales.agregar_inicio(a_lista)
    #         break

    def mostrar_tamanos(self):
        print("lista de tamanos.......")
        nodo_dron = self.tamanos_individuales.primero
        while nodo_dron:
            print(f"tamano : {nodo_dron.dato.size_ind}")
            nodo_dron = nodo_dron.siguiente
        print("se ha terminado ...")

    def return_algo(self):
        return self.lista_drones

    def graficar_sistemas_drones(self):
        sistemas_en = self.lista_sistemas.primero
        long_sys = self.lista_sistemas.size
        # print(long_sys)
        self.dot = graphviz.Digraph('html_table', node_attr={
            'shape': 'plaintext', 'width': '-4'})
        self.dot.attr(bgcolor='#708090',
                      label='sistemas de drones', fontcolor='#F0F8FF', fontname='Lucida Sans')
        while sistemas_en:
            for i in range(long_sys):
                self.dot.node(
                    f'{i+1}', fontname='Lucida Sans', fontcolor='#F0F8FF', label='<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">'
                    '<TR>'
                    f'<TD>sistema {i+1}</TD>'
                    '</TR>'
                    '<TR>'
                    f'<TD>{sistemas_en.dato.nombre}</TD>'
                    '</TR>'
                    '</TABLE>>')
                sistemas_en = sistemas_en.siguiente
        self.dot.render(outfile=f'files/sistemas.png').replace('\\', '/')

    def cargar_mms_sys(self):
        for etiqueta_lista_mensajes in self.datos_en_xml.findall('listaMensajes'):
            for etiqueta_mensaje in etiqueta_lista_mensajes.findall('Mensaje'):
                atributo_nombre = etiqueta_mensaje.get('nombre')
                for etiqueta_sistema_drones in etiqueta_mensaje.findall('sistemaDrones'):
                    sistema_mms = etiqueta_sistema_drones.text
                    nombre_sistema = MmsSistema(atributo_nombre, sistema_mms)
                    self.lista_mms_sys.agregar_al_final(nombre_sistema)
                    tamano = self.lista_mms_sys.size
                print(tamano)
                print("imprimiendo nombre de mensaje")
                nodo_dron = self.lista_mms_sys.primero
                while nodo_dron:
                    print(nodo_dron.dato.nombre_mms)
                    nodo_dron = nodo_dron.siguiente
                print("imprimiendo sistema que usa")
                nodo_dron = self.lista_mms_sys.primero
                while nodo_dron:
                    print(nodo_dron.dato.mms_sys)
                    nodo_dron = nodo_dron.siguiente
            return self.lista_mms_sys

    def cargar_mms_solo(self):
        for etiqueta_lista_mensajes in self.datos_en_xml.findall('listaMensajes'):
            for etiqueta_mensaje in etiqueta_lista_mensajes.findall('Mensaje'):
                atributo_nombre = etiqueta_mensaje.get('nombre')
                solo_mensaje = Mms(atributo_nombre)
                self.lista_mms_solo.agregar_al_final(solo_mensaje)
                tamano = self.lista_mms_solo.size
            print(tamano)
            print("imprimiendo solo nombre de mensaje")
            nodo_dron = self.lista_mms_solo.primero
            while nodo_dron:
                print(nodo_dron.dato.mms_dato)
                nodo_dron = nodo_dron.siguiente
            return self.lista_mms_solo

    def generar_archivo_xml_mms(self):
        # self.primerosss

        ruta = "files/mensajes.xml"
        with open(ruta, "w") as salida:
            salida.write('<?xml version =' + '"' + str(1.0) +
                         '"' + ' encoding = ' + str('"UTF-8"') + '?>\n')
            salida.write('<respuesta>\n')
            salida.write('   <listaMensajes>\n')
            mensaje_actual = self.lista_mms_sys.primero
            while mensaje_actual:
                mensaje = mensaje_actual.dato
                salida.write(f'      <mensaje="{mensaje.nombre_mms}">\n')
                salida.write(
                    f'      <sistemaDrones>{mensaje.mms_sys}</sistemaDrones>\n')
                salida.write(
                    f'      <tiempoOptimo> </tiempoOptimo>\n')
                salida.write(
                    f'      <mensajeRecibido> </mensajeRecibido>\n')
                salida.write('      <instrucciones>\n')
                # tiempo acciones dron
                salida.write('      </instrucciones>\n')
                salida.write('      </mensaje>\n')
                mensaje_actual = mensaje_actual.siguiente
            salida.write('   </listaMensajes>\n')
            salida.write('</respuesta>\n')

    def cargar_mms_inst(self):
        for etiqueta_lista_mensajes in self.datos_en_xml.findall('listaMensajes'):
            for etiqueta_mensaje in etiqueta_lista_mensajes.findall('Mensaje'):
                atributo_nombre = etiqueta_mensaje.get('nombre')
                # for etiqueta_sistema_drones in etiqueta_mensaje.findall('sistemaDrones'):
                #     # sistema_mms = etiqueta_sistema_drones.text
                for etiqueta_instrucciones in etiqueta_mensaje.findall('instrucciones'):
                    for etiqueta_instruccion in etiqueta_instrucciones.findall('instruccion'):
                        atributo_dron = etiqueta_instruccion.get('dron')
                        dato_altura = etiqueta_instruccion.text
                        instrucciones_en = MmsSistemaInstruccion(
                            atributo_nombre, atributo_dron, dato_altura)
                        self.lista_mms_inst.agregar_al_final(
                            instrucciones_en)
                    tamano = self.lista_mms_inst.size
                    valor_tamano_en = SizesIn(tamano)
                    self.tamanos_individuales.agregar_al_final(
                        valor_tamano_en)
                    print("imprimiendo sistemas que usa")
                    nodo_dron = self.lista_mms_inst.primero
                    while nodo_dron:
                        print(nodo_dron.dato.mms_instr)
                        nodo_dron = nodo_dron.siguiente
                    print("imprimiendo drones que usa")
                    nodo_dron = self.lista_mms_inst.primero
                    while nodo_dron:
                        print(nodo_dron.dato.dron_ins)
                        nodo_dron = nodo_dron.siguiente
                    print("imprimiendo datos en")
                    nodo_dron = self.lista_mms_inst.primero
                    while nodo_dron:
                        print(nodo_dron.dato.altura_ins)
                        nodo_dron = nodo_dron.siguiente
            return self.lista_mms_inst

    def cargar_mms_solo_otro(self):
        for etiqueta_lista_mensajes in self.datos_en_xml.findall('listaMensajes'):
            for etiqueta_mensaje in etiqueta_lista_mensajes.findall('Mensaje'):
                atributo_nombre = etiqueta_mensaje.get('nombre')
                # for etiqueta_sistema_drones in etiqueta_mensaje.findall('sistemaDrones'):
                #     # sistema_mms = etiqueta_sistema_drones.text
                for etiqueta_instrucciones in etiqueta_mensaje.findall('instrucciones'):
                    for etiqueta_instruccion in etiqueta_instrucciones.findall('instruccion'):
                        atributo_dron = etiqueta_instruccion.get('dron')
                        dato_altura = etiqueta_instruccion.text
                        instrucciones_en = MmsSistemaInstruccionOtro(
                            atributo_nombre, atributo_dron, dato_altura)
                        self.lista_mms_inst_otro.agregar_al_final(
                            instrucciones_en)
                    tamano = self.lista_mms_inst_otro.size
                    valor_tamano_en_proceso = SizesInOtro(tamano)
                    self.tamanos_sin_final.agregar_al_final(
                        valor_tamano_en_proceso)
                    print("imprimiendo sistemas que usa")
                    nodo_dron = self.lista_mms_inst_otro.primero
                    while nodo_dron:
                        print(nodo_dron.dato.mms_instr)
                        nodo_dron = nodo_dron.siguiente
                    print("imprimiendo drones que usa")
                    nodo_dron = self.lista_mms_inst_otro.primero
                    while nodo_dron:
                        print(nodo_dron.dato.dron_ins)
                        nodo_dron = nodo_dron.siguiente
                    print("imprimiendo datos en")
                    nodo_dron = self.lista_mms_inst_otro.primero
                    while nodo_dron:
                        print(nodo_dron.dato.altura_ins)
                        nodo_dron = nodo_dron.siguiente
            return self.lista_mms_inst_otro

    # def nueva_lista(self):
    #     nodo_ultimo = self.tamanos_individuales.primero
    #     rango_de = self.tamanos_individuales.size
    #     print(rango_de)
    #     # nodo_primero = self.tamanos_individuales.primero
    #     agregar_faltante = "0"
    #     self.tamanos_sin_final.agregar_al_final(int(agregar_faltante))
    #     self.tamanos_sin_final.eliminar_inicio()
    #     nodo_sinfinal = self.tamanos_sin_final.primero
    #     while (nodo_ultimo and nodo_sinfinal):
    #         for i in range(rango_de):
    #             valor1 = nodo_ultimo.dato.size_ind
    #             valor2 = nodo_sinfinal.dato.size_otro
    #             en_nodo_a = valor1-valor2
    #             en_lista_a = NuevosTamanos(en_nodo_a)
    #             self.tamanos_reales.agregar_inicio(en_lista_a)
    #         nodo_ultimo = nodo_ultimo.siguiente
    #         nodo_sinfinal = nodo_sinfinal.siguiente

    def mostrar_tamanos_nuevos(self):
        print("lista de tamanos nuevos.......")
        agregar_faltante = 0
        zero_in = SizesInOtro(agregar_faltante)
        self.tamanos_sin_final.agregar_inicio(zero_in)
        self.tamanos_sin_final.eliminar_final()
        nodo_dron = self.tamanos_sin_final.primero
        while nodo_dron:
            print(f"tamano : {nodo_dron.dato.size_otro}")
            nodo_dron = nodo_dron.siguiente
        # print("se ha terminado ...")
        return self.tamanos_sin_final

        # while nodo_ultimo:
        #     valor1 = nodo_ultimo.dato.size_ind
        #     numero = valor1 - valor1
        #     valor2 = numero - valor1
        #     while valor1 <= 0:
        #         nodo_ultimo = nodo_ultimo.anterior
        #         valor3 = nodo_ultimo.dato.size_ind
        #         otro = valor2 - valor3
        #         en_lista =

        # valor2 = nodo_ultimo.anterior
        # nuevo_valor_en_lista = valor1-valor2
        # print(nuevo_valor_en_lista)
        # break

    # def traendo_tamanos(self):
    #     nodo_instr = self.lista_mms_inst.ultimo
    #     nodo_sms = self.lista_mms_solo.primero
    #     tamano_sms = self.lista_mms_solo.size
    #     while nodo_sms:
    #         contador = 1
    #         # es_otro = False
    #         for i in range(tamano_sms-1):
    #             while nodo_instr:
    #                 valor1 = nodo_sms.dato.mms_dato
    #                 if not self.lista_mms_inst.buscar_mms(valor1):
    #                     contador += 1
    #                 nodo_instr = nodo_instr.anterior
    #                 a_lista = SizesIn(contador)
    #                 self.tamanos_individuales.agregar_inicio(a_lista)
    #                 # nuevo_size = contador
    #                 # else:
    #                 #     nuevo_size = contador
    #                 #     a_lista = SizesIn(nuevo_size)
    #                 #     self.tamanos_individuales.agregar_inicio(a_lista)
    #                 # contador = 1
    #                 # es_otro = True
    #                 break
    #             nodo_sms = nodo_sms.siguiente
    #         # if es_otro:
    #         #     nuevo_size = contador
    #         #     a_lista = SizesIn(nuevo_size)
    #         #     self.tamanos_individuales.agregar_inicio(a_lista)
    #         break

    # def ordenar_lista(self):
    #     nodo_actual = self.lista_drones.primero
    #     # print("prueba de orden")
    #     # asci = ascii == 65
    #     # print(asci)
    #     for caracter in nodo_actual.dato.nombre:
    #         ascii = ord(caracter)
    #         i=65
    #         for j in range(25):
    #             if ascii ==i:

    #     valor_variando = "Dron" + asci
    #     if asci ==
    #     print(valor_variando)
        # while nodo_actual:
        #     if "Dron" in nodo_actual.dato.nombre:
        #         # return nodo_actual.dato
        #         print(nodo_actual.dato.nombre)
        #         nodo_actual = nodo_actual.siguiente
        #     else:
        #         print("no es un nombre valido")
        #         break

    def lista_drones_procesar(self):
        self.mostrar_drones_en_sys()
        # datos_en_xml = ET.parse(ruta).getroot()
        for etiqueta_lista_sistemas_drones in self.datos_en_xml.findall('listaSistemasDrones'):
            for etiqueta_sistemas_drones in etiqueta_lista_sistemas_drones.findall('sistemaDrones'):
                for etiqueta_contenido in etiqueta_sistemas_drones.findall('contenido'):
                    for etiqueta_dron in etiqueta_contenido.findall('dron'):
                        dron_en = DronBusqueda(etiqueta_dron.text)
                        self.lista_busqueda.agregar_al_final(dron_en)
                        # self.lista_drones_en_sys.agregar_al_final(dron_en)
                        for etiqueta_alturas in etiqueta_contenido.findall('alturas'):
                            for etiqueta_altura in etiqueta_alturas.findall('altura'):
                                letra_en = DronBusqueda(etiqueta_altura.text)
                                self.lista_busqueda.agregar_al_final(letra_en)
                                tamanok = self.lista_busqueda.size
                            print("tamaño de lista busqueda")
                            print(tamanok)
                            print("imprimiendo drones en sys")
                            nodo_dron = self.lista_busqueda.primero
                            while nodo_dron:
                                print(nodo_dron.dato.valor)
                                nodo_dron = nodo_dron.siguiente

    # def cargar_lista_sistemas_drones(self):
    #     # datos_en_xml = ET.parse(ruta).getroot()
    #     for etiqueta_lista_sistemas_drones in self.datos_en_xml.findall('listaSistemasDrones'):
    #         for etiqueta_sistemas_drones in etiqueta_lista_sistemas_drones.findall('sistemaDrones'):
    #             atributo_nombre = etiqueta_sistemas_drones.get('nombre')
    #             # nuevo_sistema = SistemaDrones(atributo_nombre)
    #             for a_max in etiqueta_lista_sistemas_drones.findall('alturaMaxima'):
    #                 altura_maxima = a_max.text
    #                 for c_drones in etiqueta_lista_sistemas_drones.findall('cantidadDrones'):
    #                     cantidad_en = c_drones.text
    #                     lista_s = SistemaAC(
    #                         atributo_nombre, altura_maxima, cantidad_en)
    #                     self.lista_sistemas.agregar_al_final(lista_s)
    #                     tamanox = self.lista_sistemas.size
    #                 print("imprimiendo size")
    #                 print(tamanox)
    #         return self.lista_sistemas

    # def agregar_dato_dron(self, )

    # def mostrar(self, dron):

    # def mostrar_sistemas(self):
    #     print("lista de sistemas.......")
    #     nodo_sistema = self.lista_sistemas.primero
    #     while nodo_sistema:
    #         print(f"dron : {nodo_sistema.sistema.sistema}")
    #         nodo_sistema = nodo_sistema.siguiente
    #     print("se ha terminado")
        # return nodo_dron

    #     # nodo_dron = self.lista_drones.primero
    #     # while nodo_dron:
    #     #     nodo_dron.dron.nombre
    #     #     nodo_dron = nodo_dron.siguiente

    # def otro(self):
    #     return self.lista_drones
