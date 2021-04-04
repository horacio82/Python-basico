#Píldoras informáticas. Bucles II bucle for (Video 16):

valido=False

correo=input("Introduce tu correo electrónico: ")

for i in range(len(correo)):

 	 if correo[i]=="@":

 	 	valido=True


if valido:

	print("Correo electrónico correcto.")	

else:

	print("Correo electrónico incorrecto.")	