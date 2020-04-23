#importar las librerias SLQLite
import sqlite3

#crear una variable en donde contenr la conecxion a la base de datos
miConexion = sqlite3.connect("DBAlumno")

#crear la variable que almacena el cursor
miCuros = miConexion.cursor()

#creamos la consulta SQL que nos permite crear la tabla
#miCuros.execute("CREATE TABLE datosAlumnos (apellidoPadre VARCHAR(23), apellidoMaterno VARCHAR (23), nombreAlumno VARCHAR(23))")

#Creamos la consulta SQL que nos permite insertar un registro en la tabla
miCuros.execute("INSERT INTO datosAlumnos VALUES('Bustamante', 'Holguin', 'Leonel')")

#Confirmamo el guardado
miConexion.commit()
#en este punto cerramos la conexion a la base de datos
miConexion.close()