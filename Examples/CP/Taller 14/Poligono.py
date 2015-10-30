import pygame,math
pygame.init()
tamano = ancho, alto = 500, 500
color = 255,255,255
pantalla = pygame.display.set_mode(tamano)
pantalla.fill(color)
espesor=1
def dibujarPoligono(vertices,n,espesor):
	i=0
	for i in range (i,n):
		pygame.draw.line(pantalla,(0,0,0),vertices[i],vertices[i+1],espesor)
		pygame.display.flip()
	pygame.draw.line(pantalla,(0,0,0),vertices[i],vertices[0],espesor)
	pygame.display.flip()

def DibujarPoligonoRegular(n,Centro,radio,espesor):
	alfa=0
	a=0
	b=0
	i=0
	vertices=[]
	alfa=2*math.pi/n
	for i in range (0,n+1):
		a=Centro[0]+(radio*math.cos((i-1)*alfa))
		b=Centro[1]+(radio*math.sin((i-1)*alfa))
		vertices.insert(i,(a,b))
	dibujarPoligono(vertices,n,espesor)
for i in range (0,80):
	DibujarPoligonoRegular(5,(150,225),i,5)

while 1:
   for event in pygame.event.get():
       if event.type == pygame.QUIT: 
           sys.exit()

