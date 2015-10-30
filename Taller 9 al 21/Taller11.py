#Implementar el algoritmo del punto medio para
#dibujar circunferencias agragando la opcion del grosor

import sys,math,pygame

pygame.init()

tamano = ancho, alto = 500, 500
color = 255,255,255
pantalla = pygame.display.set_mode(tamano)
pygame.display.set_caption("Circunferencia")
pantalla.fill(color)
pygame.display.flip()

def PlotPoint(pantalla, xc, yc, x, y):
	pantalla.set_at( ( (xc + x) , (yc + y)),(0,0,0))
	pantalla.set_at( ( (xc - x) , (yc + y)),(0,0,0))
	pantalla.set_at( ( (xc + x) , (yc - y)),(0,0,0))
	pantalla.set_at( ( (xc - x) , (yc - y)),(0,0,0))
	pantalla.set_at( ( (xc + y) , (yc + x)),(0,0,0))
	pantalla.set_at( ( (xc - y) , (yc + x)),(0,0,0))
	pantalla.set_at( ( (xc + y) , (yc - x)),(0,0,0))
	pantalla.set_at( ( (xc - y) , (yc - x)),(0,0,0))

def CircleMidPoint(xc, yc, r):
	y = 0
	z = 0
	x = 0
	y = r
	p = 1 - r
	deltaE=3
	deltaSE= 5- r*2
	PlotPoint(pantalla, xc, yc, x, y)
	
	while (x < y):
		x = x + 1
		if(p < 0):
			p = p + deltaE
			deltaE=deltaE+2
			deltaSE=deltaSE+2

		else:
			y = y - 1
			p = p + deltaSE
			deltaE=deltaE+2
			deltaSE=deltaSE+4
		PlotPoint(pantalla,xc, yc, x, y)	
		pygame.display.flip()

def main():
	print "Ingrese el centro de la circunferencia"
	Cx = input()
	Cy = input()
	print "Ingrese el radio de la circunferencia"
	r = input()
	print "Ingrese el grosor"
	grosor = input()


	for i in range(grosor):
		CircleMidPoint(Cx,Cy,r)
		r = r+1

	while True:
	   for event in pygame.event.get():
	      if event.type == pygame.QUIT:
	         sys.exit()

if __name__ == "__main__":
	main()
