'''
Taller 23
Implementar el recorte de imagenes usando como area de recorte
un poligono irregular (Utilizar el mouse para definir el area de recorte)

'''
import sys, pygame

pygame.init()
tamano = ancho, alto = 800, 500
color = 255,255,255
pantalla = pygame.display.set_mode(tamano)
pygame.display.set_caption('Recorte')
pantalla.fill(color)
imagen = pygame.image.load("warner.jpg") 
pantalla.blit(imagen,(50,0))
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
        vertices.append(vertices2[i])

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
    
    Linea_Punto_Medio(0,0,0,500)
    Linea_Punto_Medio (800, 0, 800,500)
    
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

def Cortar():
    vertex=list()
    while True:
        pygame.event.wait()
        pygame.event.get()
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            posx2,posy2 = pygame.mouse.get_pos()
            if(vertex.count([posx2,posy2])==0):
                vertex.append([posx2,posy2])
        elif mouse[2]:
            FillAreas(vertex)
            break;




def main():
    Cortar()
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == "__main__":
    main()
