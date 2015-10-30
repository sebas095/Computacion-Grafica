import random
import pygame
from pygame.locals import *
import sys
import ConfigParser

#Definicion de Colores
NEGRO = (0,0,0)
BLANCO = (255,255,255)
AZUL = (0, 0, 255)

ALTO = 600
ANCHO = 800

class Sprite(pygame.sprite.Sprite):
    def __init__(self, imagefile, rect):
        pygame.sprite.Sprite.__init__(self)

        self.setPosition(0, 0)

        self.spritesheet = pygame.image.load(imagefile)
        self.setRect(rect)

    def setPosition(self, x, y):
        self.x = x
        self.y = y
        
    def setRect(self, rect):
        self.image = self.spritesheet.subsurface(rect)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


class Jugador (pygame.sprite.Sprite):
	var_x = 0
	var_y = 0
	muros = None

	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([15, 15])
		self.image.fill(BLANCO)

		self.rect = self.image.get_rect()
		self.rect.y += y
		self.rect.x += x

	def velocidad(self, x, y):
		self.var_x += x
		self.var_y += y

	def update(self):
		self.rect.x += self.var_x

		lista_golpes = pygame.sprite.spritecollide(self, self.muros, False)

		for bloque in lista_golpes:
			if self.var_x >0:
				self.rect.right = bloque.rect.left
			else:
				self.rect.left = bloque.rect.right

		self.rect.y += self.var_y
		lista_golpes = pygame.sprite.spritecollide(self, self.muros, False)

		for bloque in lista_golpes:
			if self.var_y > 0:
				self.rect.bottom = bloque.rect.top
			else:
				self.rect.top = bloque.rect.bottom

class Muro(pygame.sprite.Sprite):
	def __init__(self, x, y, ancho, alto):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([ancho, alto])
		self.image.fill(AZUL)
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x


#Hero 
hero_mov_down = [ pygame.Rect(3, 3, 18, 30), \
              pygame.Rect(23, 4, 17, 29), \
              pygame.Rect(42, 4, 17, 29), ]

hero_mov_left = [ pygame.Rect(61, 3, 16, 30), \
              pygame.Rect(79, 4, 20, 29), \
              pygame.Rect(101, 4, 20, 29), ]

hero_mov_right = [ pygame.Rect(123, 3, 16, 30), \
              pygame.Rect(141, 4, 20, 29), \
              pygame.Rect(163, 4, 20, 29), ]

hero_mov_up = [ pygame.Rect(185, 4, 16, 29), \
              pygame.Rect(203, 5, 16, 28), \
              pygame.Rect(221, 5, 16, 28), ]



pygame.init()
pantalla = pygame.display.set_mode([ANCHO, ALTO])
pygame.display.set_caption("...Laberinto...")

lista_todos = pygame.sprite.Group()
lista_muros = pygame.sprite.Group()

#Muro(pos_x inicial, pos_y inicil, ancho, alto)

#Muros de restriccion
muro = Muro(0, 0, 800, 1)
lista_muros.add(muro)
lista_todos.add(muro)

muro = Muro(0, 0, 1, 600)
lista_muros.add(muro)
lista_todos.add(muro)

muro = Muro(0, 599,8600, 1)
lista_muros.add(muro)
lista_todos.add(muro)

muro = Muro(799, 0, 1, 600)
lista_muros.add(muro)
lista_todos.add(muro)

#muros del laberinto
muro = Muro(100, 0, 60, 500)
lista_muros.add(muro)
lista_todos.add(muro)

muro = Muro(200, 0, 60, 500)
lista_muros.add(muro)
lista_todos.add(muro)

muro = Muro(100, 0, 60, 500)
lista_muros.add(muro)
lista_todos.add(muro)


#Personaje
j = Jugador(50, 50)
j.muros = lista_muros
lista_todos.add(j)
num_frame = 0
reloj = pygame.time.Clock()

hero = Sprite("hero.png", pygame.Rect(3, 3, 18, 30))
hero.setPosition(90, 90)
hero.draw(pantalla)
pygame.display.flip()

fin = False


while not fin:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			fin = True

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				if num_frame >= len(hero_mov_left):
					num_frame = 0
        			hero.setRect(hero_mov_left[num_frame])
        			num_frame += 1
        			reloj.tick(15)
        			pygame.display.flip()
				j.velocidad(-3, 0)
			elif event.key == pygame.K_RIGHT:
				j.velocidad(3, 0)
			elif event.key == pygame.K_UP:
				j.velocidad(0, -3)
			elif event.key == pygame.K_DOWN:
				j.velocidad(0, 3)

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				j.velocidad(3, 0)
			elif event.key == pygame.K_RIGHT:
				j.velocidad(-3, 0)
			elif event.key == pygame.K_UP:
				j.velocidad(0, 3)
			elif event.key == pygame.K_DOWN:
				j.velocidad(0, -3)


	lista_todos.update()
	pantalla.fill(NEGRO)
	lista_todos.draw(pantalla)
	pygame.display.flip()
	reloj.tick(60)

pygame.quit()