'''
Utilizando uno de los algoritmos vistos en clase
para trazar lineas, hacer un programa que permita
trazar poligonos regulares de cualquier numero de
lados.
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

def PoligonoRegular(pantalla,N,centro, radio, color):
    alfa = 0.0
    alfa = 2*math.pi/N
    vertices = list()
    for i in range(N):
        a = centro[0]+(int)(radio*math.cos((i-1)*alfa))
        b = centro[1]+(int)(radio*math.sin((i-1)*alfa))
        vertices.append([a,b])
    PoligonoIrregular(pantalla,vertices,color)

def main():
	print "Ingrese el numero de lados del poligono: "
	N = input()
	print "Ingrese el centro de la figura: "
	x = input()
	y = input()
	print "Ingrese el radio:"
	radio = input()
	PoligonoRegular(pantalla,N,[x,y], radio, (30,55,255))
	pygame.display.flip()
	while True:
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            sys.exit()

if __name__ == '__main__':
	main()
