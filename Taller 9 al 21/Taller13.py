import sys,math,pygame

pygame.init()

tamano = ancho, alto = 1150, 600
color = 80,200,120
pantalla = pygame.display.set_mode(tamano)
pygame.display.set_caption("Dibujo")
pantalla.fill(color)
pygame.display.flip()

def PlotPoint(pantalla, xc, yc, x, y,color):
	pantalla.set_at( ( (xc + x) , (yc + y)),color)
	pantalla.set_at( ( (xc - x) , (yc + y)),color)
	pantalla.set_at( ( (xc + x) , (yc - y)),color)
	pantalla.set_at( ( (xc - x) , (yc - y)),color)
	pantalla.set_at( ( (xc + y) , (yc + x)),color)
	pantalla.set_at( ( (xc - y) , (yc + x)),color)
	pantalla.set_at( ( (xc + y) , (yc - x)),color)
	pantalla.set_at( ( (xc - y) , (yc - x)),color)

def CircleMidPoint(xc, yc, r,color):
	y = 0
	z = 0
	x = 0
	y = r
	p = 1 - r
	deltaE=3
	deltaSE= 5- r*2
	PlotPoint(pantalla, xc, yc, x, y,color)
	
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
		PlotPoint(pantalla,xc, yc, x, y,color)	
		pygame.display.flip()

def CircleGrosor(Cx, Cy, r, color, grosor):
	for i in range(grosor):
		CircleMidPoint(Cx,Cy,r,color)
		r = r+1

def Linea_Bresenham(pantalla, Xi, Yi, Xf, Yf, color):
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
	

def Linea_Grosor(pantalla, Xa,Ya,Xb,Yb,color,grosor):
	for i in range(grosor):
		Linea_Bresenham(pantalla,Xa,Ya,Xb,Yb,color)
		Xa -=1
		Xb -=1


def main():
	rojo = (255,0,0)
	azul = (0,0,255)
	negro = (0,0,0)
	morado = (87,35,100)
	CircleGrosor(900,150,50,morado,2)#sol
	Linea_Grosor(pantalla,950,150,1010,150,negro,1)
	Linea_Grosor(pantalla,850,150,790,150,negro,1)
	Linea_Grosor(pantalla,900,100,900,40,negro,1)
	Linea_Grosor(pantalla,900,200,900,260,negro,1)
	Linea_Grosor(pantalla,935,115,985,55,negro,2)
	Linea_Grosor(pantalla,865,190,825,240,negro,2)
	Linea_Grosor(pantalla,865,115,815,75,negro,2)
	Linea_Grosor(pantalla,935,190,975,240,negro,2)
	Linea_Grosor(pantalla,850,170,450,270,azul,2)#Hilo
	CircleGrosor(170,150,40,rojo,2)#cabeza
	Linea_Grosor(pantalla,170,193,110,390,rojo,2)
	Linea_Grosor(pantalla,175,193,280,390,rojo,2)
	Linea_Grosor(pantalla,280,390,110,390,rojo,2)
	Linea_Grosor(pantalla,170,390,170,480,rojo,5)
	Linea_Grosor(pantalla,230,390,230,480,rojo,5)
	Linea_Grosor(pantalla,160,225,90,330,rojo,3)#manos
	Linea_Grosor(pantalla,190,225,450,270,rojo,4)
	CircleGrosor(155,140,5,rojo,2)#OJO
	CircleGrosor(185,140,5,rojo,2)
	CircleGrosor(170,170,5,rojo,2)#BOCA
	Linea_Grosor(pantalla,173,150,173,160,rojo,2)#nariz
	pygame.display.flip()
	while True:
	   for event in pygame.event.get():
	   	if event.type == pygame.QUIT:
	   		sys.exit()

if __name__ == '__main__':
	main()
