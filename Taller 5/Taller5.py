import sys, pygame, time

pygame.init()

tamano = ancho, alto = 650, 550

color = 255, 255, 255

pantalla = pygame.display.set_mode(tamano)
pantalla.fill(color) 

avion = pygame.image.load("avion.gif")
rectavion = avion.get_rect()

barco = pygame.image.load("barco.jpg")
rectbarco = barco.get_rect()

carro = pygame.image.load("carro.jpg")
rectcarro = carro.get_rect()

moto = pygame.image.load("moto.gif")
rectmoto = moto.get_rect()

imagenes = [rectavion,rectbarco,rectcarro,rectmoto]
imag = [avion,barco,carro,moto]

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		for i in range(len(imagenes)):
			time.sleep(0.5)
			pantalla.fill(color) 
			pantalla.blit(imag[i], imagenes[i])
			pygame.display.flip() 