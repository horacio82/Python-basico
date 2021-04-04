#Píldoras informáticas.
#Bucles II video 15.

'''Programa que comprueba si una dirección de correo tiene
una arroba y un punto...:'''
contador=0
miCorreo=input("Introduce tu dirección de correo: ") 

for i in "molinarih2011@gmail.com":

	if(i=="@" or i=="."):

		contador=contador+1

if contador==2:
	print("La dirección de correo es correcta.")
else:
	print("El correo no es correcto.")


for i in range(5):
	print(i)