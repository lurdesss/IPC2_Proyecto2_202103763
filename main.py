from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox
import webbrowser
import sys
import os

from analizador import Analizador

# Analizador
import xml.etree.ElementTree as ET
from lista_doble import *
from clases_nodo import *


class Sistema():
    def __init__(self):
        self.principal()
        self.carga = None
        self.valor_busqueda = None

# ventana principal
    def principal(self):
        self.ventana = Tk()
        self.ventana.resizable(0, 0)
        self.ventana.config(bg="#2c2e2f", bd=5)
        self.ventana.title("sistema de drones")
        self.ventana.geometry("420x320")
        self.centrar(self.ventana, 420, 320)
        Button(self.ventana, text="Cargar archivo XML", command=self.cargar_archivo,
               width=30, height=1, font=("Lucida Sans", 12), background='#151718',
               foreground='#F5F5F5', activeforeground='black', activebackground='gray52').place(x=50, y=40)
        Button(self.ventana, text="Generar archivo XML", command=self.generar_archivo,
               width=30, height=1, font=("Lucida Sans", 12), background='#151718',
               foreground='#F5F5F5', activeforeground='black', activebackground='gray52').place(x=50, y=80)
        Button(self.ventana, text="Gestión de drones", command=self.gestionar_dron,
               width=30, height=1, font=("Lucida Sans", 12), background='#151718',
               foreground='#F5F5F5', activeforeground='black', activebackground='gray52').place(x=50, y=120)
        Button(self.ventana, text="Gestión de sistema de drones", command=self.gestionar_sistema_dron,
               width=30, height=1, font=("Lucida Sans", 12), background='#151718',
               foreground='#F5F5F5', activeforeground='black', activebackground='gray52').place(x=50, y=160)
        Button(self.ventana, text="Gestión de mensajes", command=self.gestionar_mensaje,
               width=30, height=1, font=("Lucida Sans", 12), background='#151718',
               foreground='#F5F5F5', activeforeground='black', activebackground='gray52').place(x=50, y=200)
        # Opciones
        Button(self.ventana, text="Inicializar", command=self.inicializar,
               width=14, height=1, font=("Lucida Sans", 12), background='#f7ff19',
               foreground='black', activeforeground='black', activebackground='gray52').place(x=50, y=240)
        Button(self.ventana, text="Ayuda", command=self.ayuda,
               width=14, height=1, font=("Lucida Sans", 12), background='#f7ff19',
               foreground='black', activeforeground='black', activebackground='gray52').place(x=210, y=240)

        self.ventana.mainloop()

    def centrar(self, ventana, ancho, alto):
        altura_pantalla = ventana.winfo_screenheight()
        ancho_pantalla = ventana.winfo_screenwidth()
        ancho_x = (ancho_pantalla//2) - (ancho//2)
        altura_y = (altura_pantalla//2) - (alto//2)
        ventana.geometry(f"+{ancho_x}+{altura_y}")

    def inicializar(self):  # INCISO A
        python = sys.executable
        os.execl(python, python, * sys.argv)

    def cargar_archivo(self):  # INCISO B
        filepath = askopenfilename(
            filetypes=[("archivos XML", "*.xml"), ("Todos los archivos", "*.*")])
        if not filepath:
            return
        self.carga = Analizador(filepath)
        self.carga.cargar_dron()
        self.carga.cargar_lista_sistemas_drones()
        self.carga.cargar_altura_cantidad()
        self.carga.cargar_sac()
        self.carga.cargar_lista_drones_sys()
        self.carga.cargar_mms_sys()
        self.carga.cargar_mms_inst()
        self.carga.cargar_mms_solo()
        self.carga.mostrar_tamanos()
        self.carga.cargar_mms_solo_otro()
        self.carga.mostrar_tamanos_nuevos()
        self.carga.tamanos_individuales_sumando()
        self.carga.tamanos_reales_en()
        self.carga.cargar_mms_all()

    def generar_archivo(self):  # INCISO C
        self.carga.generar_archivo_xml_mms()

    def gestionar_dron(self):  # INCISO D
        self.ventana.destroy()
        self.gestion_de_drones_principal()

    # gestion de sistemas de drones / grafica
    def gestionar_sistema_dron(self):  # INCISO E
        self.carga.graficar_sistemas_drones()

    def gestionar_mensaje(self):  # INCISO F
        self.ventana.destroy()
        self.gestion_de_mms_a_principal()

    def ayuda(self):  # INCISO G
        self.ventana.destroy()
        self.ayuda_datos_documentacion()

# ventana gestion de drones
    def gestion_de_drones_principal(self):  # INCISO D
        self.ventana_gestion = Tk()
        self.ventana_gestion.title("gestión de drones")
        self.ventana_gestion.geometry("510x450")
        self.ventana_gestion.config(background="#f0f0f0")
        self.centrar(self.ventana_gestion, 510, 450)
        # self.resizable(0, 0)
        # self.overrideredirect(True)
        self.scroll_ver_listado = ScrollText(self.ventana_gestion)
        self.scroll_ver_listado.place(x=5, y=26)
        self.ventana_gestion.after(200, self.scroll_ver_listado.redraw())

        # entry
        self.entry_agregar = Entry(
            self.ventana_gestion, width=20, justify="center", font=("Lucida Sans", 10))
        self.entry_agregar.place(x=170, y=379)

        # label
        self.lbl_valor = Label(self.ventana_gestion, text="[valor alfanumérico]", bg=(
            "#f0f0f0"), fg=("#151718"), font=("Lucida Sans", 10))
        self.lbl_valor.place(x=35, y=377)

        self.lbl_orden = Label(self.ventana_gestion, text="[drones en sistema]", bg=(
            "#f0f0f0"), fg=("#151718"), font=("Lucida Sans", 10))
        self.lbl_orden.place(x=185, y=4)

        # botones
        btn_agregarNuevo = Button(self.ventana_gestion, text="Agregar nuevo", command=self.agregar_nuevo_gestion,
                                  width=13, height=1, font=("Lucida Sans", 10), bg="#2c2e2f", foreground="white")
        btn_agregarNuevo.place(x=350, y=375)

        btn_verListado = Button(self.ventana_gestion, text="Ver listado", command=self.ver_listado_drones_gestion,
                                width=13, height=1, font=("Lucida Sans", 10), bg="#2c2e2f", foreground="white")
        btn_verListado.place(x=140, y=412)

        btn_regresarMenu = Button(self.ventana_gestion, text="Volver a menu", command=self.__ir_pantalla_menu_desde_gestion,
                                  width=13, height=1, font=("Lucida Sans", 10), bg="#2c2e2f", foreground="white")
        btn_regresarMenu.place(x=260, y=412)

        # self.ventana_gestion.mainloop()
    # funciones
    def ver_listado_drones_gestion(self):
        try:
            print("Mostrando listado de drones...")
            self.scroll_ver_listado.delete(1.0, tk.END)
            drones_en = self.carga.lista_drones.primero
            self.carga.lista_drones.ordenamiento()
            # long = self.carga.lista_drones.size
            long = self.carga.lista_drones.tamano()
            print(long)
            while drones_en:
                for i in range(long):
                    self.scroll_ver_listado.insert(
                        tk.END, f"  {drones_en.dato.nombre}" + "\n")
                    drones_en = drones_en.siguiente
                break
        except Exception as e:  # mostrar mensaje
            print("Error al ver listado de drones:", e)

    def agregar_nuevo_gestion(self):
        try:
            valores_entrada = self.entry_agregar.get()
            while valores_entrada:
                if not self.carga.lista_drones.buscar_dron(valores_entrada):
                    valor_salida = Dron(valores_entrada)
                    agregando = self.carga.lista_drones.agregar_al_final(
                        valor_salida)
                break
        except Exception as e:  # mostrar mensaje
            print("Error al ver listado de drones:", e)

    def __ir_pantalla_menu_desde_gestion(self):
        self.ventana_gestion.destroy()
        self.principal()

# ventana gestion de mms A
    def gestion_de_mms_a_principal(self):
        self.ventana_mms_a = Tk()
        self.ventana_mms_a.title("gestión de mensajes")
        self.ventana_mms_a.geometry("510x415")
        self.ventana_mms_a.config(background="#f0f0f0")
        self.centrar(self.ventana_mms_a, 510, 415)
        # self.resizable(0, 0)
        # self.overrideredirect(True)
        self.scroll_ver_listado_mms = ScrollText(self.ventana_mms_a)
        self.scroll_ver_listado_mms.place(x=5, y=26)
        self.ventana_mms_a.after(200, self.scroll_ver_listado_mms.redraw())

        # label
        self.lbl_orden = Label(self.ventana_mms_a, text="[mensajes e instrucciones]", bg=(
            "#f0f0f0"), fg=("#151718"), font=("Lucida Sans", 10))
        self.lbl_orden.place(x=150, y=4)

        # botones
        btn_verListado = Button(self.ventana_mms_a, text="Ver listado", command=self.ver_listado_drones_mms_a,
                                width=13, height=1, font=("Lucida Sans", 10), bg="#2c2e2f", foreground="white")
        btn_verListado.place(x=80, y=375)

        btn_agregarNuevo = Button(self.ventana_mms_a, text="Ver instruccion", command=self.ver_instrucciones_mms_a,
                                  width=13, height=1, font=("Lucida Sans", 10), bg="#2c2e2f", foreground="white")
        btn_agregarNuevo.place(x=200, y=375)

        btn_regresarMenu = Button(self.ventana_mms_a, text="Volver a menu", command=self.__ir_pantalla_menu_desde_mms_a,
                                  width=13, height=1, font=("Lucida Sans", 10), bg="#2c2e2f", foreground="white")
        btn_regresarMenu.place(x=320, y=375)

    # funciones
    def ver_listado_drones_mms_a(self):
        try:
            print("Mostrando listado de mensajes e instrucciones")
            self.scroll_ver_listado_mms.delete(1.0, tk.END)
            mensajes_en = self.carga.lista_mms_solo.primero
            long_mms = self.carga.lista_mms_solo.size
            instrucciones_en = self.carga.lista_mms_inst.primero
            tamanos_definitivos = self.carga.tamanos_reales.primero
            while mensajes_en and tamanos_definitivos:
                for i in range(long_mms):
                    self.scroll_ver_listado_mms.insert(
                        tk.END, f" {mensajes_en.dato.mms_dato}" + "\n")
                    while instrucciones_en:
                        for i in range(tamanos_definitivos.dato.size_nuevo):
                            self.scroll_ver_listado_mms.insert(
                                tk.END, f"    {instrucciones_en.dato.dron_ins} , {instrucciones_en.dato.altura_ins}" + "\n")
                            instrucciones_en = instrucciones_en.siguiente
                        break
                    tamanos_definitivos = tamanos_definitivos.siguiente
                    mensajes_en = mensajes_en.siguiente
                break
        except Exception as e:  # mostrar mensaje
            print("Error:", e)

    def ver_instrucciones_mms_a(self):
        self.ventana_mms_a.destroy()
        self.gestion_de_mms_b_principal()

    def __ir_pantalla_menu_desde_mms_a(self):
        self.ventana_mms_a.destroy()
        self.principal()

# ventana gestion mms B
    def gestion_de_mms_b_principal(self):
        self.ventana_mms_b = Tk()
        self.ventana_mms_b.title("gestión de mensajes")
        self.ventana_mms_b.geometry("510x450")
        self.ventana_mms_b.config(background="#f0f0f0")
        self.centrar(self.ventana_mms_b, 510, 450)
        # self.resizable(0, 0)
        # self.overrideredirect(True)
        self.scroll_ver_listado_ins = ScrollText(self.ventana_mms_b)
        self.scroll_ver_listado_ins.place(x=5, y=26)
        self.ventana_mms_b.after(200, self.scroll_ver_listado_ins.redraw())

        # valores de busqueda
        self.valor_busqueda = None

        # entry
        self.entry_buscar_mms = Entry(
            self.ventana_mms_b, width=20, justify="center", font=("Lucida Sans", 10))
        self.entry_buscar_mms.place(x=170, y=379)

        # label
        self.lbl_valor = Label(self.ventana_mms_b, text="[buscar mensaje]", bg=(
            "#f0f0f0"), fg=("#151718"), font=("Lucida Sans", 10))
        self.lbl_valor.place(x=45, y=377)

        self.lbl_orden = Label(self.ventana_mms_b, text="[sistema de drones, mensaje, tiempo óptimo]", bg=(
            "#f0f0f0"), fg=("#151718"), font=("Lucida Sans", 10))
        self.lbl_orden.place(x=110, y=4)

        # botones
        btn_agregarNuevo = Button(self.ventana_mms_b, text="Seleccionar", command=self.seleccionar_mms_b,
                                  width=13, height=1, font=("Lucida Sans", 10), bg="#2c2e2f", foreground="white")
        btn_agregarNuevo.place(x=350, y=375)

        btn_verListado = Button(self.ventana_mms_b, text="Mostrar sistema", command=self.mostrar_sistema_drones_b,
                                width=13, height=1, font=("Lucida Sans", 10), bg="#2c2e2f", foreground="white")
        btn_verListado.place(x=80, y=412)

        btn_regresarMenu = Button(self.ventana_mms_b, text="Ver gráfica", command=self.ver_graficamente_mms_b,
                                  width=13, height=1, font=("Lucida Sans", 10), bg="#2c2e2f", foreground="white")
        btn_regresarMenu.place(x=200, y=412)

        btn_regresarMenu = Button(self.ventana_mms_b, text="Volver", command=self.__ir_pantalla_gestion_mms_a_desde_mms_b,
                                  width=13, height=1, font=("Lucida Sans", 10), bg="#2c2e2f", foreground="white")
        btn_regresarMenu.place(x=320, y=412)

    # funciones
    def seleccionar_mms_b(self):
        try:
            valor_en = self.entry_buscar_mms.get()
            while valor_en:
                if self.carga.lista_mms_solo.buscar_mms(valor_en):
                    self.valor_busqueda = valor_en
                    return
                break
        except Exception as e:  # mostrar mensaje
            print("Error", e)

    def mostrar_sistema_drones_b(self):
        try:
            self.scroll_ver_listado_ins.delete(1.0, tk.END)
            mms_a_buscar = self.valor_busqueda
            print(mms_a_buscar)
            msg_sistema = self.carga.lista_mms_sys.primero
            tamano_msg_sistema = self.carga.lista_mms_sys.size
            lista_mms_todo = self.carga.lista_mms_all.primero
            iterantes = self.carga.tamanos_reales.primero
            while msg_sistema:
                for i in range(tamano_msg_sistema):
                    if msg_sistema.dato.nombre_mms == mms_a_buscar:
                        # lista_mms_todo = lista_mms_todo.siguiente
                        self.scroll_ver_listado_ins.insert(
                            tk.END, f"  {msg_sistema.dato.mms_sys}" + "\n")
                        # while lista_mms_todo:
                        #     for i in range(iterantes.dato.size_nuevo):
                        #         if self.carga.lista_mms_all.buscar_nombre_mms(mms_a_buscar):
                        #             pass
                        break
                    msg_sistema = msg_sistema.siguiente
                break
        except Exception as e:  # mostrar mensaje
            print("Error", e)

    def ver_graficamente_mms_b(self):
        self.seleccionar_mms_b()

    def __ir_pantalla_gestion_mms_a_desde_mms_b(self):
        self.ventana_mms_b.destroy()
        self.gestion_de_mms_a_principal()

# ventana ayuda
    def ayuda_datos_documentacion(self):
        self.ventana_ayuda = Tk()
        self.ventana_ayuda.title("ayuda")
        self.ventana_ayuda.geometry("400x200")
        self.ventana_ayuda.config(background="#151718")
        self.centrar(self.ventana_ayuda, 400, 200)

        self.lbl_titulo = Label(self.ventana_ayuda, text="Introducción a la programación y computación 2", bg=(
            "#151718"), fg=("#f0f0f0"), font=("Lucida Sans", 10))
        self.lbl_titulo.place(x=50, y=20)

        self.lbl_datos = Label(self.ventana_ayuda, text="""
Ingeniería en ciencias y sistemas, 6to semestre
Nombres: Jennifer Yulissa Lourdes
Apellidos: Taperio manuel
Carnet: 202103763
""", bg=(
            "#151718"), fg=("#f0f0f0"), font=("Lucida Sans", 10))
        self.lbl_datos.place(x=50, y=40)

        # enlace a documentacion
        self.lbl_link = Label(self.ventana_ayuda, text="[enlace a documentación]", bg=(
            "#151718"), fg=("#f7ff19"), font=("Lucida Sans", 10, "underline"))
        self.lbl_link.place(x=115, y=130)
        self.lbl_link.bind("<Button-1>", lambda evento_link: webbrowser.open(
            "https://github.com/lurdesss/IPC2_Proyecto2_202103763/tree/main/DOCUMENTACION"))

        btn_regresarMenu = Button(self.ventana_ayuda, text="Volver a menu", command=self.__ir_pantalla_menu_desde_ayuda,
                                  width=13, height=1, font=("Lucida Sans", 10), bg="#f7ff19")
        btn_regresarMenu.place(x=145, y=160)

    def __ir_pantalla_menu_desde_ayuda(self):
        self.ventana_ayuda.destroy()
        self.principal()


# ver listados
class ScrollText(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = tk.Text(
            self,
            bg="#2c2e2f",
            foreground="#e8e8e8",
            insertbackground="#444546",
            selectbackground="#5b5d5d",
            width=49,
            height=20,
            font=("Courier New", 11),
        )
        self.scrollbar = tk.Scrollbar(
            self, orient=tk.VERTICAL, command=self.text.yview)
        self.text.configure(yscrollcommand=self.scrollbar.set)

        self.numberLines = TextLineNumbers(self, width=35, bg="#444546")
        self.numberLines.attach(self.text)

        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.numberLines.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
        self.text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.text.bind("<Key>", self.onPressDelay)
        self.text.bind("<Button-1>", self.numberLines.redraw)
        self.scrollbar.bind("<Button-1>", self.onScrollPress)
        self.text.bind("<MouseWheel>", self.onPressDelay)

    # funciones
    def onScrollPress(self, *args):
        self.scrollbar.bind("<B1-Motion>", self.numberLines.redraw)

    def onScrollRelease(self, *args):
        self.scrollbar.unbind("<B1-Motion>", self.numberLines.redraw)

    def onPressDelay(self, *args):
        self.after(2, self.numberLines.redraw)

    def get(self, *args, **kwargs):
        return self.text.get(*args, **kwargs)

    def insert(self, *args, **kwargs):
        return self.text.insert(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.text.delete(*args, **kwargs)

    def index(self, *args, **kwargs):
        return self.text.index(*args, **kwargs)

    def redraw(self):
        self.numberLines.redraw()


class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs, highlightthickness=0)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        """redraw line numbers"""
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True:
            dline = self.textwidget.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(
                2,
                y,
                anchor="nw",
                text=linenum,
                fill="#e8e8e8",
                font=("Courier New", 11, "bold"),
            )
            i = self.textwidget.index("%s+1line" % i)


Sistema()
