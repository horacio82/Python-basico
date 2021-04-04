#Píldoras Informáticas.
#Curso Python. Sintaxis Básica VII Los diccionarios. Vídeo 9


#midiccionario = {"Argentina":"Buenos Aires", "Maradona":10,}
#print(midiccionario)

#Utilizar una tupla para asignar valores:
mitupla=["España", "Francia", "Argentina"]
diccionario={mitupla[0]:"Madrid", mitupla[1]:"Paris", mitupla[2]:"Buenos Aires"}
print(diccionario)

#Tupla almacenada dentro del diccionario:
diccio={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":[1991,1992,1993,1996,1997,1998]}


#Diccionario dentro de otro diccionario:
diccio={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}

#Imprime las claves:
print(diccio.keys())
#Imprime los valores:
print(diccio.values())
#Imprime la longitud del diccionario:
print(len(diccio))

print(diccio)