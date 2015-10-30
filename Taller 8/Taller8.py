import pygame,sys,time

pygame.init()

tamano = ancho, alto = 1000, 600
color = 0, 0, 0
velocidad = [1, 6]
frenado = velocidad[1]+4

pantalla = pygame.display.set_mode(tamano)
playa = pygame.image.load("playa.jpg").convert()
bola = pygame.image.load("ball.gif").convert_alpha()
rectbola = bola.get_rect()

mov = 0
band = True
while 1:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	
	if (mov-alto) < 0:
		rectbola = rectbola.move(velocidad)
		if rectbola.left < 0 or rectbola.right > ancho:
			velocidad[0] = -velocidad[0]

		if rectbola.top < mov or rectbola.bottom > alto:
			velocidad[1] = -velocidad[1]

		if rectbola.top < mov:
			mov += frenado
			rectbola.top += frenado
		
	if (mov-alto)>=0 and band:
		band = False
		velocidad = [0,0]
		rectbola.centerx = (rectbola.right+rectbola.left)/2
		rectbola.centery = alto-50

	time.sleep(0.009)
	pantalla.fill(color)
	pantalla.blit(playa,(0,0))
	pantalla.blit(bola, rectbola)
  	pygame.display.flip() 
