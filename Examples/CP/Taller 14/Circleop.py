import sys,math,pygame

pygame.init()

tamano = ancho, alto = 500, 500
color = 0, 0, 0
tono = 216,30,5

pantalla = pygame.display.set_mode(tamano)

pantalla.fill(color)


def PlotPoint(pantalla, xc, yc, x, y):
	pantalla.set_at( ( (xc + x) , (yc + y)),(255,255,255))
	pantalla.set_at( ( (xc - x) , (yc + y)),(255,255,255))
	pygame.draw.line(pantalla,(255,255,255),[xc+x,y+yc],[xc-x,y+yc],1)
	pantalla.set_at( ( (xc + x) , (yc - y)),(255,255,255))
	pantalla.set_at( ( (xc - x) , (yc - y)),(255,255,255))
	pygame.draw.line(pantalla,(255,255,255),[xc+x,yc-y],[xc-x,yc-y],1)
	pantalla.set_at( ( (xc + y) , (yc + x)),(255,255,255))
	pantalla.set_at( ( (xc - y) , (yc + x)),(255,255,255))
	pygame.draw.line(pantalla,(255,255,255),[xc+y,x+yc],[xc-y,x+yc],1)
	pantalla.set_at( ( (xc + y) , (yc - x)),(255,255,255))
	pantalla.set_at( ( (xc - y) , (yc - x)),(255,255,255))
	pygame.draw.line(pantalla,(255,255,255),[xc+y,yc-x],[xc-y,yc-x],1)
	
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


CircleMidPoint(200, 200, 200)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()