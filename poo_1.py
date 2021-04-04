'''Píldoras informáticas
POO. video 26'''

#Clase
class Coche(): 
	#Constructor:
	def __init__(self):

		#Propiedades encapsuladas(4):
		self.__largoChasis=250 
		self.__anchoChasis=120
		self.__ruedas=4
		self.__enmarcha=False

	def arrancar(self,arrancamos): 
		#Comportamientos:
		self.__enmarcha=arrancamos

		if(self.__enmarcha):
			return "El coche está en marcha"
		else:
			return "El coche está parado"

	def estado(self):
			print("El coche tiene " , self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

#Instanciar la clase:
miCoche=Coche() 

#Llamando al método arrancar:
print(miCoche.arrancar(True))		

miCoche.estado()


print("-----------------------------------------")
print("A continuación creamos el segundo objeto:")
print("-----------------------------------------")

miCoche2 = Coche()
print(miCoche2.arrancar(False))
miCoche2.__ruedas=2
miCoche2.estado()
