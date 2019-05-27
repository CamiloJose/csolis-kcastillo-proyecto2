#Proyecto 2. Taller de Programacion.
#Kenneth Castillo Herrera 2019062984
#Camilo Jose Solís Gonzales 2019048742
import pygame
from pygame.locals import *
import tkinter as TK
from tkinter import *
import time

#Clases utiliadas en el juego principal.
#Se desarrolla de esta manera para mantener el orden.
class auto:
    def __init__(self, pos_x, pos_y, image):
        self.image = pygame.image.load(image)
        sef.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
        
    
    def dibujar(self, pantalla, dibujar_rect):
        pantalla.blit(self.imagen, self.rect)
        if pintar_rect:
            pygame.draw.rect(pantalla, (255,0,0), self.rect)
        

class objecto:
    def __init__(self, pos_x, pos_y, image):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
		

    def dibujar(self, pantalla, pos_x, pos_y):
        pantalla.blit(self.imagen, self.rect)
		
