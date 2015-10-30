#Implementar el algoritmo de Bresenham permitiendo recibir
#los puntos de teclado y el grosor de la linea

import pygame, sys

colorfondo = 255, 255, 255
tamano = ancho, alto = 500, 500
pantalla = pygame.display.set_mode(tamano)
pantalla.fill(colorfondo)

pygame.display.flip() 

def Linea_Bresenham(pantalla, Xi, Yi, Xf, Yf, color):
	dx = (Xf - Xi)
	dy = (Yf - Yi)
	
	if (abs(dy > abs(dx))):
		Xi, Yi = Yi, Xi
		Xf, Yf = Yf, Xf 

	if (Xi > Xf):
		Xi, Xf = Xf, Xi
		Yi, Yf = Yf, Yi

	if Yi < Yf:
		pasoY = 1

	else:
		pasoY = -1

	p = -dx/2
	Y = Yi

	for X in range(Xi, Xf + 1):
		if(abs(dy) > abs(dx)):
			pantalla.set_at((Y,X), color)

		else:
			pantalla.set_at((X,Y), color)

		p = p + dy

		if p > 0:
			Y = Y + pasoY
			p = p - dx


def Linea_Grosor(pantalla, Xa,Ya,Xb,Yb,color,grosor):
	for i in range(grosor):
		Linea_Bresenham(pantalla,Xa,Ya,Xb,Yb,color)
		Xa = Xa+1
	

def main():
	print "Digite el punto inicial:"
	xa, ya = input(), input()
	print "Digite el punto final:"
	xb, yb = input(), input()
	print "Digite Grosor:"
	grosor = input()

	Linea_Grosor(pantalla,xa,ya,xb,yb,(0,0,0),grosor)
	pygame.display.flip() 

	while True:
	   for event in pygame.event.get():
	      if event.type == pygame.QUIT:
	         sys.exit()


if __name__ == "__main__":
	main()
