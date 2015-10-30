import pygame, sys, math
pygame.init()

#-------------------------------------------------------------------------------------
#LINEAS
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

def lineaDDA(pantalla,x1,y1,x2,y2,color):
    dx = x2 - x1
    dy = y2 - y1
    numeropasos = abs(dy)
    if abs(dx) > abs(dy):
        numeropasos = abs(dx)
    incrementoX = incrementoY = 0
    if numeropasos != 0:
        incrementoX = 1.0 * dx / numeropasos
        incrementoY = 1.0 * dy / numeropasos
    x, y = x1, y1
    pantalla.set_at((int(x), int(y)),color)
    for k in range(numeropasos):
        x = x + incrementoX
        y = y + incrementoY
        
        pantalla.set_at((int(x),int(y)),color)
    pygame.display.flip()
#-------------------------------------------------------------------------------------
#Circunferencia sin relleno
def PlotPoint(pantalla, xc, yc, x, y, color):
	pantalla.set_at( ( (xc + x) , (yc + y)),color)
	pantalla.set_at( ( (xc - x) , (yc + y)),color)
	pantalla.set_at( ( (xc + x) , (yc - y)),color)
	pantalla.set_at( ( (xc - x) , (yc - y)),color)
	pantalla.set_at( ( (xc + y) , (yc + x)),color)
	pantalla.set_at( ( (xc - y) , (yc + x)),color)
	pantalla.set_at( ( (xc + y) , (yc - x)),color)
	pantalla.set_at( ( (xc - y) , (yc - x)),color)

def CircleMidPoint(pantalla,xc, yc, r, color):
	y = 0
	z = 0
	x = 0
	y = r
	p = 1 - r
	deltaE=3
	deltaSE= 5- r*2
	PlotPoint(pantalla, xc, yc, x, y, color)
	
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
		PlotPoint(pantalla,xc, yc, x, y, color)	
		pygame.display.flip()

#-------------------------------------------------------------------------------------
#Circunferencia con relleno
def PlotPoint2(pantalla, xc, yc, x, y, color):
	pantalla.set_at( ( (xc + x) , (yc + y)),color)
	pantalla.set_at( ( (xc - x) , (yc + y)),color)
	Linea_Bresenham(pantalla,xc+x,y+yc,xc-x,y+yc,color)
	pantalla.set_at( ( (xc + x) , (yc - y)),color)
	pantalla.set_at( ( (xc - x) , (yc - y)),color)
	Linea_Bresenham(pantalla,xc+x,yc-y,xc-x,yc-y,color)
	pantalla.set_at( ( (xc + y) , (yc + x)),color)
	pantalla.set_at( ( (xc - y) , (yc + x)),color)
	Linea_Bresenham(pantalla,xc+y,x+yc,xc-y,x+yc,color)
	pantalla.set_at( ( (xc + y) , (yc - x)),color)
	pantalla.set_at( ( (xc - y) , (yc - x)),color)
	Linea_Bresenham(pantalla,xc+y,yc-x,xc-y,yc-x,color)

def CirculoRelleno(pantalla,Cx, Cy, r,color):
	y = 0
	z = 0
	x = 0
	y = r
	p = 1 - r
	deltaE=3
	deltaSE= 5- r*2
	PlotPoint2(pantalla, Cx, Cy, x, y, color)
	
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
		PlotPoint2(pantalla,Cx, Cy, x, y, color)	
		pygame.display.flip()

#-------------------------------------------------------------------------------------
#Elipse sin relleno

def PlotPointel(pantalla, xc, yc, x, y, color):
	pantalla.set_at((xc+x,yc+y),color)
	pantalla.set_at((xc-x,yc+y),color)
	pantalla.set_at((xc+x,yc-y),color)
	pantalla.set_at((xc-x,yc-y),color)


def ElipseMidPoint(pantalla,xc,yc,rx,ry,color):
	ry2=ry*ry
	rx2=rx*rx
	twory2=2*ry2
	tworx2=2*rx2
	x=0
	y=ry
	p=0
	PlotPointel(pantalla,xc,yc,x,y,color)
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
		PlotPointel(pantalla,xc,yc,x,y,color)
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
		PlotPointel(pantalla,xc,yc,x,y,color)
	pygame.display.flip()
		
#-------------------------------------------------------------------------------------
#Elipse con relleno
def PlotPointel2(pantalla, xc, yc, x, y,color):
    pantalla.set_at((xc + x,yc + y),color)
    pantalla.set_at((xc - x,yc + y),color)
    pygame.draw.line(pantalla, color, (xc - x,yc + y),(xc + x,yc + y),1)
    pantalla.set_at((xc + x,yc - y),color)
    pantalla.set_at((xc - x,yc - y),color)
    pygame.draw.line(pantalla, color, (xc - x,yc - y),(xc + x,yc - y),1)

