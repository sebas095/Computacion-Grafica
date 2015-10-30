import sys,math,pygame

def LineaMidPoint(x0,y0,x1,y1):
	pygame.init()

	tamano = ancho, alto = 640, 480
	color = 0, 0, 0

	pantalla = pygame.display.set_mode(tamano)
	pantalla.fill(color)
	x,y,dx,dy,xend,p,incE,incNE=0,0,0,0,0,0,0,0

	dx = x1-x0
	dy = y1-y0
	p =2*dy - dx
	incE=2*dy
	if p<0:
		p=abs(p)
	if dx<0:
		dx=abs(dx)
	if dy<0:
		dy=abs(dy)
	if incE<0:
		incE=abs(incE)

	if x0>x1:
		x=x1
		y=y1
		xend=x0
	else:
		x=x0
		y=y0
		xend=x1
	while x<=xend:
		pantalla.set_at((x,y),(255,255,255))
		x=x+1
		if p<=0:
			p=p+incE
		else:
			y=y+1
			p=p+incNE
	pygame.display.flip()

