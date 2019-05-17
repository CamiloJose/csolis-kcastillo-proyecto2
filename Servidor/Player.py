import pygame
#clase jugador puesta fuera de el cliente para
#evitar que un jugador cambie sus atributos
# y haga trampa en el juego
class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 5
    #crea el jugador
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    #teclas para moverse
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

# actualizar la imagen
    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
