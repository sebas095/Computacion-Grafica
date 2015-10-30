import funcion

diccionario = {}

archivo = open("personas.txt", "r")
registro = archivo.readlines()
lista = []

for i in registro:
	l = i.strip().split(",")
	lista.append(l)

#print lista_personas
funcion.leerRegistros(diccionario,lista)



#print diccionario

clave = raw_input("Por favor Digite el numero de documento: ")

print diccionario[clave]
archivo.close()
