def leerRegistros(diccionario, lista):
	for i in range(len(lista)):
		diccionario[lista[i][0]] = lista[i]
