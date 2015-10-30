import pygame, sys, math

pygame.init()

tamano = ancho, alto = 900, 650

color = 96, 96, 255
pantalla = pygame.display.set_mode(tamano)
pygame.display.set_caption('Autoretrato Pygame')


while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	pantalla.fill(color)
	#pygame.draw.rect(pantalla, color(R,G,B), Rect(X,Y), ancho)
	pygame.draw.line(pantalla, (0, 0, 0), (450,170), (450, 500), 5)#cuerpo
	pygame.draw.circle(pantalla, (255,160,122), (450,100), 70, 0)#cabeza
	pygame.draw.circle(pantalla, (0,0,0), (420,80), 5, 0)#ojos
	pygame.draw.circle(pantalla, (0,0,0), (480,80), 5, 0)#ojos
	pygame.draw.line(pantalla, (0, 0, 0), (450,500), (350, 620), 5)#pies
	pygame.draw.line(pantalla, (0, 0, 0), (450,500), (550, 620), 5)#pies
	pygame.draw.line(pantalla, (0, 0, 0), (450,300), (350, 150), 5)#manos
	pygame.draw.line(pantalla, (0, 0, 0), (450,300), (550, 150), 5)#manos
	pygame.draw.line(pantalla, (0, 0, 0), (450,100), (460, 110), 3)#nariz
	pygame.draw.line(pantalla, (0, 0, 0), (460,110), (450, 110), 3)#nariz
	pygame.draw.arc(pantalla, (0,0,0), (430,100,50,50),-math.pi,0,2) #boca recibe pantalla,color,rectangulo(x,y,alto,ancho),angulo inicial, angulo final,espesor
	pygame.display.flip()

