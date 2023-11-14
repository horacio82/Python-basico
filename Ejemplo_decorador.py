''' Píldoras informáticas - video 73, 74 y 74b.
En este vídeo comenzamos a ver las funciones decoradores. 
Estas funciones añaden funcionalidades al resto de funciones del programa.
'''

def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args, **kwards):

        #Acciones adicionales que decoran:
        print("Vamos a realizar un cálculo: ")

        funcion_parametro(*args, **kwards)

        #Acciones adicionales que decoran:
        print("Hemos terminado el cáculo.")

    return funcion_interior    


@funcion_decoradora
def suma(num1, num2):
    print(num1+num2)

@funcion_decoradora
def resta(num1, num2):
    print(num1-num2)

@funcion_decoradora
def potencia(base, exponente):
    print(pow(base, exponente))

suma(7,5)

resta(12,10)

potencia(5,3)