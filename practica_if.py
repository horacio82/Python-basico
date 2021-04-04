#Pildoras informáticas:
#Curso Python. Condicionales I. Vídeo 10

print("Programa de evaluación de notas de alumnos")

#input pide al usuario que ingrese un dato (lo toma como string).
nota_alumno=input("Introduce la nota: ") 

def evaluacion(nota):
	valoracion="aprobado" #Variable
	if nota<5: #Condicional if.
		valoracion="suspenso"
	return valoracion
	
print(evaluacion(int(nota_alumno)))		


