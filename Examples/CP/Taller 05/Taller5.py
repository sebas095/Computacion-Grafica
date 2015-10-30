def llenar_oculta(palabra, palabra_oculta):
	cont = len(palabra)
	i = 0
	while (i < cont):
		palabra_oculta.append("*")
		i = i + 1
def fin_juego(vidas):
	vidas = 0
def Ahorcado():
	palabras = ["casa", "sapo", "conejo","asdhakshdkajshd"]
	palabra_selec = input("Escoja un Numero del 1 al 4: ")
	palabra = palabras[palabra_selec - 1]
	palabra_oculta = []
	llenar_oculta(palabra, palabra_oculta)
	vidas = 5
	letra = ''
	j = 0
	asteriscos = palabra_oculta.count("*")
	while (vidas > 0):
		letra = raw_input("Ingrese Una Letra: ")
		cont_letra = 0
		j = 0
		while (j < len(palabra)):
			if (letra == palabra[j]):
				cont_letra = cont_letra + 1
				del palabra_oculta[j]
				palabra_oculta.insert(j,letra)
			j = j + 1
			asteriscos = palabra_oculta.count("*")
			if(asteriscos <= 0):
				vidas = 0
		print(palabra_oculta)
		if (cont_letra == 0):
			vidas = vidas - 1
			print("La letra ",letra," no esta en la palabra.")
			print("Te quedan ",vidas," vidas.")
	print("Juego Terminado.")

Ahorcado()