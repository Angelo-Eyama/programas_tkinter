#Crear exe: pyinstaller --onefile --icon=img/swap.ico --add-data "img;img" conversor.py
#Ejecutar directamente: py conversor.py
from tkinter import *
from ttkbootstrap import ttk
from PIL import Image, ImageTk
import subprocess

class Conversor:
    def __init__(self, root):
        #Ventana de aplicacion
        root.title('Demo')
        root.geometry('600x200')

        #Ventana principal
        mainframe = ttk.Frame(master=root) #Por ahora, sin padding
        mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        #Titulo
        ttk.Label(master=mainframe, text="Conversor de medidas", font="Calibri 16 bold").grid(column=1, row=0, padx=30, sticky='E')
        
        #Entrada de unidad
        self.valor_entrada = DoubleVar()
        self.entrada = ttk.Entry(master=mainframe, width=16, textvariable=self.valor_entrada)
        self.entrada.grid(column=1, row=1)

        #Texto para el usuario
        ttk.Label(master=mainframe,text="De", font='Calibri 12').grid(column=0, row=2)
        ttk.Label(master=mainframe,text="A", font='Calibri 12').grid(column=2, row=2)

        #Desplegables
        self.valor_desplegable_entrada = StringVar()
        self.valor_desplegable_salida = StringVar()
        opciones = [ 'toneladas(t)', 'quintales(q)', 'miriagramos(mag)', 'kilogramos(kg)','hectogramos(hg)', 
                        'decagramos(dag)', 'gramos(g)', 'decigramos(dg)', 'centigramos(cg)', 'miligramos(mg)']
        self.desplegable_entrada = ttk.Combobox(master=mainframe, textvariable=self.valor_desplegable_entrada, values=opciones, state='readonly')
        self.desplegable_salida = ttk.Combobox(master=mainframe, textvariable=self.valor_desplegable_salida, values=opciones, state='readonly')
        self.desplegable_entrada.grid(column=0, row=3, padx=8)
        self.desplegable_salida.grid(column=2,row=3)

        
        self.boton_convertir = ttk.Button(master=mainframe, text='Convertir', command=self.convertir)
        self.boton_convertir.grid(column=1,row=4, pady=10)

        #Boton intercambiar
        imagen = Image.open('img\\swap.png')
        imagen = imagen.resize((15, 20), Image.Resampling.LANCZOS)
        self.img_swap = ImageTk.PhotoImage(imagen)
        self.boton_intercambiar = ttk.Button(master=mainframe,image=self.img_swap, command= self.intercambiar, bootstyle='outline')
        self.boton_intercambiar.grid(column=1, row=3)

        #Salida de texto
        self.valor_salida = StringVar()
        self.salida = ttk.Label(master=mainframe, text="", textvariable=self.valor_salida, font='Calibri 12 bold').grid(column=1, row=5)

        #Configuracion adicional: Al pulsar enter, se llama a la funcion convertir
        root.bind('<Return>', self.convertir)

    def convertir(self, *args):

        unidades = {
        'toneladas(t)': 10e6,
        'quintales(q)': 105,
        'miriagramos(mag)': 10e4,
        'kilogramos(kg)': 10e3,
        'hectogramos(hg)': 10e2,
        'decagramos(dg)': 10e1,
        'gramos(g)': 1,
        'decigramos(dg)': 10e-1, 
        'centigramos(cg)':10e-2, 
        'miligramos(mg)': 10e-3
        }

        unidad_entrada = self.valor_desplegable_entrada.get()
        unidad_salida = self.valor_desplegable_salida.get()
        if not unidad_entrada or not unidad_salida:
            self.valor_salida.set("Introduzca una medida de entrada/salida")
        else:
            try:
                str(self.valor_entrada.get())
            except:
                self.valor_salida.set("Solo se permiten números")
            else:
                a_gramos = float(self.valor_entrada.get()) * unidades.get(unidad_entrada)
                conversion_final = a_gramos / unidades.get(unidad_salida)
                salida = str(conversion_final) +" "+ unidad_salida
                self.valor_salida.set(salida)

    def intercambiar(self):
        temp = self.valor_desplegable_entrada.get()
        self.valor_desplegable_entrada.set(self.valor_desplegable_salida.get())
        self.valor_desplegable_salida.set( temp)

root = Tk()
Conversor(root)
root.mainloop()