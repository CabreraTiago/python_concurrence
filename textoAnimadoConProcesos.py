import tkinter as tk
from tkinter import ttk
import time
import multiprocessing

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


if __name__ == '__main__':
    process_1 = multiprocessing.Process(target=crearAnimacion, args=(10, 10, 'A'))
    process_2 = multiprocessing.Process(target=crearAnimacion, args=(10, 30, 'B'))
    process_3 = multiprocessing.Process(target=crearAnimacion, args=(10, 50, 'C'))

    process_1.start()
    process_2.start()
    process_3.start()
    process_1.join()
    process_2.join()
    process_3.join()

opcionFinalizar()

main_window.mainloop()
