#!/usr/bin/env python

'''
    File name: mover_archivos.py
    Author: Alex Inza 
    Date created: 26/9/2018
    Date last modified: 25/11/2018
    Python Version: 3.6.5
'''

'''
El tipo de archivo a mover tiene el mismo índice que la carpeta donde van a moverse,
y por lo tanto, con las opciones dadas en la parte de #Interacción con el usuario.
Esto debe tenerse en cuenta a la hora de modificar cualquier parámetro.
'''

import shutil
import os

#Interacción con el usuario
print('0  -  Mover archivos .zip')
print('1  -  Mover archivos .stl')
print('2  -  Mover archivos .pdf')
print('3  -  Mover archivos .docx')
print('4  -  Mover archivos .odt')
entrada = input()

#Definimos una variable para el número de archivos movidos
num_archivos = 0

#Directorios de origen y de destino de los archivos
origen = 'C:\\Users\\user\\Downloads'  
destinos = {'0' : 'D:\\ZIPs', '1' : 'D:\\STLs', '2' : 'D:\\PDFs', '3' : 'D:\\WORDs', '4' : 'D:\\WORDs'}

#Primero nos movemos al directorio donde están los archivos a mover
os.chdir(origen)

#Creamos una lista con todos los archivos de el directorio de origen y otra con los que vamos mover que empieza vacía.
archivos = os.listdir()
amover = []
directorio = os.getcwd()

#Creamos un diccionario que contenga los diferentes tipos de archivos
tipo_archivo = {'0' : '.zip', '1' : '.stl', '2' : '.pdf', '3' : '.docx', '4' : '.odt'}

#Definimos la función que se encarga de seleccionar el archivo deseado.
def seleccionar(archivos, extension):
	global amover
	try:
		for i in archivos:
			if i.endswith(extension):
				amover.append(i)
	except:
		print('ERROR')

#Ejecutamos la función para obtener la lista.
try:	
	seleccionar(archivos, tipo_archivo[entrada])
except:
	print('No has introducido un opción válida.')

#Movemos los archivos a la ubicación deseada y vamos mostrando lo que movemos
if amover:
	for x in amover:
		try:
			shutil.move(os.path.join(origen, x), os.path.join(destinos[entrada], x))
			print('{} movido correctamente'.format(x))
			num_archivos += 1
		except:
			print('{} no se ha movido correctamente'.format(x))
else:
	print('Ningún archivo elegido en la ubicación dada, nada que mover.')

#Mostramos los archivos movidos
print('\nSe han movido {} archivos.\n'.format(num_archivos))

print('Proceso completado, pulse cualquier tecla para cerrar esta ventana.')

a = []
while not a:
	a.append(input(''))
