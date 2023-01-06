import random
import sys
import tkinter
from tkinter import ttk, messagebox

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

def salir(event):
    window.quit()

def mostrar_seleccion():
    # Obtener la opción seleccionada.
    seleccion = combo.get()
    messagebox.showinfo(
        message=f"La opción seleccionada es: {seleccion}",
        title="Selección"
    )

label1 = ttk.Label(window, text="Lista Paises Suramerica:")
label1.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

lista = ['Argentina', 'Brasil', 'Colombia', 'Ecuador', 'Chile', 'Peru', 'Uruaguay']
lista_items = tkinter.StringVar(value=lista)

combo = ttk.Combobox(window, state="readonly", values=lista)
combo.grid(column=1, row=1, sticky=tkinter.W, padx=5, pady=5)

button = ttk.Button(window, text="Mostrar selección", command=mostrar_seleccion)
button.grid(column=1, row=2, sticky=tkinter.W, padx=5, pady=5)

botonSalir = tkinter.Button(window, text='Salir')
botonSalir.grid(column=2, row=2, sticky=tkinter.E, padx=15, pady=15)
botonSalir.bind('<Button-1>', salir)

window.mainloop()