''' Pildoras informáticas - video 76
Vemos en este vídeo  cómo hacer pruebas y testeos de nuestras funciones 
utilizando la documentación de Python.
'''
import doctest
doctest.testmod()


def areaTriangulo(base,altura):

    """ DOCUMENTYACIÓN Y PRUEBAS
    Calcula el área de un triángulo dado

    >>> areaTriangulo(3,6)
    9.0


    """
    return (base*altura)/2

#----------------------------------------------------------------------------

def compruebaMail(mailUsuario):
    """
    La función compruebaMail evalúa un mail recibido en busca de la @
    si tiene una @ es correcto, si tiene mas de una @ es incorecto
    si la @ está al final es incorrecto.

    >>> compruebaMail('juan@cursos.es')
    True

    >>> compruebaMail('juancursos.es@')
    False

    >>> compruebaMail('juancursos.es')
    False

    >>> compruebaMail('juan@cursos@.es')
    False


    """    
    arroba=mailUsuario.count('@')

    if(arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1)or mailUsuario.find('@')==0):

        return False

    else:
        return True




