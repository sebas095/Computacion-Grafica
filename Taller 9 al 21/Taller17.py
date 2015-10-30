'''
Utilizando uno de los algoritmos vistos en clase
para trazar lineas, hacer un programa que permita
trazar poligonos irregulares de cualquier numero de lados.
'''
import pygame, sys,math

colorfondo = 255, 255, 255
tamano = ancho, alto = 900, 600
pantalla = pygame.display.set_mode(tamano)
pantalla.fill(colorfondo)

pygame.display.flip()

def Linea_Punto_Medio (pantalla, Xi, Yi, Xf, Yf, color):
	dx = (Xf - Xi)
	dy = (Yf - Yi)
	if dy < 0:
		dy = -dy
		stepy = -1
	else:
		stepy = 1
	if dx < 0:
		dx = -dx
		stepx = -1
	else:
		stepx = 1
	x = Xi
	y = Yi
	pantalla.set_at((x,y),color)
	if dx > dy:
		p = 2*dy - dx
		incE = 2*dy
		incNE = 2*(dy-dx)
		while x != Xf:
			x = x + stepx
			if p <= 0:
				p = p + incE
			else:
				y = y + stepy
				p = p + incNE
			pantalla.set_at((x,y),color)

	else:
		p = 2*dx - dy
		incE = 2*dx
		incNE = 2*(dx-dy)
		while  y != Yf:
			y = y + stepy
			if p < 0:
				p = p + incE
			else:
				x = x + stepx
				p = p + incNE
			pantalla.set_at((x,y),color)


def PoligonoIrregular(pantalla,vertices,color):
    N = len(vertices)
    for i in range(N-1):
        Linea_Punto_Medio (pantalla, vertices[i][0], vertices[i][1], vertices[i+1][0], vertices[i+1][1],color)
    Linea_Punto_Medio (pantalla, vertices[N-1][0], vertices[N-1][1], vertices[0][0], vertices[0][1],color)

def main():
	print "Cuantos puntos va ingresar:"
	N = input()
	vertices = list()
	for i in range(N):
		print "Ingrese el",str(i+1)+". par de puntos:"
		x = input()
		y = input()
		vertices.append([x,y])
	vertices.sort()
	PoligonoIrregular(pantalla,vertices,(125,125,125))

	pygame.display.flip()
	while True:
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            sys.exit()

if __name__ == '__main__':
	main()