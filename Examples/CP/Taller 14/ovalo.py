import pygame
pygame.init()
tamano = ancho, alto = 500, 500
color = 0, 0, 0
tono = 216,30,5
pantalla = pygame.display.set_mode(tamano)
pantalla.fill(color)

def PlotPoint(pantalla, xc, yc, x, y):
	pantalla.set_at( ( (xc + x) , (yc + y)),(255,255,255))
	pantalla.set_at( ( (xc - x) , (yc + y)),(255,255,255))
	pantalla.set_at( ( (xc + x) , (yc - y)),(255,255,255))
	pantalla.set_at( ( (xc - x) , (yc - y)),(255,255,255))
x=0
y=0
rx=0
ry=0
rx1=0
ry2=0
tworx2=0
twory2=0
def EllipseMidPoint(xc,yc,rx,ry):
	ry2=ry*ry
	rx2=rx*rx
	twory2=2*ry2
	tworx2=2*rx2
	x=0
	y=ry
	p=0
	PlotPoint(pantalla,xc,yc,x,y)
	pygame.display.flip()
	px=0
	py=tworx2*y
	while(px<py):
		x=x+1
		px=px+twory2
		if p<0:
			p=p+ry2+px
		else:
			y=y-1
			py=py-tworx2
			p=p+ry2+px-py
		PlotPoint(pantalla,xc,yc,x,y)
		pygame.display.flip()
	p=int(round((ry2-rx2*ry+(0.7*rx2))))
	px=0
	py=tworx2*y
	while(y>0):
		y=y-1
		py=py-tworx2
		if(p>0):
			p=p+rx2-py
		else:
			x=x+1
			px=px+twory2
			p=p+rx2-py+px
		PlotPoint(pantalla,xc,yc,x,y)
		pygame.display.flip()
for i in range (0,50):
	for j in range(0,40):
		EllipseMidPoint(200,200,i,j)
while 1:
   for event in pygame.event.get():
       if event.type == pygame.QUIT: 
           sys.exit()