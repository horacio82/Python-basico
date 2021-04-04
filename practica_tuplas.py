#Píldoras informáticas.
#Curso Python. Sintaxis Básica VI. Las tuplas. Vídeo 8


mitupla=("Juan", 13, 1, 1995)
milista1=["Horacio", "Molinari"]

#list convierte una tupla en una lista:
milista=list(mitupla)

#tuple convierte una lista en una tupla:
mitupla1=tuple(milista1)

#Imprime true o false si dicho elemento se encuentra:
#print(13 in mitupla)

#Método que imprime la cantidad de veces que se encuentra dicho elemento:
#print(mitupla.count(13))

#Método que imprime la cantidad de elementos:
print(len(mitupla))

#Tupla unitaria
otratupla=("Andrés",)

#Nota: las tuplas tambien se pueden declarar sin parentesis, aunque no es muy recomendable.
#se lo conoce como empaquetado.

#Tambien está el desempaquetado de tuplas:
tupla=("Pepe", 15, 5, 2008)
nombre, dia, mes, año=tupla

#Concatenar strings:
print("Nombre: " +nombre)

#Convertir números en strings para concatenar:
print("Día: "+ str(dia))
print("Mes: "+ str(mes))

#Concatenar texto y números:
print("Año:" ,año)