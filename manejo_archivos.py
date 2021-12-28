'''Píldoras informáticas:
Archivos externos (video 37)'''


from io import open

archivo_texto=open("archivo.txt","w")

frase="Estupendo día para estudiar Python."

archivo_texto.write(frase)

archivo_texto.close()
