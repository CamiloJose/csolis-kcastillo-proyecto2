#Proyecto 2. Taller de Programacion.
#Kenneth Castillo Herrera 2019062984
#Camilo Jose Solís Gonzales 2019048742
import pygame
from pygame.locals import *
import tkinter as TK
from tkinter import *
import time

#Variables utiliadas en el juego principal.
#Se desarrolla de esta manera para mantener el orden.
#Variables globales
pygame.init()
global resolucion

alto = 800
ancho = 800

global superficies


global objetos
menusong = pygame.mixer.music.load("music/menu_song.mp3")
basesong = pygame.mixer.music.load("music/base_song.mp3")
#spito = pygame.mixer.music.load("music/pito.mp3")
#spito1 = pygame.mixer.music.load("music/pito1.mp3")
sshot = pygame.mixer.Sound("music/shot.wav")
sshot1 = pygame.mixer.Sound("music/shot1.wav")
clock = pygame.time.Clock()
car_d = pygame.image.load("img/car_d.png")
car1_d = pygame.image.load("img/car1_d.png")
car_i = pygame.image.load("img/car_i.png")
car1_i = pygame.image.load("img/car1_i.png")
car_arr = pygame.image.load("img/car_arr.png")
car1_arr = pygame.image.load("img/car1_arr.png")
car_ab = pygame.image.load("img/car_ab.png")
car1_ab = pygame.image.load("img/car1_ab.png")
shot = pygame.image.load("img/laser.png")
shot1 = pygame.image.load("img/laser1.png")
auto = car_d
auto1 = car1_i
arbusto = pygame.image.load("img/arbusto.png")
fondo = pygame.image.load("img/fondo.png")
icono = pygame.image.load("img/icono.ico")
fuente1 = ("fuente/fast_race.ttf")
fuente = pygame.font.Font(fuente1, 30)
