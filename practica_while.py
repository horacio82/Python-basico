#Píldoras informáticas.
#Bucles IV. while (Video 17)

edad = int(input("Introduce tu edad por favor: "))

while edad<5 or edad>100:
	print("Has introducido una edad incorrecta, vuelve a intentarlo.")
	edad=int(input("Introduce tu edad por favor: "))

print("Gracias por colaborar, puedes pasar.")
print("Edad del aspirante " + str(edad))