'''
Pildopras informáticas - video 69,70 Y 71
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

    
#----------------------------------video 72-------------------------------------------

cadena1="jARA López"
cadena2="564654"
cadena3="a45621987" 

if re.match("\d",cadena2):
    print("Hemos encontrado el número.")
else:
    print("No lo hemos encontrado.")    


codigo1="dkfdnhdlñpslñfhsdd"
codigo2="jfisklvnb71klowyt"
codigo3="dngoqugmodjff"

if re.search("71", codigo2):
    print("Hemos encontrado el código")

else:
    print("No lo hemos encontrado")    