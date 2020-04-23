#importar una libreria 
import sqlite3

#crear variable que contendra la conexion
miConexion = sqlite3.connect("DBAlumno")

#crear la variable que almacena el cursor
miCursor = miConexion.cursor()

#crear la lista
multiplesRegistros = [
    ('Contreras','Lomeli','Oscar'),
    ('Griphin','n','Peter'),
    ('Flores','Mesa','Osiris'),
    ('Monkye','D','Lufy')
]

#crear la consulta de SQL que nos permita insertar multiples registros
miCursor.executemany("INSERT INTO datosAlumnos VALUES(?,?,?)", multiplesRegistros)


#crear una consulta de SQL que permita recuperar los registros
miCursor.execute("SELECT * FROM datosAlumnos")

#Creamos una variable que contenga la matriz de valores
matrizValores = miCursor.fetchall()

#funcion print para mostra los valores
print(matrizValores)

#Confirmamo el guardado
miConexion.commit()

# en este punto cerramos la base de datos 
miConexion.close()
