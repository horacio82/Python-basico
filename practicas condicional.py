#Pildoras informaticas:
#CONDICIONALES III VIDEO 12

salario_presidente=int(input("Introduce el salario del presidente:"))
print("Salario presidente " + str (salario_presidente))

salario_director=int(input("Introduce el salario del director:"))
print("Salario director " + str (salario_director))

salario_jefe_area=int(input("Introduce el salario del jefe de area:"))
print("Salarios jefe de area " + str (salario_jefe_area))

salario_admin=int(input("Introduce el salario del administrativo:"))
print("Salario administrativo " + str (salario_admin))

	#Concatenación de comparación en un condicional:
if salario_admin<salario_jefe_area<salario_director<salario_presidente:
	print("Todo funciona correctamente.")
else:
	print("algo anda mal en esta empresa...")	