import pygame , sys
import math

pygame.init()

#LIBRERIA DE FUNCIONES



#funciones para dibujar lineas

#--------------------------------lineaDDA-------------------------------------
def lineaDDA(pantalla,x1,y1,x2,y2,color):
    dx = x2 - x1
    dy = y2 - y1
    numeropasos = abs(dy)
    if abs(dx) > abs(dy):
        numeropasos = abs(dx)
    incrementoX = incrementoY = 0
    if numeropasos <>0:
        incrementoX = 1.0 * dx / numeropasos
        incrementoY = 1.0 * dy / numeropasos
    x, y = x1, y1
    pantalla.set_at((int(x), int(y)),color)
    for k in range(numeropasos):
        x = x + incrementoX
        y = y + incrementoY
        
        pantalla.set_at((int(x),int(y)),color)
    pygame.display.flip()


#--------------------------linea_Bresenham-------------------------------------
def Bresenham(screen, pini, pend, color):

    dx = abs(pend[0] - pini[0])
    dy = abs(pend[1] - pini[1])

    incx = 1
    
    if (pend[0] < pini[0]):
            incx = -1
    
    incy = 1
    
    if (pend[1] < pini[1]):
            incy = -1
       
    x = pini[0]
    y = pini[1]

    if (dx > dy):
       screen.set_at((x,y),color)
       p = 2*dy - dx
       incNE = 2 * (dy - dx)
       incE = 2 * dy
       for i in range(dx - 2):
          if p >= 0:
             y += incy
             p += incNE
          else:
             p += incE
          x += incx
          screen.set_at((x,y), color)
    else:
       screen.set_at((x,y), color)
       p = 2*dy - dx
       incNE = 2 * (dx - dy)
       incE = 2 * dx
       for i in range(dy - 2):
          if p >= 0:
             x += incx
             p += incNE
          else:
             p += incE
          y += incy
          screen.set_at((x,y), color)


#-----------------------------linea punto medio------------------------------
def lineaPuntomedio(pantalla,x0,y0,x1,y1,color):
    x = y = dx = dy = xend = p = incE = incNE = 0
    
    dx = x1 - x0
    dy = y1 - y0
    p = 2*dy - dx
    incE = 2*dy
    incNE = 2*(dy-dx)

    if x0 > x1:
     x = x1
     y = y1
     xend = x0
    else: 
      x = x0
      y = y0
      xend = x1;

    while x <= xend:
        pantalla.set_at((x,y),color)
        x = x + 1
        if (p <= 0):
          p = p + incE
        else: 
         y = y + 1
         p = p + incNE
    pygame.display.flip()
#------------------------------------------------------------------------------

#funciones para dibujar poligonos
    
#--------------------------poligonos regulares----------------------------------
def dibujarPoligono(vertices, N, pantalla, color):
    for i in range (N):
        pygame.draw.line(pantalla,color, vertices[i-1],vertices[i],1)
        pygame.display.flip()
    pygame.draw.line(pantalla,color, vertices[N-1],vertices[0],1)
    pygame.display.flip()

def poligonoRegular(N, (Cx,Cy), radio, pantalla, color):
    vertices = []
    alfa = (2 * math.pi)/N
    for i in range (N):
        a = Cx + (radio * math.cos((i-1)*alfa))
        b = Cy + (radio * math.sin((i-1)*alfa))
        vertices.insert(i, (a, b))

    dibujarPoligono(vertices, N, pantalla, color)    
    pygame.display.flip()


#--------------------------poligonos irregulares---------------------------------

def lineaRecta(pantalla,x1,y1,x2,y2,color):
    dx = x2 - x1
    dy = y2 - y1
    numeropasos = abs(dy)
    if abs(dx) > abs(dy):
        numeropasos = abs(dx)
    incrementoX = incrementoY = 0
    if numeropasos <>0:
        incrementoX = 1.0 * dx / numeropasos
        incrementoY = 1.0 * dy / numeropasos
    x, y = x1, y1
    pantalla.set_at((int(x), int(y)),color)
    for k in range(numeropasos):
        x = x + incrementoX
        y = y + incrementoY
        pantalla.set_at((int(x),int(y)),color)
    pygame.display.flip()


def poligonoIrregular(pantalla, vectorX,vectorY,color):
    i = 0
    while i < len(vectorX)-1:
        lineaRecta(pantalla,vectorX[i],vectorY[i],vectorX[i+1],vectorY[i+1],color)
        i = i + 1
    lineaRecta(pantalla,vectorX[0],vectorY[0],vectorX[i],vectorY[i],color)
        
x = [100,150,200,270,330,210]
y = [100,50,90,65,95,180]
#pygame.display.flip()
#---------------------------------------------------------------------------------

#funciones para dibujar circulos

#-------------------------circunferencias----------------------------------------
def PlotPoint(pantalla, xc, yc, x, y,color):
    pantalla.set_at((xc + x,yc + y),color)
    pantalla.set_at((xc - x,yc + y),color)
    pantalla.set_at((xc + x,yc - y),color)
    pantalla.set_at((xc - x,yc - y),color)
    pantalla.set_at((xc + y,yc + x),color)
    pantalla.set_at((xc - y,yc + x),color)
    pantalla.set_at((xc + y,yc - x),color)
    pantalla.set_at((xc - y,yc - x),color)

