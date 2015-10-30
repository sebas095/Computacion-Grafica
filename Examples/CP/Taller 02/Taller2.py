def BuscarLetra():
	palabra = raw_input("Digite una palabra: ")
	letra = ''
	j = 0
	letra = raw_input("Ingrese Una Letra: ")
	cont_letra = 0
	while (j < len(palabra)):
		if (letra == palabra[j]):
			cont_letra = cont_letra + 1
		j = j + 1
	if (cont_letra>0):
		print "la letra ingresada se encontro en la palabra y se repite  "
		print cont_letra
	if(cont_letra==0):
		print "la letra que ingreso no esta en la palabra"