'''Píldoras informáticas:
Archivos externos (video 37)'''

#Importa el módulo io:
from io import open

#Crea un archivo de texto,vacío (en modo escritura):
#archivo_texto=open("archivo.txt","w")

#frase="Estupendo día para estudiar Python\nun sábado."

#Con el método write se agrega el texto de la variable frase
#archivo_texto.write(frase)

#Abriendo el archivo en modo lectura:
#archivo_texto=open("archivo.txt","r")

#Para que lea lo que hay dentro del archivo y lo guarde en la variable:
#texto=archivo_texto.read()

#print(texto)

#Lee lo que hay en el archivo y lo convierte en una lista:
#lineas_texto=archivo_texto.readlines()

#print(lineas_texto[0])

#Para poder agregar texto en el archivo(método append):
#archivo_texto=open("archivo.txt","a")

#archivo_texto.write("\nsiempre es una buena ocasión para estudiar.")

#print(archivo_texto.read())

#Para que desplace el puntero a la posición 0:
#archivo_texto.seek(0)

#Imprime hasta dicha posición:
#print(archivo_texto.read(11))

#Para obtener la mitad de la longitud del texto:

#Lectura y escritura:
archivo_texto=open("archivo.txt","r+")

archivo_texto.seek(len(archivo_texto.read())/2)

print(archivo_texto.read())

archivo_texto.close()
