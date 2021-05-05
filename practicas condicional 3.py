#Píldoras informáticas
#Condicionales IV. Video 13:

print("Asignaturas optativas año 2017.")
print("Asignaturas optativas: Informática gráfica - Pruebas de software - Usabilidad y accesibilidad.")
opcion = input("Escribe la asignatura escogida: ")

#Transforma el texto ingresado en minúsculas:
asignatura=opcion.lower()


if asignatura in ("informática gráfica", "pruebas de software", "usabilidad y accesibilidad"):
	print("Asignatura elegida: " + asignatura)
else:
	print("La asignatura elegida no está contemplada.")	