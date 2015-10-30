import pygame,sys,time

pygame.init()

tamano = ancho, alto = 1000, 600
color = 0, 0, 0
gravedad = None
gravedad = int(raw_input("Ingrese Gravedad: "))
velocidad = [1, gravedad]

if gravedad != None:
	pantalla = pygame.display.set_mode(tamano)
	playa = pygame.image.load("playa.jpg").convert()
	bola = pygame.image.load("ball.gif").convert_alpha()
	pygame.display.set_caption("Pelota Movimiento :D")
	rectbola = bola.get_rect()

	while 1:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		rectbola = rectbola.move(velocidad)

		if rectbola.left < 0 or rectbola.right > ancho:
			velocidad[0] = -velocidad[0]

		if rectbola.top < 0 or rectbola.bottom > alto:
			velocidad[1] = -velocidad[1]
			if rectbola.left > 0 and rectbola.right <= ancho:
				velocidad[0] = velocidad[0]+1
			else:
				velocidad[0] = -(velocidad[0]-1)

		time.sleep(0.009)
		pantalla.fill(color)
		pantalla.blit(playa,(0,0))
	  	pantalla.blit(bola, rectbola)
	  	pygame.display.flip() 
