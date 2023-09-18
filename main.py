from tkinter import *
from tkinter import messagebox


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
        self.ventana.config(bg="#151718", bd=5)

    def centrar(self, ventana, ancho, alto):
        altura_pantalla = ventana.winfo_screenheight()
        ancho_pantalla = ventana.winfo_screenwidth()
        ancho_x = (ancho_pantalla//2) - (ancho//2)
        altura_y = (altura_pantalla//2) - (alto//2)
        ventana.geometry(f"+{ancho_x}+{altura_y}")

    # funciones
    def inicializar(self):
        pass

    def cargar_archivo(self, ruta):
        pass

    def frame(self):
        self.frame = Frame()
        self.frame.pack(side=BOTTOM)
        self.frame.config(bg="#151718", width="420",
                          height="320")
        # labels
        # Label(self.frame, text="IPC2 proyecto2", bg="#2b2b2b", fg=("white"),
        #       font=("Helvetica", 16)).place(x=140, y=15)

        # Aside
        Button(self.frame, text="Cargar archivo XML", command=self.inicializar,
               width=30, height=1, font=("Lucida Sans", 12), background='#1c1c1d',
               foreground='#ecedee', activeforeground='black', activebackground='gray52').place(x=50, y=40)
        Button(self.frame, text="Generar archivo XML", command=self.inicializar,
               width=30, height=1, font=("Lucida Sans", 12), background='#1c1c1d',
               foreground='#ecedee', activeforeground='black', activebackground='gray52').place(x=50, y=80)
        Button(self.frame, text="Gestión de drones", command=self.inicializar,
               width=30, height=1, font=("Lucida Sans", 12), background='#1c1c1d',
               foreground='#ecedee', activeforeground='black', activebackground='gray52').place(x=50, y=120)
        Button(self.frame, text="Gestión de sistema de drones", command=self.inicializar,
               width=30, height=1, font=("Lucida Sans", 12), background='#1c1c1d',
               foreground='#ecedee', activeforeground='black', activebackground='gray52').place(x=50, y=160)
        Button(self.frame, text="Gestión de mensajes", command=self.inicializar,
               width=30, height=1, font=("Lucida Sans", 12), background='#1c1c1d',
               foreground='#ecedee', activeforeground='black', activebackground='gray52').place(x=50, y=200)
        # Opciones
        Button(self.frame, text="Inicializar", command=self.inicializar,
               width=14, height=1, font=("Lucida Sans", 12), background='#f7ff19',
               foreground='black', activeforeground='black', activebackground='gray52').place(x=50, y=240)
        Button(self.frame, text="Ayuda", command=self.inicializar,
               width=14, height=1, font=("Lucida Sans", 12), background='#f7ff19',
               foreground='black', activeforeground='black', activebackground='gray52').place(x=210, y=240)

        self.frame.mainloop()


class CargarArchivo(Sistema):
    def __init__(self):
        super().principal()
        self.ventana.title("Cargar Archivo")
        super().centrar(self.ventana, 420, 160)
        self.ventana.geometry("420x160")
        self.frame()

    def btn_regresar(self):
        self.ventana.destroy()
        Sistema()


Sistema()
