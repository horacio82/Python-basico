import sqlite3

miConexion=sqlite3.connect("Primera base")
miCursor=miConexion.cursor()
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER,SECCION VARCHAR(20))")
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN',15,'DEPORTES')")

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=miCursor.fetchall()

for producto in variosProductos:
    print("Nombre artículo:",producto[0],"Sección:",producto[2])

miConexion.commit()






miConexion.close()
