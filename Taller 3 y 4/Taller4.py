import sys, pygame

pygame.init()
color = 255,255,255

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		for i in range(800):
			for j in range (800):
				tamano = ancho, alto = i, j
				pantalla = pygame.display.set_mode(tamano)
				pantalla.fill(color) 
				pygame.display.flip() 

					