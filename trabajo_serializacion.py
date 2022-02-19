#Curso Python. Serialización I. Vídeo 39 - Píldoras informáticas.

import pickle

'''lista_nombres=["Pedro", "Ana","María", "Isabel"]

#Creando un fichero externo binario y agregando la lista:
fichero_binario=open("lista_nombres","wb") #("wb") es escritura binaria.

#Volcado de la lista a ese fichero externo:
pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

#Borra el alchivo de la memoria:
del (fichero_binario)'''

#Crea un archivo en memoria;
fichero=open("lista_nombres","rb") #("rb") lee la información binaria.

#Para guardar la información del archivo en una variable (fichero);
lista=pickle.load(fichero) #El método "load" carga la información.

print(lista)