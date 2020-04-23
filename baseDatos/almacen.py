#importar una libreria 
import sqlite3

#crear variable que contendra la conexion
miConexion = sqlite3.connect("dbAlmacen")


#crear la variable que almacena el cursor
miCursor = miConexion.cursor()


#creamos la consulta SQL que me permita construir la tabla
#miCursor.execute(''' CREATE TABLE detalleProductos3
#(idProducto INTEGER PRIMARY KEY AUTOINCREMENT,
#nombreProducto VARCHAR(34) UNIQUE,
#precioProducto FLOAT,
#seccionTienda VARCHAR(15))''')

#crear una lista que contenga los items que insetaremos a la tabla
multiplesProdutos = [
    ('Pan Tostado', 12.3, 'Panaderia'),
    ('Pan de trigo', 14.2, 'Panaderia'),
    ('Pasas', 33, 'Abarrotes'),
    ('Pepsi-cola', 15, 'Abarrotes'),
]
#crear la consulta de SQL que nos permita insertar multiples registros
miCursor.executemany("INSERT INTO detalleProductos3 VALUES(NULL,?,?,?)", multiplesProdutos)

#crear la sentencia SQL que permita recuperar los datos de la tabla
miCursor.execute("SELECT * FROM detalleProductos3")

#crear una variable donde almaceno los registros
matrizValores = miCursor.fetchall()

#estructura repetituiva FOR
for productoAlmacenado in matrizValores:
    print ("Nombre del producto: ",productoAlmacenado[1], "Precio del Producto: " ,productoAlmacenado[2] )

#Confirmamo el guardado
miConexion.commit()

# en este punto cerramos la base de datos 
miConexion.close()

