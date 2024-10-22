'''
    Para probar lo que he aprendido sobre el funcionamiento de los tipos de botones
    (botones normales, checkboxes y radiobuttons), haré una interfaz que pida ciertos datos
    al usuario con diferentes opciones y finalmente los imprime en pantalla
    Simple ¿verdad? :-)
'''
from tkinter import *
from tkinter import ttk

class Presentacion:
    def __init__(self, root):
        root.title('Presentacion')
        root.geometry('500x250')

        window = ttk.Frame(root, padding="3 3 12 12")
        window.grid(column=0, row=0, sticky=(N,W,E,S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ttk.Label(window, text='Presentacion personal', font='Calibri 16 bold').grid(column=1, row=0)

        self.nombre_var = StringVar()
        self.nombre_entrada = ttk.Entry(window, textvariable=self.nombre_var)
        self.nombre_entrada.grid(column=1, row=1)

        ttk.Label(window, text='Estado', font='bold').grid(column=0, row=2)
        ttk.Label(window, text='Deseos', font='bold').grid(column=2, row=2)

        #Solo se puede elegir una opcion
        self.radio_var = StringVar()
        ttk.Radiobutton(window, text='Soltero', value='Soltero', variable=self.radio_var).grid(column=0, row=3)
        ttk.Radiobutton(window, text='Casado', value='Casado', variable=self.radio_var).grid(column=0, row=4)
        ttk.Radiobutton(window, text='Complicado', value='Complicado', variable=self.radio_var).grid(column=0, row=5, sticky=('WE'))

        #Multiples opciones
        self.check1, self.check2, self.check3 = StringVar(), StringVar(), StringVar() #Se ve horrible
        ttk.Checkbutton(window, text='Riqueza', variable=self.check1, onvalue='Riqueza', offvalue='').grid(column=2, row=3)
        ttk.Checkbutton(window, text='Fama', variable=self.check2, onvalue='Fama', offvalue='').grid(column=2, row=4)
        ttk.Checkbutton(window, text='Poder', variable=self.check3, onvalue='Poder', offvalue='').grid(column=2, row=5)

        ttk.Button(window, text='Subir', command=self.presentar, width=15).grid(column=1, row=6)
        self.texto_final = StringVar()
        self.texto_final_label = ttk.Label(window, text="", font='Roboto 12 bold', textvariable=self.texto_final)
        self.texto_final_label.grid(column=1, row=7, pady=15)
        root.bind('<Return>', self.presentar)
    
    def validar(self):
        nombre = self.nombre_var.get()
        radio_valor = self.radio_var.get()
        check1 = self.check1.get()
        check2 = self.check2.get()
        check3 = self.check3.get()
        if not nombre:
            self.texto_final.set('Introduzca un nombre')
            return False
        elif not radio_valor:
            self.texto_final.set('Elija una de las opciones redondas')
            return False
        elif not check1 and not check2 and not check3:
            self.texto_final.set('Elija una o varias de\nlas opciones cuadradas')
            return False
        else:
            return True

    def presentar(self, extra=None):
        if not self.validar():
            return

        nombre = self.nombre_var.get()
        radio_valor = self.radio_var.get()
        check1 = self.check1.get()
        check2 = self.check2.get()
        check3 = self.check3.get()

        estado = {
            'Casado': 'sr/a',
            'Soltero': 'celibato'
        }.get(radio_valor, 'Don "Es complicado"')

        combinaciones = {
            (True, True, True): 'GOL D. ROGER',
            (True, True, False): 'José Mota!',
            (True, False, True): 'la autoridad',
            (False, True, True): 'El Rubius',
            (True, False, False): 'avaricioso',
            (False, True, False): 'vanaglorioso',
            (False, False, True): 'ambicioso'
        }
        
        deseo = combinaciones.get((bool(check1), bool(check2), bool(check3)), '')

        texto = f'Hola {estado} {nombre}!\nEres {deseo}'
        self.texto_final.set(texto)

root = Tk()
Presentacion(root)
root.mainloop()