def CircleMidPoint(pantalla, xc, yc, r,color):
    x = 0
    y = r
    p = 1 - r
    deltaE = 3
    deltaSE = 5 - r*2
    PlotPoint(pantalla,xc,yc,x,y,color)

    while (x < y):
        x = x + 1
        if (p < 0):
            p = p + deltaE
            deltaE = deltaE + 2
            deltaSE = deltaSE + 2
        else:
            y = y - 1
            p = p + deltaSE
            deltaE = deltaE + 2
            deltaSE = deltaSE + 4
        PlotPoint(pantalla,xc,yc,x,y,color)

#---------------------------elipse----------------------------------------------
def PlotPoint12(pantalla, xc, yc, x, y,color):
    pantalla.set_at((xc + x,yc + y),color)
    pantalla.set_at((xc - x,yc + y),color)
    #pygame.draw.line(pantalla, (0,0,0), (xc - x,yc + y),(xc + x,yc + y),1)
    pantalla.set_at((xc + x,yc - y),color)
    pantalla.set_at((xc - x,yc - y),color)
    #pygame.draw.line(pantalla, (0,0,0), (xc - x,yc - y),(xc + x,yc - y),1)

def EllipseMidPoint(pantalla, xc, yc, rx, ry,color):
    ry2 = ry*ry;
    rx2 = rx*rx
    twory2 = 2 * ry2
    tworx2 = 2 * rx2
    x = 0
    y = ry
    PlotPoint12(pantalla,xc,yc,x,y,color)

    p = round(ry2 - rx2*ry + (0.25*rx2))
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
        PlotPoint12(pantalla,xc,yc,x,y,color)

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
        PlotPoint12(pantalla,xc,yc,x,y,color)
#-------------------------------------------------------------------------------

#funciones para recortar

#--------------------------recorte de puntos-------------------------------------
def recorte(xmin, xmax, ymin, ymax):
    i = 0
    j = 0
    for i in range(510):
        for j in range(373):
            if ((j < ymin) or (j > ymax) or (i < xmin) or (i > xmax)):
                pantalla.set_at((i, j), blanco)
                
        j = 0

#--------------------------recorte de lineas--------------------------------------
def recorte(xmin, xmax, ymin, ymax):
    i = 0
    j = 0
    for i in range(500):
        for j in range(500):
            if ((j < ymin) or (j > ymax) or (i < xmin) or (i > xmax)):
                pantalla.set_at((i, j), negro)
                
        j = 0

#-----------------------------recorte de imagenes---------------------------------
def corte(Pantalla,Xmin, Xmax, Ymin, Ymax,alto,ancho,color):
    i = 0
    f = 0
    for i in range(alto):
        for f in range(ancho):
            if ((f < Ymin) or (f > Ymax) or (i < Xmin) or (i > Xmax)):
                Pantalla.set_at((i, f), color)
                
        k = 0
#------------------------------------------------------------------------------------
#funciones para rellenar

#----------------------------rellenar poligonos rregulares--------------------------
def dibujarPoligono1(vertices, N, pantalla, color):
    for i in range (N):
        pygame.draw.line(pantalla,color, vertices[i-1],vertices[i],2)
        pygame.display.flip()
    pygame.draw.line(pantalla,color, vertices[N-1],vertices[0],2)
    pygame.display.flip()
    
def poligonoRegularRelleno(N, (Cx,Cy), radio, pantalla, color):
    vertices = []
    alfa = (2 * math.pi)/N
    for r in range (radio):
        for i in range (N):
            a = Cx + (r * math.cos((i-1)*alfa))
            b = Cy + (r * math.sin((i-1)*alfa))
            vertices.insert(i, (a, b))
        
        dibujarPoligono1(vertices, N, pantalla, color)
        pygame.display.flip()

#-------------------------rellenar circunferencia-----------------------------------

def PlotPoint1(pantalla, xc, yc, x, y,color):
    pantalla.set_at((xc + x,yc + y),color)
    pantalla.set_at((xc - x,yc + y),color)
    pygame.draw.line(pantalla, color, (xc - x,yc + y),(xc + x,yc + y),1)
    pantalla.set_at((xc + x,yc - y),color)
    pantalla.set_at((xc - x,yc - y),color)
    pygame.draw.line(pantalla, color, (xc - x,yc - y),(xc + x,yc - y),1)
    pantalla.set_at((xc + y,yc + x),color)
    pantalla.set_at((xc - y,yc + x),color)
    pygame.draw.line(pantalla, color, (xc - y,yc + x),(xc + y,yc + x),1)
    pantalla.set_at((xc + y,yc - x),color)
    pantalla.set_at((xc - y,yc - x),color)
    pygame.draw.line(pantalla, color, (xc - y,yc - x),(xc + y,yc - x),1)


def CircleMidPointRellenar(pantalla, xc, yc, r, color):
    x = 0
    y = r
    p = 1 - r
    PlotPoint1(pantalla,xc,yc,x,y,color)

#se cicla hasta trazar todo un octante 

    while (x < y):
        x = x + 1
        if (p < 0):
            p = p + 2*x + 1
        else:
            y = y - 1
            p = p + 2*(x - y) + 1
        PlotPoint1(pantalla,xc,yc,x,y,color)

#-----------------------------rellenar elipse-----------------------------------------

def PlotPoint2(pantalla, xc, yc, x, y,color):
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
    PlotPoint2(pantalla,xc,yc,x,y,color)

    p = round(ry2 - rx2*ry + (0.25*rx2))
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
        PlotPoint2(pantalla,xc,yc,x,y,color)

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
        PlotPoint2(pantalla,xc,yc,x,y,color)
