import sys,pygame,time,os
pygame.init()
Pantalla = pygame.display.set_mode((110, 142))
Gris = (42, 42, 42)
Pantalla.fill(Gris)

imagen1 = pygame.image.load("ahorcado1.bmp")
imagen2 = pygame.image.load("ahorcado2.bmp")
imagen3 = pygame.image.load("ahorcado3.bmp")
imagen4 = pygame.image.load("ahorcado4.bmp")
imagen5 = pygame.image.load("ahorcado5.bmp")
imagen6 = pygame.image.load("ahorcado6.bmp")
imagen7 = pygame.image.load("ahorcado7.bmp")
vidas = 7

Lista_Imagenes = [imagen7, imagen6, imagen5, imagen4, imagen3,imagen2, imagen1]
Pantalla.blit(Lista_Imagenes[vidas-1], (10,10))
pygame.display.flip()

def llenar_oculta(palabra, palabra_oculta):
	cont = len(palabra)
	i = 0
	while (i < cont):
		palabra_oculta.append("*")
		i = i + 1

def Ahorcado():
	palabras = ["casa", "perro", "esternoncleidomastoideo","comadreja","pato","castillo","cascabel"]
	palabra_selec = input("Escoja un Numero del 1 al 7: ")
	palabra = palabras[palabra_selec - 1]
	palabra_oculta = []
	llenar_oculta(palabra, palabra_oculta)
	vidas=7
	letra = ''
	j = 0
	asteriscos = palabra_oculta.count("*")
	os.system('cls')
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
			os.system('cls')
			if(asteriscos <= 0):
				vidas = 0
		print(palabra_oculta)
		if (cont_letra == 0):
			vidas = vidas - 1
			Pantalla = pygame.display.set_mode((110, 142))
			Gris = (42, 42, 42)
			Pantalla.fill(Gris)
			Pantalla.blit(Lista_Imagenes[vidas-1], (10,10))
			pygame.display.flip()
			print("La letra ",letra," no esta en la palabra.")
			print("Te quedan ",vidas," vidas.")
	print("Juego Terminado.")
	while 1:
    		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
       				sys.exit()
Ahorcado()