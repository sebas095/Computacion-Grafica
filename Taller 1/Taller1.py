''' Leer un archivo de texto, guardar todas las palabras en una lista, y decir cuantas
consonantes hay en la lista'''

archivo = open("lectura.txt","r")
lineas = []
cont = 0

#separar todo por palabras
for i in archivo.readlines():
	palabra = i.split(' ')
	for j in palabra:
		if j != '':
			lineas.append(j)

#cuenta las consonantes
for pal in lineas:
	for pos in range(len(pal)):
		if pal[pos] != 'a' and pal[pos] != 'A'and pal[pos] != 'e' and pal[pos] != 'E' and pal[pos] != 'i' and pal[pos] != 'O' and pal[pos] != 'U' and pal[pos] != 'u' and pal[pos] != '\n':
			cont += 1

print "EL archivo tiene: ",cont," consonantes.\n"

