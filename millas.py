from tkinter import *
from ttkbootstrap import ttk

def milla_a_km():
    try:
        calculo_km = str(float(millas.get() * 1.609344))
        km.set(calculo_km)
    except:
        km.set("Entrada invalida")

#Ventana principal
root = Tk()
root.title('Demo')
root.geometry('250x200') #ancho x alto

#Marco principal (Widget que incluye todo)
mainframe = ttk.Frame(master= root)
mainframe.pack(fill=BOTH, expand=True)

#Titulo principal
title_intern = ttk.Label(master= mainframe, text= 'De millas a km', font='Roboto 21 bold')
title_intern.pack()

#Valor de entrada
millas = IntVar()
entrada_millas = ttk.Entry(master=mainframe, width=10, textvariable=millas)
boton_convertir = ttk.Button(master=mainframe, text="Convertir", command=milla_a_km)
entrada_millas.pack()
boton_convertir.pack(side='top', pady=5)

'''
# Lista de opciones para el Combobox
opciones = ["Opción 1", "Opción 2", "Opción 3"]
# Variable para almacenar la opción seleccionada
opcion_seleccionada = StringVar()
# Crear el Combobox
combobox = ttk.Combobox(mainframe, textvariable=opcion_seleccionada, values=opciones, state='readonly')
combobox.pack(pady=(10, 0))  # Empaquetar el Combobox con un margen superior de 10 píxeles
'''


#texto final
km = StringVar()
entrada_km = ttk.Label(mainframe, text="", font='Calibri 12 bold', textvariable=km)
entrada_km.pack(pady=20)

#Mostrar ventana principal
root.mainloop()