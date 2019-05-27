#Proyecto 2. Taller de Programacion.
#Kenneth Castillo Herrera 2019062984
#Camilo Jose Solís Gonzales 2019048742
import pygame
from pygame.locals import *
import tkinter as TK
from tkinter import *
import time
from Clases import *
from Variables import *
from random import *
#Juego principal.
#Se desarrolla de esta manera para mantener el orden.

pygame.init()
pantalla = pygame.display.set_mode([ancho,alto])
pantalla = pygame.display.set_mode([ancho,alto])
def TranscicionScene(mensaje, niv1):
    pygame.display.update()
    vel = 5
    niv = niv1
    pantalla
    pantalla.blit(fondo,(0,0)) #Esto crea el fondo de la Scena
    fuentee1 = "fuente/fast_race.ttf"#Acá se observa como se crean las letras que aparecen en pantalla.
    fuente = pygame.font.Font(fuentee1, 80)
    fuente1 = pygame.font.Font(fuentee1, 55)
    texto = fuente.render(mensaje , 0, (0, 0, 0))
    texto1 = fuente1.render("Precione cualquier tecla para continuar", 0, (5, 5, 5))
    pantalla.blit(texto,(300, 300))#Aca se dibujan los Textos
    pantalla.blit(texto1,(110, 400))
    pygame.display.set_caption("Fast Race Game 1.0")
    bandera = True
    
    while bandera:
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bandera = False
            elif event.type == pygame.KEYDOWN:
                if mensaje == "Game Pause":
                    LevelScene(vel)
                if niv == 0:
                    if mensaje == "Nivel 1":
                        niv += 1
                        LevelScene(vel)
                        print("Nivel 1")
                    if mensaje == "Nivel 2":
                        vel = vel + 5
                        niv += 1
                        LevelScene(5)
                    if mensaje == "Ultima Ronda":
                        vel = vel + 5
                        niv += 1
                        LevelScene(5)
    
def LevelScene(vel):
    basesong
    pygame.mixer.music.play()
    vel_c = 10
    t_inicial = time.time()
    pygame.display.update()
    pantalla
    bandera = True
    c_x = 1
    c_y = 300
    c1_x = 1
    c1_y = 600
    cs_x = 0
    c1s_x = 0

    """a_x = random.randint(815, 830)
    a_y = random.randint(0, 800)
    
    a1_x = random.randint(815, 830)
    a1_y = random.randint(0, 800)
    
    a2_x = random.randint(815, 830)
    a2_y = random.randint(0, 800)
    
    a3_x = random.randint(815, 830)
    a3_y = random.randint(0, 800)"""
    while bandera:
        
        clock.tick(60)
        pygame.display.update()
        pantalla.fill((236, 226, 198))
        pantalla.blit(car_d,(c_x,c_y))
        pantalla.blit(car1_d,(c1_x, c1_y))
        
        """pantalla.blit(arbusto,(a_x, a_y))
        pantalla.blit(arbusto,(a1_x, a1_y))
        pantalla.blit(arbusto,(a2_x, a2_y))
        pantalla.blit(arbusto,(a3_x, a3_y))
        a_x -= 5
        a1_x -= 5
        a2_x -= 5
        a3_x -= 5
        if a_x < 0:
            a_x = random.randint(815, 830)
            a_y = random.randint(0, 800)
        if a1_x < 0:
            a1_x = random.randint(815, 830)
            a1_y = random.randint(0, 800)
        if a2_x < 0:
            a2_x = random.randint(815, 830)
            a2_y = random.randint(0, 800)
        if a3_x < 0:
            a3_x = random.randint(815, 830)
            a3_y = random.randint(0, 800)"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bandera = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    TranscicionScene("Game Pause")
                if event.key == pygame.K_w:
                    c_y -= vel_c
                if event.key == pygame.K_s:
                    c_y += vel_c
                if event.key == pygame.K_a:
                    c_x -= vel_c
                if event.key == pygame.K_d:
                    c_x += vel_c
                if cs_x <= 0:
                    if event.key == pygame.K_c:
                        sshot.play()
                        cs_x = c_x + 180
                        cs_y = c_y + 45
                        
                if event.key == pygame.K_UP:
                    c1_y -= vel_c
                if event.key == pygame.K_DOWN:
                    c1_y += vel_c
                if event.key == pygame.K_LEFT:
                    c1_x -= vel_c
                if event.key == pygame.K_RIGHT:
                    c1_x += vel_c
                if c1s_x <= 0:
                    if event.key == pygame.K_SPACE:
                        sshot1.play()
                        c1s_x = c1_x + 180
                        c1s_y = c1_y + 45
                        
        if 0 < cs_x < 800:
            pantalla.blit(shot, (cs_x, cs_y))
            cs_x += 10
            if cs_x > 800:
                cs_x = 0
        if 0 < c1s_x < 800:
            pantalla.blit(shot, (c1s_x, c1s_y))
            c1s_x += 10
            if c1s_x > 800:
                c1s_x = 0
    pygame.mixer.music.stop()
    pygame.display.update()             
    pygame.quit()
def MainScene(niv):
    menusong
    pygame.mixer.music.play()
    o = 0
    pantalla
    pygame.display.update()
    vel = 5
    pantalla
    pantalla.blit(fondo,(0,0)) #Esto crea el fondo de la Scena
    fuentee1 = "fuente/fast_race.ttf"#Acá se observa como se crean las letras que aparecen en pantalla.
    fuente = pygame.font.Font(fuentee1, 80)
    fuente1 = pygame.font.Font(fuentee1, 55)
    texto = fuente.render("Bienvenido", 0, (0, 0, 0))
    texto1 = fuente1.render("En momentos continuaremos", 0, (5, 5, 5))
    pantalla.blit(texto,(300, 300))#Aca se dibujan los Textos
    pantalla.blit(texto1,(190, 400))
    pygame.display.set_caption("Fast Race Game 1.0")
    clock.tick(60)
    bandera = True
    pygame.display.update()
    
    while bandera:
        clock.tick(60)
        o = o + 1
        pygame.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bandera = False
            elif o > 600:
                if niv == 1:
                    TranscicionScene("Nivel 1", 0)
                if niv == 2:
                    TranscicionScene("Nivel 2", 0)
                if niv == 3:
                    TranscicionScene("Ultima Ronda", 0)
            
    pygame.quit()
    
   
#def MenuScene():


MainScene(1)
pygame.quit()
