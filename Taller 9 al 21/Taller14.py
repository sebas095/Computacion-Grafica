import sys,math,pygame

pygame.init()

tamano = ancho, alto = 1150, 600
color = 255,255,255
pantalla = pygame.display.set_mode(tamano)
pygame.display.set_caption("Elipses")
pantalla.fill(color)
pygame.display.flip()

def PlotPoint(pantalla, xc, yc, x, y, color):
	pantalla.set_at((xc+x,yc+y),color)
	pantalla.set_at((xc-x,yc+y),color)
	pantalla.set_at((xc+x,yc-y),color)
	pantalla.set_at((xc-x,yc-y),color)

x=0
y=0
rx=0
ry=0
rx1=0
ry2=0
tworx2=0
twory2=0

def ElipseMidPoint(xc,yc,rx,ry,color):
	ry2=ry*ry
	rx2=rx*rx
	twory2=2*ry2
	tworx2=2*rx2
	x=0
	y=ry
	p=0
	PlotPoint(pantalla,xc,yc,x,y,color)
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
		PlotPoint(pantalla,xc,yc,x,y,color)
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
		PlotPoint(pantalla,xc,yc,x,y,color)
		


def RellenoElipse(xc,yc,rx,ry,color):
	for i in range(rx):
		for j in range(ry):
			ElipseMidPoint(xc,yc,i,j,color)
		pygame.display.flip()

def main():
	#Elipse 1
	RellenoElipse(200,200,100,90,(102,205,170))
	#Elipse 2
	RellenoElipse(500,300,50,200,(72,61,139))
	#Elipse 3
	RellenoElipse(900,250,150,120,(255,175,0))
	pygame.display.flip()
	print "\nElipse 1:"
	print "Ecuacion Canonica: (X-200)^2/100 + (Y-200)^2/90 = 1"
	print "Ecuacion General: 9X^2 - 3600X + 10Y^2 - 4000Y + 759600 = 0\n"

	print "Elipse 2:"
	print "Ecuacion Canonica: (X-500)^2/50 + (Y-300)^2/200 = 1"
	print "Ecuacion General: 4X^2 - 400X + Y^2 - 600Y + 99800 = 0\n"

	print "Elipse 3:"
	print "Ecuacion Canonica: (X-200)^2/100 + (Y-200)^2/90 = 1"
	print "Ecuacion General: 12X^2 - 21600X + 15Y^2 - 7500Y + 10655700 = 0\n"
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

if __name__ == '__main__':
	main()