'''
complementar el taller 20 agregando el 
algoritmo para manejar aristas horizontales
'''
import sys,math,pygame

pygame.init()

color=0,0,255
colorfondo = 255, 255, 255
tamano = ancho, alto = 1100,800
pantalla = pygame.display.set_mode(tamano)
pantalla.fill(colorfondo)

pygame.display.flip()

vector=[]

for i in range(800):
    vector.append([])

def Linea_Punto_Medio ( Xi, Yi, Xf, Yf):
    xaux,yaux=-1,-1
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
    if(vector[y].count(x)==0):
        vector[y].append(x)
    tempo=False
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
                tempo=True
                p = p + incNE
            pantalla.set_at((x,y),color)
            if(tempo):
                xaux=x
                yaux=y
                if(vector[y].count(x)==0):
                    vector[y].append(x)
                tempo=False
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
            xaux=x
            yaux=y
            if(vector[y].count(x)==0):
                    vector[y].append(x)
    if(xaux!=-1 and yaux!=-1 and yaux==Yf):
        vector[yaux].remove(xaux)
    pygame.display.flip()


def FillAreas(vertices2):
    vertices = list()
    for i in range(len(vertices2)):
        vertices.append(vertices2)

    vertices.sort()
    N = len(vertices)
    for i in range(N-1):
        Linea_Punto_Medio (vertices2[i][0], vertices2[i][1], vertices2[i+1][0], vertices2[i+1][1])
    Linea_Punto_Medio (vertices2[N-1][0], vertices2[N-1][1], vertices2[0][0], vertices2[0][1])
    
    for i in range(N-2):
        if vertices2[i][1]>vertices2[i+1][1] and vertices2[i+2][1]>vertices2[i+1][1]:
            if(vector[vertices2[i+1][1]].count(vertices2[i+1][0])==1):
                vector[vertices2[i+1][1]].remove(vertices2[i+1][0])

        elif vertices2[i][1]<vertices2[i+1][1] and vertices2[i+2][1]<vertices2[i+1][1]:
            if(vector[vertices2[i+1][1]].count(vertices2[i+1][0])==1):
                vector[vertices2[i+1][1]].remove(vertices2[i+1][0])

    if vertices2[N-1][1]>vertices2[0][1] and vertices2[1][1]>vertices2[0][1]:
        if(vector[vertices2[0][1]].count(vertices2[0][0])==1):
            vector[vertices2[0][1]].remove(vertices2[0][0])
            
    elif vertices2[N-2][1]<vertices2[N-1][1] and vertices2[0][1]<vertices2[N-1][1]:
        if(vector[vertices2[N-1][1]].count(vertices2[N-1][0])==1):
            vector[vertices2[N-1][1]].remove(vertices2[N-1][0])

    
    for i in range(len(vector)):
        vector[i].sort()
        p=0
        for j in range(len(vector[i])-1):
            if p==0:
                Linea_Punto_Medio(vector[i][j],i,vector[i][j+1],i)
                pygame.display.flip()
                p=1
            elif p==1:
                p=0

def main():
    vertices = [[100,50],[150,50],[200,0],[250,50],[300,50],[350,150],[360,250],[250,200],[100,250],[150,150]]
    #vertices.append([50,100])
   # vertices.append([50,500])
    #vertices.append([200,300])
   
#vertices = [[100,50],[100,250],[150,50],[150,150],[200,0],[250,50],[250,200],[300,50],[350,150],[360,250]]
    vertices2 = [[730,220],[530,0],[630,250],[890,290]]
    vertices3 = [[280,230],[330,400],[580,600],[700,550]]
    vertices4 = [[20,40],[40,40],[20,100],[40,100]]
    FillAreas(vertices)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
main()
