'''Píldoras informáticas. Curso de Python
Generadores I. Video 19.'''


#Función tradicional
print("Función tradicional")

def generaPres(limite):

	num=1

	miLista=[]

	while num<limite:

		miLista.append(num*2)

		num=num+1

	return miLista
	
print(generaPres(10))

print("-------------------------------")

#Generador
print("Generador")

def generaPares2(limite):

	num=1

	while num<limite:

		yield num*2

		num=num+1

devuelvePares=generaPares2(10)

#for i in devuelvePares:

	#print(i)


#Para imprimir los 3 primeros valores:
print(next(devuelvePares))
print("Acá podría ir más código...")
print(next(devuelvePares))
print("Acá podría ir más código...")
print(next(devuelvePares))
print("Acá podría ir más código...")

				