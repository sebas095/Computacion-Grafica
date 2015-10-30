#implementar el algoritmo del punto medio para dibujar
#lineas agregando la opcion del grosor


import sys,math,pygame

pygame.init()

tamano = ancho, alto = 500, 500
color = 255,255,255
pantalla = pygame.display.set_mode(tamano)
pygame.display.set_caption("Linea")
pantalla.fill(color)
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


def main():
	print ("Digite el punto inicial")
	xi, yi = input(), input()
	print ("Digite el punto final")
	xf, yf = input(), input()
	print ("Digite Grosor")
	grosor = input()


	for i in range(grosor):
		Linea_Punto_Medio(pantalla,xi,yi,xf,yf,(0,0,0))
		xi = xi +1
		xf = xf + 1
	pygame.display.flip() 

	while True:
	   for event in pygame.event.get():
	      if event.type == pygame.QUIT:
	         sys.exit()

if __name__ == "__main__":
	main()