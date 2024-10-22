from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry('600x400')
window.title('Menu')

menu = Menu(window)

#Sub menú
file_menu = Menu(menu, tearoff= False)
file_menu.add_command(label= 'Nuevo', command=lambda:print('Opcion: Nuevo') )
file_menu.add_command(label= 'Abrir', command=lambda:print('Opcion: Abrir') )

#Sub menu 2
check = StringVar()
help_menu = Menu(menu, tearoff= False)
help_menu.add_command(label= 'Ayuda', command=lambda:print(f"Check: {check.get()}") )
help_menu.add_checkbutton(label='Check', onvalue='On', offvalue='Off', variable=check)

#Insertar en menú
menu.add_cascade(label='Archivo', menu= file_menu)
menu.add_cascade(label='Ayuda', menu= help_menu)

#Mas informacion: tutorialspoint.com/python/tk_menu.htm
exercise_menu = Menu(menu, tearoff=False)
exercise_menu.add_command(label= 'Exercise test')
menu.add_cascade(label='Exercise', menu = exercise_menu)

#Submenu dentro del menu del ejercicio
exercise_sub_menu = Menu(exercise_menu, tearoff=False)
exercise_sub_menu.add_command(label= 'Exercise sub menu test')
exercise_menu.add_cascade(label='otros...', menu=exercise_sub_menu)

#Botón de menú en pantalla
menu_button = ttk.Menubutton(window, text='Menu')
menu_button.pack()

#Sub menú en pantalla (dentro del menu_button)
sub_menu = Menu(menu_button, tearoff=False)
sub_menu.add_command(label='Opcion 1', command= lambda: print('Opcion 1'))
menu_button.config(menu= sub_menu)


window.configure(menu=menu) #Equivalente de pack()
window.mainloop()