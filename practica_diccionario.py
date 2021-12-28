#Píldoras informáticas.
#Curso Python. Sintaxis Básica VII Los diccionarios. Vídeo 9

#Los países y sus capitales:
midiccionario = {"Alemania":"Berlín", "Francia":"París", "Reino Unido":"Londres", "España":"Madrid"}

#Imprime la capital de Francia, en este caso:
#print(midiccionario["Francia"])

#Agregar un elemento al diccionario:
midiccionario["Italia"]="Roma"

#Para eliminar un elemento:
del midiccionario["Italia"]

#imprime el diccionario completo:
print(midiccionario)

#Convertir una tupla en diccionario:
mitupla=["España", "Francia", "Reino Unido", "Alemania"]
otrodiccionario={mitupla[0]:"Madrid", mitupla[1]:"Paris", mitupla[2]:"Londres", mitupla[3]:"Berlín"}
print(otrodiccionario)

#Diccionario con una tupla en su interior:
diccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":[1991,1992,1993,1996,1997,1998] }
print(diccionario["anillos"])

print(diccionario.keys()) #Imprime las claves del diccionario.
print(diccionario.values()) #Imprime los valores del diccionario.
print(len(diccionario)) #Imprime la longitud del diccionario.