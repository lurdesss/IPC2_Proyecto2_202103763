from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox
import webbrowser
import sys
import os


class Sistema():
    def __init__(self):
        self.principal()
        self.ventana.title("sistema de drones")
        self.centrar(self.ventana, 420, 320)
        self.ventana.geometry("420x320")
        self.frame()

    def principal(self):
        self.ventana = Tk()
        self.ventana.resizable(0, 0)
        self.ventana.config(bg="#2c2e2f", bd=5)

    def centrar(self, ventana, ancho, alto):
        altura_pantalla = ventana.winfo_screenheight()
        ancho_pantalla = ventana.winfo_screenwidth()
        ancho_x = (ancho_pantalla//2) - (ancho//2)
        altura_y = (altura_pantalla//2) - (alto//2)
        ventana.geometry(f"+{ancho_x}+{altura_y}")

    def frame(self):
        self.frame = Frame()
        self.frame.pack(side=BOTTOM)
        self.frame.config(bg="#2c2e2f", width="420",
                          height="320")

        # Aside
        Button(self.frame, text="Cargar archivo XML", command=self.cargar_archivo,
               width=30, height=1, font=("Lucida Sans", 12), background='#151718',
               foreground='#F5F5F5', activeforeground='black', activebackground='gray52').place(x=50, y=40)
        Button(self.frame, text="Generar archivo XML", command=self.generar_archivo,
               width=30, height=1, font=("Lucida Sans", 12), background='#151718',
               foreground='#F5F5F5', activeforeground='black', activebackground='gray52').place(x=50, y=80)
        Button(self.frame, text="Gestión de drones", command=self.gestionar_dron,
               width=30, height=1, font=("Lucida Sans", 12), background='#151718',
               foreground='#F5F5F5', activeforeground='black', activebackground='gray52').place(x=50, y=120)
        Button(self.frame, text="Gestión de sistema de drones", command=self.gestionar_sistema_dron,
               width=30, height=1, font=("Lucida Sans", 12), background='#151718',
               foreground='#F5F5F5', activeforeground='black', activebackground='gray52').place(x=50, y=160)
        Button(self.frame, text="Gestión de mensajes", command=self.gestionar_mensaje,
               width=30, height=1, font=("Lucida Sans", 12), background='#151718',
               foreground='#F5F5F5', activeforeground='black', activebackground='gray52').place(x=50, y=200)
        # Opciones
        Button(self.frame, text="Inicializar", command=self.inicializar,
               width=14, height=1, font=("Lucida Sans", 12), background='#f7ff19',
               foreground='black', activeforeground='black', activebackground='gray52').place(x=50, y=240)
        Button(self.frame, text="Ayuda", command=self.ayuda,
               width=14, height=1, font=("Lucida Sans", 12), background='#f7ff19',
               foreground='black', activeforeground='black', activebackground='gray52').place(x=210, y=240)

        self.frame.mainloop()

    # funciones
    # def salir_archivo(self):
    #     sys.exit(0)
    def inicializar(self):  # INCISO A
        python = sys.executable
        os.execl(python, python, * sys.argv)

    def cargar_archivo(self, ruta):  # INCISO B
        self.ventana.destroy()
        CargarArchivo()

    def generar_archivo(self):  # INCISO C
        self.ventana.destroy()

    def gestionar_dron(self):  # INCISO D
        self.ventana.destroy()
        GestionarDrones()

    def gestionar_sistema_dron(self):  # INCISO E
        pass

    def gestionar_mensaje(self):  # INCISO F
        self.ventana.destroy()
        GestionarMensajesA()

    def ayuda(self):  # INCISO G
        self.ventana.destroy()
        AyudaMostrarDatos()


class CargarArchivo():  # archivo XML entrada
    pass


class GenerarArchivo():  # archivo XML salida
    pass


class GestionarSistemaDeDrones():  # archivo de graphviz
    pass


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


class GestionarDrones(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("gestión de drones")
        self.geometry("510x450")
        self.config(background="#f0f0f0")
        self.centrar(self, 510, 450)
        # self.resizable(0, 0)
        # self.overrideredirect(True)
        self.scroll_ver_listado = ScrollText(self)
        self.scroll_ver_listado.place(x=5, y=26)
        self.after(200, self.scroll_ver_listado.redraw())

        # entry
        self.entry_agregar = Entry(
            self, width=20, justify="center", font=("Lucida Sans", 10))
        self.entry_agregar.place(x=170, y=379)

        # label
        self.lbl_valor = Label(self, text="[valor alfanumérico]", bg=(
            "#f0f0f0"), fg=("#151718"), font=("Lucida Sans", 10))
        self.lbl_valor.place(x=35, y=377)

        self.lbl_orden = Label(self, text="[drones en sistema]", bg=(
            "#f0f0f0"), fg=("#151718"), font=("Lucida Sans", 10))
        self.lbl_orden.place(x=185, y=4)

        # botones
        btn_agregarNuevo = Button(self, text="Agregar nuevo", command=self.agregar_nuevo,
                                  width=13, height=1, font=("Lucida Sans", 10), bg="#2c2e2f", foreground="white")
        btn_agregarNuevo.place(x=350, y=375)

        btn_verListado = Button(self, text="Ver listado", command=self.ver_listado_drones,
                                width=13, height=1, font=("Lucida Sans", 10), bg="#f7ff19")
        btn_verListado.place(x=140, y=412)

        btn_regresarMenu = Button(self, text="Volver a menu", command=self.__ir_pantalla_menu,
                                  width=13, height=1, font=("Lucida Sans", 10), bg="#f7ff19")
        btn_regresarMenu.place(x=260, y=412)

    # funciones
    def centrar(self, ventana, ancho, alto):  # centra la ventana
        altura_pantalla = ventana.winfo_screenheight()
        ancho_pantalla = ventana.winfo_screenwidth()
        ancho_x = (ancho_pantalla//2) - (ancho//2)
        altura_y = (altura_pantalla//2) - (alto//2)
        ventana.geometry(f"+{ancho_x}+{altura_y}")

    def ver_listado_drones(self):
        pass

    def agregar_nuevo(self):
        pass

    def __ir_pantalla_menu(self):
        self.destroy()
        Sistema()


class GestionarMensajesA(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("gestión de mensajes")
        self.geometry("510x415")
        self.config(background="#f0f0f0")
        self.centrar(self, 510, 415)
        # self.resizable(0, 0)
        # self.overrideredirect(True)
        self.scroll_ver_listado = ScrollText(self)
        self.scroll_ver_listado.place(x=5, y=26)
        self.after(200, self.scroll_ver_listado.redraw())

        # label
        self.lbl_orden = Label(self, text="[mensajes e instrucciones]", bg=(
            "#f0f0f0"), fg=("#151718"), font=("Lucida Sans", 10))
        self.lbl_orden.place(x=150, y=4)

        # botones
        btn_verListado = Button(self, text="Ver listado", command=self.ver_listado_drones,
                                width=13, height=1, font=("Lucida Sans", 10), bg="#f7ff19")
        btn_verListado.place(x=80, y=375)

        btn_agregarNuevo = Button(self, text="Ver instruccion", command=self.ver_instrucciones,
                                  width=13, height=1, font=("Lucida Sans", 10), bg="#2c2e2f", foreground="white")
        btn_agregarNuevo.place(x=200, y=375)

        btn_regresarMenu = Button(self, text="Volver a menu", command=self.__ir_pantalla_menu,
                                  width=13, height=1, font=("Lucida Sans", 10), bg="#f7ff19")
        btn_regresarMenu.place(x=320, y=375)

    # funciones
    def centrar(self, ventana, ancho, alto):  # centra la ventana
        altura_pantalla = ventana.winfo_screenheight()
        ancho_pantalla = ventana.winfo_screenwidth()
        ancho_x = (ancho_pantalla//2) - (ancho//2)
        altura_y = (altura_pantalla//2) - (alto//2)
        ventana.geometry(f"+{ancho_x}+{altura_y}")

    def ver_listado_drones(self):
        pass

    def ver_instrucciones(self):
        self.destroy()
        GestionarMensajesB()

    def __ir_pantalla_menu(self):
        self.destroy()
        Sistema()


class GestionarMensajesB(tk.Tk):  # para un mms en el sistema
    def __init__(self):
        super().__init__()
        self.title("gestión de mensajes")
        self.geometry("510x450")
        self.config(background="#f0f0f0")
        self.centrar(self, 510, 450)
        # self.resizable(0, 0)
        # self.overrideredirect(True)
        self.scroll_ver_listado = ScrollText(self)
        self.scroll_ver_listado.place(x=5, y=26)
        self.after(200, self.scroll_ver_listado.redraw())

        # combobox
        self.opciones = ["Opción 1", "Opción 2",
                         "Opción 3"]  # lista doblemente enlazada
        self.combobox_t = ttk.Combobox(
            state="readonly", values=self.opciones, width=25)
        self.combobox_t.place(x=170, y=378)

        # # OptionMenu
        # self.var = tk.StringVar(self)
        # self.var.set('mms')
        # self.opciones = [
        #     "Opción 1", "Opción 2", "Opción 3"]
        # self.desplegable_seleccion = tk.OptionMenu(
        #     self, self.var, *self.opciones)
        # self.desplegable_seleccion.config(
        #     width=20, background='#2b2b2b',
        #     foreground='white', activeforeground='black', activebackground='gray52')
        # self.desplegable_seleccion.place(x=170, y=375)

        # # entry
        # self.entry_agregar = Entry(
        #     self, width=20, justify="center", font=("Lucida Sans", 10))
        # self.entry_agregar.place(x=170, y=379)

        # label
        self.lbl_valor = Label(self, text="[mensaje a mostrar]", bg=(
            "#f0f0f0"), fg=("#151718"), font=("Lucida Sans", 10))
        self.lbl_valor.place(x=35, y=377)

        self.lbl_orden = Label(self, text="[sistema de drones, mensaje, tiempo óptimo]", bg=(
            "#f0f0f0"), fg=("#151718"), font=("Lucida Sans", 10))
        self.lbl_orden.place(x=110, y=4)

        # botones
        btn_agregarNuevo = Button(self, text="Seleccionar", command=self.seleccionar_mms,
                                  width=13, height=1, font=("Lucida Sans", 10), bg="#2c2e2f", foreground="white")
        btn_agregarNuevo.place(x=350, y=375)

        btn_verListado = Button(self, text="Mostrar sistema", command=self.mostrar_sistema_drones,
                                width=13, height=1, font=("Lucida Sans", 10), bg="#f7ff19")
        btn_verListado.place(x=80, y=412)

        btn_regresarMenu = Button(self, text="Ver gráfica", command=self.ver_graficamente,
                                  width=13, height=1, font=("Lucida Sans", 10), bg="#f7ff19")
        btn_regresarMenu.place(x=200, y=412)

        btn_regresarMenu = Button(self, text="Volver", command=self.__ir_pantalla_gestion,
                                  width=13, height=1, font=("Lucida Sans", 10), bg="#f7ff19")
        btn_regresarMenu.place(x=320, y=412)

    # funciones
    def centrar(self, ventana, ancho, alto):  # centra la ventana
        altura_pantalla = ventana.winfo_screenheight()
        ancho_pantalla = ventana.winfo_screenwidth()
        ancho_x = (ancho_pantalla//2) - (ancho//2)
        altura_y = (altura_pantalla//2) - (alto//2)
        ventana.geometry(f"+{ancho_x}+{altura_y}")

    def seleccionar_mms(self):
        # get from combobox
        pass

    def mostrar_sistema_drones(self):
        pass

    def ver_graficamente(self):
        pass

    def __ir_pantalla_gestion(self):
        self.destroy()
        GestionarMensajesA()


class AyudaMostrarDatos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ayuda")
        self.geometry("400x200")
        self.config(background="#151718")
        self.centrar(self, 400, 200)

        self.lbl_titulo = Label(self, text="Introducción a la programación y computación 2", bg=(
            "#151718"), fg=("#f0f0f0"), font=("Lucida Sans", 10))
        self.lbl_titulo.place(x=50, y=20)

        self.lbl_datos = Label(self, text="""
Ingeniería en ciencias y sistemas, 6to semestre
Nombres: Jennifer Yulissa Lourdes
Apellidos: Taperio manuel
Carnet: 202103763
""", bg=(
            "#151718"), fg=("#f0f0f0"), font=("Lucida Sans", 10))
        self.lbl_datos.place(x=50, y=40)

        # enlace a documentacion
        self.lbl_link = Label(self, text="[enlace a documentación]", bg=(
            "#151718"), fg=("#f7ff19"), font=("Lucida Sans", 10, "underline"))
        self.lbl_link.place(x=115, y=130)
        self.lbl_link.bind("<Button-1>", lambda evento_link: webbrowser.open(
            "https://github.com/lurdesss/IPC2_Proyecto2_202103763"))

        btn_regresarMenu = Button(self, text="Volver a menu", command=self.__ir_pantalla_menu,
                                  width=13, height=1, font=("Lucida Sans", 10), bg="#f7ff19")
        btn_regresarMenu.place(x=145, y=160)

    def centrar(self, ventana, ancho, alto):  # centra la ventana
        altura_pantalla = ventana.winfo_screenheight()
        ancho_pantalla = ventana.winfo_screenwidth()
        ancho_x = (ancho_pantalla//2) - (ancho//2)
        altura_y = (altura_pantalla//2) - (alto//2)
        ventana.geometry(f"+{ancho_x}+{altura_y}")

    def __ir_pantalla_menu(self):
        self.destroy()
        Sistema()


Sistema()
