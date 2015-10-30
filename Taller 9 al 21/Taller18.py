'''
Implementar el relleno de poligonos regulares e irregulares.
'''
import pygame, sys,math

colorfondo = 255, 255, 255
tamano = ancho, alto = 1000, 600
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

def Linea_Grosor(pantalla, Xa,Ya,Xb,Yb,color,grosor):
	for i in range(grosor):
		Linea_Punto_Medio(pantalla,Xa,Ya,Xb,Yb,color)
		Xa -=1
		Xb -=1


def PoligonoIrregular(pantalla,vertices,color,espesor):
    N = len(vertices)
    for i in range(N-1):
    	Linea_Grosor (pantalla, vertices[i][0], vertices[i][1], vertices[i+1][0], vertices[i+1][1],color,espesor)
    Linea_Grosor (pantalla, vertices[N-1][0], vertices[N-1][1], vertices[0][0], vertices[0][1],color,espesor)

def PoligonoRegular(pantalla,N,centro, radio, color):
    alfa = 0.0
    alfa = 2*math.pi/N
    vertices = list()
    for i in range(N):
        a = centro[0]+(int)(radio*math.cos((i-1)*alfa))
        b = centro[1]+(int)(radio*math.sin((i-1)*alfa))
        vertices.append([a,b])
    PoligonoIrregular(pantalla,vertices,color,2)

def PoligonoRegularRelleno(pantalla,N,centro, radio, color):
    while radio >= 0:
    	pygame.display.flip()
        PoligonoRegular(pantalla,N,centro, radio, color)
        radio = radio-1


def InsidePolygon(polygon, N, p):
	counter = 0
	i = 1
	xinters = 0.0
	p1 = polygon[0]
	for i in range(N+1):
		p2 = polygon[i % N]
		if p[1] > min(p1[1],p2[1]):
			if p[1] <= max(p1[1],p2[1]):
				if p1[0] <= max(p1[0],p2[0]):
					if p1[1] != p2[1]:
						xinters = (p[1]-p1[1])*(p2[0]-p1[0])/(p2[1]-p1[1])+p1[0]
						if p1[0] == p2[0] or p[0] <= xinters:
							counter +=1
		p1 = p2
	if counter%2 == 0:
		return False
	else:
		return True

			
def flooffill(pantalla,x,y,oldColor,newColor):
	theStack = [(x,y)]
	while len(theStack) > 0:
		x,y = theStack.pop()
		if pantalla.get_at((x,y)) != oldColor:
			return
		if x>0 and y>0 and x<900 and y<600:
			pantalla.set_at((x,y),newColor)
			theStack.append((x+1,y)) #right
			theStack.append((x-1,y))#left
			theStack.append((x,y+1))#down
			theStack.append((x,y-1))#up

def PoligonoIrregularRelleno(pantalla,vertices,color):
	PoligonoIrregular(pantalla,vertices,color,2)
	pygame.display.flip()
	for i in range(vertices[len(vertices)-1][0]+500):
		if i<=ancho-1:
			for j in range(vertices[len(vertices)-1][1]+500):
				if j<=alto-1:
					if InsidePolygon(vertices,len(vertices),[i,j]):
						flooffill(pantalla,i,j,(255,255,255),color)
		pygame.display.flip()

		
def main():
	PoligonoRegularRelleno(pantalla,11,[100,250], 100, (30,55,255))
	vertices = [[700,500],[280,180],[330,350],[580,550]]
	vertices.sort()
	PoligonoIrregularRelleno(pantalla,vertices,(135,206,250))
	pygame.display.flip()
	vertices2 = [[730,220],[530,0],[630,250],[890,290]]
	vertices2.sort()
	PoligonoIrregularRelleno(pantalla,vertices2,(210,105,30))
	pygame.display.flip()
	while True:
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            sys.exit()

if __name__ == '__main__':
	main()

