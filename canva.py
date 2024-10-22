from tkinter import *
from tkinter import ttk
tam_pincel = 7
color = 'black'
def dibujar(event):
    global color
    x = event.x
    y = event.y
    canva.create_oval((x-(tam_pincel/2),y-(tam_pincel/2),x+(tam_pincel/2),y+(tam_pincel/2)), fill=color, outline=color)

def ajustar_pincel(event):
    delta = event.delta
    global tam_pincel
    if delta > 0:
        tam_pincel+=4
    else:
        tam_pincel-=4

    #Ajustamos el rango de tamaños posibles
    tam_pincel = max(0, min(tam_pincel, 40))

def cambiarColor(nuevo_color):
    global color
    color = nuevo_color

#Configuraciones iniciales de la ventana y widget principal
root = Tk()
root.geometry('450x300')
window = ttk.Frame(root)
window.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canva = Canvas(window, bg='gray', height=200, width=400)
canva.pack()
canva.bind('<MouseWheel>', lambda event: ajustar_pincel(event))
canva.bind('<Motion>', lambda event: dibujar(event))

# Creo un Frame que contiene los tres botones
button_frame = ttk.Frame(window)
button_frame.pack(pady=(15,5))

green_button = ttk.Button(button_frame, text='Verde')
red_button = ttk.Button(button_frame, text='Rojo')
blue_button = ttk.Button(button_frame, text='Azul')
black_button = ttk.Button(button_frame, text='Negro')

#Cambiamos los colores segun se pulsa
green_button.bind('<Button>', lambda event: cambiarColor('green'))
red_button.bind('<Button>', lambda event: cambiarColor('red'))
blue_button.bind('<Button>', lambda event: cambiarColor('blue'))
black_button.bind('<Button>', lambda event: cambiarColor('black'))

green_button.pack(side='left', padx=(0,5))
red_button.pack(side='left', padx=5)
blue_button.pack(side='left', padx=5)
black_button.pack(side='left', padx=5)

clear_button = ttk.Button(window, text='Reiniciar')
clear_button.bind('<Button>', lambda event: (canva.delete('all'), canva.config(bg='gray'), cambiarColor('black')))
clear_button.pack()

root.mainloop()