'''
Taller 25 Hacer un programa que reciba angulo y velocidad inicial, para un objeto
que se lanza en movimiento parabolico.
El programa debe mostrar el lanzamiento del objeto, y debe verificar si el objeto
alcanza un muro.
'''
import pygame, sys, math,time
pygame.init()


colorfondo = 255, 255, 255
tamano = ancho, alto = 1350, 600
pantalla = pygame.display.set_mode(tamano)
pygame.display.set_caption('MOVIMIENTO')
fondo = pygame.image.load("fondo.jpg")
cerdo = pygame.image.load("cerdo.png")
angry = pygame.image.load("angry.png")
explosion = pygame.image.load("explo.png")

sprite1 = pygame.sprite.Sprite()
sprite1.image = angry
sprite1.rect = angry.get_rect()

sprite2 = pygame.sprite.Sprite()
sprite2.image = cerdo
sprite2.rect = cerdo.get_rect()

pantalla.blit(fondo,(0,0))
pantalla.blit(angry,(0,500))
pantalla.blit(cerdo,(1080,450))
pygame.display.flip()

vo = int(input("Ingrese velocidad inicial >> "))
angulo_inicial = int(input("Ingrese angulo inicial >> "))
angulo_inicial = angulo_inicial*(math.pi/180)
vy = abs(int(vo*math.sin(angulo_inicial)))
vx = abs(int(vo*math.cos(angulo_inicial)))

velocidad = [vx,-vy]
sprite1.rect.top = 499
sprite1.rect.left = 0
sprite2.rect.left = 1080
sprite2.rect.top = 450 
pygame.mixer.music.load("explosion.mp3")

run = True
flag = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
	       run = False
    sprite1.rect = sprite1.rect.move(velocidad)
    if sprite1.rect.top < 0:
        velocidad[1] = -velocidad[1]

    if sprite1.rect.bottom > alto:
        velocidad = [0,0]

    if pygame.sprite.collide_rect(sprite1,sprite2):
        pantalla.blit(fondo,(0,0))
        velocidad = [0,0]
        sprite1.rect.top = 499
        sprite1.rect.left = 0
        sprite2.rect.left = 1080
        sprite2.rect.top = 450 
        pantalla.blit(explosion,(1000,365))
        pygame.mixer.music.play(1)
        flag = False

    if flag:
        pantalla.blit(fondo,(0,0))
        pantalla.blit(angry,(sprite1.rect.left,sprite1.rect.top))
        pantalla.blit(cerdo,(sprite2.rect.left,sprite2.rect.top))

    pygame.display.flip()

