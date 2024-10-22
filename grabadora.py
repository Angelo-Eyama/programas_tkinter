from tkinter import * 
from tkinter import ttk
import sounddevice, winsound
from scipy.io.wavfile import write

nombre_fichero = 'salida.wav'

#Ventana principal
window = Tk()
window.title('Grabadora de sonidos')
window.geometry('300x350')

#funciones
def verificarSegundos():
    try:
        valor_segundos = int(segundos.get())
        if valor_segundos <= 0:
            salida.set('Introduzca un numero entero mayor que 0')
        else:
            #salida.set(f'Audio de {valor_segundos} s')
            valor_segundos+=1
            grabarSonido(valor_segundos)
    except TclError:
        salida.set('Introduzca solo valores numericos')

def grabarSonido(segundos):
    FRECUENCIA = 44100
    grabacion = sounddevice.rec( int(segundos * FRECUENCIA), samplerate=FRECUENCIA, channels=2)
    entrada.config(state=DISABLED)
    salida.set('Grabando...')
    sounddevice.wait()
    write(nombre_fichero, FRECUENCIA, grabacion)
    salida.set('Grabacion finalizada')
    entrada.config(state=NORMAL)

def reproducirSonido():
    salida.set('Reproduciendo...')
    winsound.PlaySound(nombre_fichero, winsound.SND_FILENAME | winsound.SND_ASYNC)
    salida.set('Fin de reproduccion')

#Creacion widgets
segundos = IntVar()
ttk.Label(window, text='Introduzca la duracion de la grabacion en segundos', background='red').pack()
entrada = ttk.Entry(window, textvariable=segundos)
grabar_boton = ttk.Button(window, text='Grabar', command=verificarSegundos)
reproducir_boton = ttk.Button(window, text='Reproducir', command=reproducirSonido)

#Colocacion widgets
entrada.pack()
grabar_boton.pack()
reproducir_boton.pack()

salida = StringVar()
texto = ttk.Label(window, textvariable=salida)
texto.pack()

#Iniciar aplicacion
window.mainloop()