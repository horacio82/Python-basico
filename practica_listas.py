#Pildoras informaticas
#Curso Python. Sintaxis Básica V. Las listas. Vídeo 7

miLista=["Maria", "Pepe", "Marta", "Antonio"]

#Agrega un elemento al final de la lista
miLista.append("Sandra")

#Agrega un elemento en dicha posición 
miLista.insert(2, "José")

#Concatena otra lista al final de miLista
miLista.extend(["Ana", "Marcelo"])

#Muetra el indice del elemento mencionado
#print(miLista.index("Antonio"))

#Imprime true o false si el elemento mencionado está en la lista
#print("Pepe" in miLista)

#Elimina dicho elemento de la lista
#miLista.remove("Ana")

#Elimina el ultimo elemento de la lista
#miLista.pop()


miLista2=["Hugo", "Pedro"]

#Suma esas dos listas
miLista3=miLista+miLista2

#Multiplica dicha lista
miLista4=["Horacio", 38, 1982, "Molinari"]*2

print(miLista4)
