#Píldoras informáticas
#Bucles V continue, pass y else.


for letra in "Python":

	if letra=="h":
		continue

	print("Viendo la letra: " + letra)	

print("---------------------------------------------------")

#Otro ejemplo sencillo:
nombre = "Píldoras informáticas"

contador=0

for i in nombre:

	if i==" ": #Para que ignore el espacio en blanco
		continue # y continue.
	contador+=1 #Incrementa la variable en 1.

print(contador)	

print("---------------------------------------------------")

#Ejemplo con else. Para evaluar si tiene una arroba:
email=input("Introduce tu correo electrónico: ")

for i in email:
	if i=="@":
		arroba=True
		break;

else: #Forma parte del bucle for.
	arroba=False

print(arroba)			