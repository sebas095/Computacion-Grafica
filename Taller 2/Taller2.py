'''
Utilizando diccionarios leer la base de datos de la clase (nombre, email,telefono)
de un archivo, y permite hacer una busqueda de los datos por el nombre
'''
def leerRegistros(diccionario, personas):
	for i in range(len(personas)):
		diccionario[personas[i][0]] = personas[i][1:len(personas)]


def buscar(clave,llaves):
	for i in llaves:
		if i == clave and clave != '':
			return True
	return False

diccionario = {}

archivo = open("personas.txt","r")
registros = archivo.readlines()
personas = []

for i in registros:
	user = i.strip().split(',')
	personas.append(user)

leerRegistros(diccionario, personas)
llaves = diccionario.keys()

clave = str(raw_input("Por favor ingrese el nombre de la persona: "))
clave = clave.lower()
print '\n'

if buscar(clave,llaves):
	print "Los datos de",clave,"son:\n"
	print "E-mail:",diccionario[clave][0]
	print "Telefono:",diccionario[clave][1]

else:
	print "...La persona:",clave,"No esta registrada en la base de datos...\n"

archivo.close()



