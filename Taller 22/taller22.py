'''
Implementar el recorte de recorte de imagenes (mouse),
utlizando como prueba una imagen cargando desde un archivo
'''
import sys, pygame

pygame.init()
tamano = ancho, alto = 800, 500
color = 255,255,255
pantalla = pygame.display.set_mode(tamano)
pygame.display.set_caption('Recorte')
pantalla.fill(color)
imagen = pygame.image.load("warner.jpg") 
pantalla.blit(imagen,(250,0))
pygame.display.flip()

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
	pygame.display.flip()
	

def Linea_Grosor(pantalla, Xa,Ya,Xb,Yb,color,grosor):
	for i in range(grosor):
		Linea_Bresenham(pantalla,Xa,Ya,Xb,Yb,color)
		Ya -=1
		Yb -=1
	pygame.display.flip()


def RectanguloRelleno(pantalla,xi,yi,xf,yf,color):
    largo = abs(xf - xi)
    ancho = abs(yf - yi)
    x1 = xi
    y1 = yi
    x2 = x1+largo
    y2 = y1
    x3 = xi
    y3 = y1+ancho
    x4 = xi+largo
    y4 = yi + ancho
    Linea_Grosor (pantalla, x1, y1, x2, y2, color,2)
    Linea_Grosor (pantalla, x1, y1, x3, y3, color,2)
    Linea_Grosor (pantalla, x3, y3, x4, y4, color,2)
    Linea_Grosor (pantalla, x2, y2, x4, y4, color,2)
    i = 0
    while i <= ancho:
        Linea_Grosor(pantalla, x1,y1+i,x2,y2+i,color,2)
        i+=1
   
def Cortar():
	capturador = 0
	while True:
		pygame.event.wait()
		pygame.event.get()
		mouse = pygame.mouse.get_pressed()
		if mouse[0]:
			if capturador==1:
				posx2,posy2 = pygame.mouse.get_pos()
				capturador = 2 
				break
			else:
				posx,posy = pygame.mouse.get_pos()
				capturador += 1
	RectanguloRelleno(pantalla,0,0,ancho,posy,(255,255,255))#arriba
	RectanguloRelleno(pantalla,0,0,posx,alto,(255,255,255))#izquierda
	RectanguloRelleno(pantalla,0,posy2,ancho,alto,(255,255,255))#abajo
	RectanguloRelleno(pantalla,posx2,0,ancho,alto,(255,255,255))#derecha



def main():
	Cortar()
	pygame.display.flip()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

if __name__ == "__main__":
    main()
    