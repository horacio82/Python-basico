#Pildoras informáticas
#Curso de Python. Métodos de cadenas. Vídeo 33

#nombreUsuario=input("Introduce tu nombre de Usuario: ")

#print("El nombre es:",nombreUsuario.lower())

edad=input("Introduce la edad: ")

while (edad.isdigit()==False):
	print("Por favor, introduce un valor numérico.")
	edad=input("Introduce la edad: ")




if (int(edad)<18):
	print("No puedes pasar.")
else:
	print("Puedes pasar.")	