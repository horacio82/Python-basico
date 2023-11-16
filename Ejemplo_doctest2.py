#Pildoras informaticas - video 77
#cómo realizar pruebas un poco más complejas utilizando expresiones anidadas con el módulo doctest.

import math

def raizCuadrada(listaNumeros):

    """
    La función devuelve una lista con la raíz
    cuadrada de los elementos numéricos pasados
    por parámetros en otra lista.

    >>> lista=[]
    >>> for i in [4,9,16]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    [2.0, 3.0, 4.0]

    """

    return [math.sqrt(n) for n in listaNumeros]

#print(raizCuadrada([9,16,25,36]))    

import doctest
doctest.testmod()