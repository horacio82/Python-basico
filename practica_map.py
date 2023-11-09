'''
Píldoras informáticas - video 68
En este vídeo vemos la función map(). Esta función permite aplicar otra función definida 
previamente a cada elemento de una lista iterable. Se ve con un ejemplo sencillo el uso 
de esta función.
'''

class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de ${}".format(self.nombre, self.cargo, self.salario)
    

listaEmpleados=[

    Empleado("Horacio", "Director", 6700),
    Empleado("Ana", "Presidente", 7500),
    Empleado("Antonio", "Administrativo", 2100),
    Empleado("Sara", "Secretaria", 2150),
    Empleado("Mario", "Botones", 1800),
]    

def calculo_comision(empleado):

    if(empleado.salario<=3000):
        empleado.salario=empleado.salario*1.03
    return empleado

listaEmpleadosComision=map(calculo_comision, listaEmpleados)

for empleado in listaEmpleadosComision:
    print(empleado)