# Pildoras informaticas / Interfaces gráficas I. Vídeo 42 y 43

from tkinter import *

raiz = Tk() #Crea la ventana gráfica.
raiz.title("Ventana de pruebas") #titulo de la ventana.
#raiz.resizable(0,0) #Para impedir redimensionar la ventana (ancho, alto).
raiz.iconbitmap("") #Para cambiar el icono de la ventana.
#raiz.geometry("340x380") #Tamaño de la ventana ("anchoxalto").
raiz.config(bg="blue") #Color de la ventana (bg="color")
miFrame = Frame()
miFrame.pack(side="right", anchor="n")
miFrame.config(bg="green")
miFrame.config(width="650", height="350")
miFrame.config(bd=35)
miFrame.config(relief="sunken")
miFrame.config(cursor="pirate")
raiz.mainloop() #Esta intrucción siempre debe ir a lo último.