def EllipseMidPointRellenar(pantalla, xc, yc, rx, ry,color):
    ry2 = ry*ry;
    rx2 = rx*rx
    twory2 = 2 * ry2
    tworx2 = 2 * rx2
    x = 0
    y = ry
    PlotPointel2(pantalla,xc,yc,x,y,color)

    p = int(round(ry2 - rx2*ry + (0.7*rx2)))
    px = 0
    py = tworx2*y
    while (px < py):
        x = x + 1
        px = px + twory2
        if (p < 0):
            p = p + ry2 + px
        else:
            y = y - 1
            py = py - tworx2
            p = p + ry2 + px - py
        PlotPointel2(pantalla,xc,yc,x,y,color)
    p = round(ry2*(x+0.5)*(x+0.5) + rx2*(y-1)*(y-1) - rx2*ry2)    
    px = 0          
    py = tworx2*y
    while (y > 0):
        y = y - 1
        py = py - tworx2
        if (p > 0):
            p = p + rx2 - py
        else:
            x = x + 1
            px = px + twory2
            p = p + rx2 - py + px
        PlotPointel2(pantalla,xc,yc,x,y,color)


#-------------------------------------------------------------------------------------
#Parabola
def PlotPointpar(pantalla,x,y,color):
    pantalla.set_at((x,y),color)
    pantalla.set_at((x,-y),color)

def ParabolaMidPoint(pantalla, color, direccion,init,final):
    h = init[0]
    k = init[1]
    x = 0
    y = 0
    p = 1

    if direccion == "derecha":
        PlotPointpar(pantalla,x+h,y+k,color)
        PlotPointpar(pantalla,x+h,y-k,color)
        while x <= final:
            x = x+1
            if p>0:
                y = y+1
                p = p - y +1
            else:
                p = p+1
                PlotPointpar(pantalla,x+h,y+k,color)
                PlotPointpar(pantalla,x+h,y-k,color)
                
    if direccion == "izquierda":
        x = final
        PlotPointpar(pantalla,x+h,y+k,color)
        PlotPointpar(pantalla,x+h,y-k,color)
        while x > 0:
            x = x-1
            if p>0:
                y = y+1
                p = p - y +1
            else:
                p = p+1
                PlotPointpar(pantalla,x+h,y+k,color)
                PlotPointpar(pantalla,x+h,y-k,color)
                
    if direccion == "arriba":
            y = final
            PlotPointpar(pantalla,-x+h,-y-k,color)
            PlotPointpar(pantalla,x+h,-y-k,color)
            while y > 0:
                y = y-1
                if p>0:
                    x = x+1
                    p = p - x +1
                else:
                    p = p+1
                    PlotPointpar(pantalla,-x+h,-y-k,color)
                    PlotPointpar(pantalla,x+h,-y-k,color)
           

    if direccion == "abajo":
            PlotPointpar(pantalla,-x+h,-y-k,color)
            PlotPointpar(pantalla,x+h,-y-k,color)
            while y <= final:
                y = y+1
                if p>0:
                    x = x+1
                    p = p - x +1
                else:
                    p = p+1
                    PlotPointpar(pantalla,-x+h,-y-k,color)
                    PlotPointpar(pantalla,x+h,-y-k,color)

    pygame.display.flip()
#-------------------------------------------------------------------------------------
#Rectangulos sin relleno
def Rectangulo2(pantalla,x,y,largo,ancho,color):
    x1 = x
    y1 = y
    x2 = x1+largo
    y2 = y1
    x3 = x
    y3 = y1+ancho
    x4 = x+largo
    y4 = y + ancho
    Linea_Grosor (pantalla, x1, y1, x2, y2, color,2)
    Linea_Grosor (pantalla, x1, y1, x3, y3, color,2)
    Linea_Grosor (pantalla, x3, y3, x4, y4, color,2)
    Linea_Grosor (pantalla, x2, y2, x4, y4, color,2)
    pygame.display.flip()
 
def Rectangulo(pantalla,xi,yi,xf,yf,color):
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
    pygame.display.flip()
 
#-------------------------------------------------------------------------------------
#Rectangulos con relleno
def RectanguloRelleno2(pantalla,x,y,largo,ancho,color):
    x1 = x
    y1 = y
    x2 = x1+largo
    y2 = y1
    x3 = x
    y3 = y1+ancho
    x4 = x+largo
    y4 = y + ancho
    Linea_Grosor (pantalla, x1, y1, x2, y2, color,2)
    Linea_Grosor (pantalla, x1, y1, x3, y3, color,2)
    Linea_Grosor (pantalla, x3, y3, x4, y4, color,2)
    Linea_Grosor (pantalla, x2, y2, x4, y4, color,2)
    i = 0
    while i <= ancho:
        Linea_Grosor(pantalla, x1,y1+i,x2,y2+i,color,2)
        i+=1
    pygame.display.flip()

def RectanguloRelleno(pantalla,xi,yi,xf,yf,color):
    ancho = abs(xf - xi)
    largo = abs(yf - yi)
    pygame.draw.rect(pantalla,color,[xi,yi,ancho,largo])
    pygame.display.flip()
