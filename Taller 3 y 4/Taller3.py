import sys, pygame

pygame.init()

tamano = ancho, alto = 500, 500

color = 0, 0, 0

pantalla = pygame.display.set_mode(tamano)

while 1:
	for event in pygame.event.get():

		for i in range(256):
			for j in range (256):
				for k in range (256):
					pantalla.fill((i,j,k))
					pygame.display.flip() 

		if event.type == pygame.QUIT:
			sys.exit()

