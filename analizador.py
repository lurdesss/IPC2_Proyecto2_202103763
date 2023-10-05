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
        self.tamanos_reales = ListaDoble()
        self.lista_mms_all = ListaDoble()

    def cargar_dron(self):
        # datos_en_xml = ET.parse(ruta).getroot()
        for etiqueta_lista_drones in self.datos_en_xml.findall('listaDrones'):
            for etiqueta_dron in etiqueta_lista_drones.findall('dron'):
                dron = Dron(etiqueta_dron.text)
                self.lista_drones.agregar_al_final(dron)
            return self.lista_drones

    def cargar_lista_sistemas_drones(self):
        for etiqueta_lista_sistemas_drones in self.datos_en_xml.findall('listaSistemasDrones'):
            for etiqueta_sistemas_drones in etiqueta_lista_sistemas_drones.findall('sistemaDrones'):
                atributo_nombre = etiqueta_sistemas_drones.get('nombre')
                nuevo_sistema = SistemaDron(atributo_nombre)
                self.lista_sistemas.agregar_al_final(nuevo_sistema)
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

    def mostrar_tamanos(self):
        print("lista de tamanos.......")
        nodo_dron = self.tamanos_individuales.primero
        while nodo_dron:
            print(f"tamano : {nodo_dron.dato.size_ind}")
            nodo_dron = nodo_dron.siguiente
        print("se ha terminado ...")

    def tamanos_individuales_sumando(self):
        print("tamanos individuales sumados")
        nodo_dron = self.tamanos_individuales.primero
        tamano = self.tamanos_individuales.size
        suma = 0
        while nodo_dron:
            for i in range(tamano):
                suma += nodo_dron.dato.size_ind
                nodo_dron = nodo_dron.siguiente
            print(suma)
            break

    def return_algo(self):
        return self.lista_drones

    def graficar_sistemas_drones(self):
        sistemas_en = self.lista_sac.primero
        long_sys = self.lista_sac.size
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
                    f'<TD>sistema: {i+1}</TD>'
                    '</TR>'
                    '<TR>'
                    f'<TD>{sistemas_en.dato.sistema}</TD>'
                    '</TR>'
                    '<TR>'
                    f'<TD>altura: {sistemas_en.dato.altura}</TD>'
                    '</TR>'
                    '<TR>'
                    f'<TD>drones: {sistemas_en.dato.cantidad}</TD>'
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
            return self.lista_mms_sys

    def cargar_mms_all(self):
        for etiqueta_lista_mensajes in self.datos_en_xml.findall('listaMensajes'):
            for etiqueta_mensaje in etiqueta_lista_mensajes.findall('Mensaje'):
                atributo_nombre = etiqueta_mensaje.get('nombre')
                for etiqueta_sistema_drones in etiqueta_mensaje.findall('sistemaDrones'):
                    dato_sistema = etiqueta_sistema_drones.text
                    for etiqueta_instrucciones in etiqueta_mensaje.findall('instrucciones'):
                        for etiqueta_instruccion in etiqueta_instrucciones.findall('instruccion'):
                            atributo_dron = etiqueta_instruccion.get('dron')
                            dato_altura = etiqueta_instruccion.text
                            instrucciones_en = MmsAll(
                                atributo_nombre, dato_sistema, atributo_dron, dato_altura)
                            self.lista_mms_all.agregar_al_final(
                                instrucciones_en)
            return self.lista_mms_all

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

    def tamanos_reales_en(self):
        tamanos_con_final = self.tamanos_individuales.primero
        tamanos_sin_f = self.tamanos_sin_final.primero
        tamano = self.tamanos_individuales.size
        while tamanos_sin_f:
            for i in range(tamano):
                valor_en = tamanos_con_final.dato.size_ind-tamanos_sin_f.dato.size_otro
                nuevo = NuevosTamanos(valor_en)
                self.tamanos_reales.agregar_al_final(nuevo)
                tamanos_con_final = tamanos_con_final.siguiente
                tamanos_sin_f = tamanos_sin_f.siguiente
            break

    def generar_archivo_xml_mms(self):

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
            return self.lista_mms_inst_otro

    def mostrar_tamanos_nuevos(self):
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
