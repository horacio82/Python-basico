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
			chequeo=self.__chequeo_interno()

		if(self.__enmarcha and chequeo):
			return "El coche está en marcha"

		elif(self.__enmarcha and chequeo==False):
			return"ALgo ha ido mal en el chequeo, no puede arrancar"
			
		else:
			return "El coche está parado"

	def estado(self):
			print("El coche tiene " , self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

	def __chequeo_interno(self):
		print("Realizando chequeo interno")

		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"

		if(self.gasolina=="ok" and self.aceite=="0k" and self.puertas=="cerradas"):
			return True
		else:
			return False

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

miCoche2.estado()
