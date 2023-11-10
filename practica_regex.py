'''
Pildopras informáticas - video 69 y 70
qué son las expresiones regulares. Se trata de herramientas muy útiles 
para la manipulación y procesado de texto.
'''

import re

cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintáxis sencilla "

print(re.search("aprender", cadena))

textoBuscar="Python"

textoEncontrado=re.search(textoBuscar, cadena)

#Devuelve la posición inicial del texto
print(textoEncontrado.start())

#Devuelve la posición final del texto
print(textoEncontrado.end())

#Devuelve en una tupla donde inicia y termina el texto
print(textoEncontrado.span())

#Devuelve una lista con los strings que coinciden con la búsqueda
print(re.findall(textoBuscar, cadena))

#Devuelve la cantidad (número) de la búsqueda 
print(len(re.findall(textoBuscar, cadena)))


#----------------------------------Video 70------------------------------------------

lista_nombres=['Ana Gómez', 'María Martín', 'Sandra López', 'Santiago Martín']

for elemento in lista_nombres:
    if re.findall('^Sandra', elemento): # ^ Buscar los que comienzan con Sandra
        print(elemento)

    