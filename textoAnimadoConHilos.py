import tkinter as tk
from tkinter import ttk
import time
import threading

main_window = tk.Tk()
main_window.title("Ejemplo")
main_window.configure(width=350, height=200)


def createLabel(a, b):
    label = ttk.Label(text="")
    label.place(x=a, y=b)
    return label


def crearAnimacion(a, b, char):
    mylabel = createLabel(a, b)
    texto = ""
    retardo: float = 0.25
    for i in range(0, 35):
        time.sleep(retardo)
        texto += char
        mylabel.config(text=texto)
        main_window.update_idletasks()
        main_window.update()


def opcionFinalizar():
    boton = ttk.Button(main_window, text="Salir", command=main_window.destroy)
    boton.place(x=170, y=170)


thread_1 = threading.Thread(target=crearAnimacion, args=(10, 10, 'A'))
thread_2 = threading.Thread(target=crearAnimacion, args=(10, 30, 'B'))
thread_3 = threading.Thread(target=crearAnimacion, args=(10, 50, 'C'))

thread_1.start()
thread_2.start()
thread_3.start()

opcionFinalizar()

main_window.mainloop()
