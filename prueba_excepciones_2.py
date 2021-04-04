'''Píldoras informáticas
Excepciones II. Video 22 / minuto 9:10'''


def divide():

	try:

		op1=(float(input("Introduce el primer número, por favor: ")))

		op2=(float(input("Introduce el segundo número, por favor: ")))

		print("La división es: " + str(op1/op2))

	except ValueError:
	
		print("El valor introducido es erroneo.")

	except ZeroDivisionError:
	
		print("¡No se puede dividir entre 0!")

	finally:			

		print("Cálculo finalizado")

divide()	