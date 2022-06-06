import pygame
import sys
import time
import numpy as np
from random import randrange


class Ball:
    def __init__(self, x, y, speedx, speedy, color, diametro = 60, gravidade = 0.0002, accelerationx=0, friccao = 0.0009,
                 constituicao = 0.09):
        self.x = x
        self.y = y
        self.speedx = speedx
        self.speedy = speedy
        self.accelerationy = gravidade
        self.accelerationx = accelerationx
        self.constituicao = constituicao
        self.friccao = friccao
        self.speed = (self.speedx ** 2 + self.speedy **2) ** 0.5
        self.color = color
        self.diametro = diametro
        self.raio = diametro/2
        self.tempo_no_chao = 0
    def principal(self):
        pygame.draw.ellipse(janela, self.color, (self.x - self.raio, self.y - self.raio, self.diametro, self.diametro))

        self.x += self.speedx
        self.y += self.speedy
        self.speedy += self.accelerationy
        self.speedx += self.accelerationx

        # Colisão lado esquerdo
        if self.x - self.raio <= 0:
            self.x = 0.1 + self.raio
            self.speedx = (-self.speedx)+(self.speedx*self.constituicao+0.00111)

        # Colisão lado direito
        if self.x + self.raio >= janela_lar:
            self.x = janela_lar - 0.1 - self.raio
            self.speedx = (-self.speedx)+(self.speedx*self.constituicao+0.00111)

        # Colisão em cima
        if self.y - self.raio <= 0:
            self.y = 0 + self.raio
            self.speedy = (-self.speedy)-(self.speedy*self.constituicao+0.00111)

        # Colisão em baixo
        if self.y + self.raio >= janela_alt - 0.1:
            self.y = janela_alt - 0.2 - self.raio
            self.speedy = (-self.speedy) + (self.speedy * self.constituicao + 0.00241)
            self.speedx = self.speedx - self.speedx * self.friccao

            # Check se a bola está no chão
            if self.y + self.raio > 599.6:
                self.tempo_no_chao += 1
                if self.tempo_no_chao > 50:
                    self.speedy = 0
                    self.accelerationy = 0
                    self.y = 599.9 - self.raio
            else:
                self.tempo_no_chao = 0

def checkcollisions():
    for i in range(len(balls)):
        for j in range(len(balls) - 1, i, -1):
            distancia_bolas = ((balls[i].x - balls[j].x)**2 + (balls[i].y - balls[j].y)**2)**0.5
            if distancia_bolas <= balls[i].raio + balls[j].raio:
                    if i != j:
                        vb1 = np.array([balls[i].speedx, balls[i].speedy])
                        vb2 = np.array([balls[j].speedx, balls[j].speedy])
                        xb1 = np.array([balls[i].x, balls[i].y])
                        xb2 = np.array([balls[j].x, balls[j].y])
                        balls[i].speedx, balls[i].speedy = compute_velocity(vb1, vb2, ball1.raio, ball2.raio, xb1, xb2)
                        balls[j].speedx, balls[j].speedy = compute_velocity(vb2, vb1, ball1.raio, ball2.raio, xb2, xb1)



def compute_velocity(v1, v2, m1, m2, x1, x2):
    return v1 - (2 * m2 / (m1 + m2)) * np.dot(v1 - v2, x1 - x2) / np.linalg.norm(x1 - x2) ** 2 * (x1 - x2)

janela_lar = 800
janela_alt = 600

black = (00, 00, 00)
gray = (80, 80, 80)
white = (255, 255, 255)
green = (20, 205, 20)
red = (190, 20, 20)
blue = (20, 20, 190)
yellow = (230, 220, 20)
pink = (200, 30, 200)
nao = (20, 215, 190)
purpleblue = (70, 20, 205)
purplered = (215, 20, 70)
bleue = (210, 90, 110)
gren = (230, 130, 20)

pygame.init()
janela = pygame.display.set_mode((janela_lar, janela_alt))


ball1 = Ball(x=80, y=80, speedx=randrange(-4, 4)/10, speedy=-0.4, color=green)
ball2 = Ball(x=120, y=310, speedx=randrange(-4, 4)/10, speedy=-0.4, color=blue)
ball3 = Ball(x=200, y=330, speedx=randrange(-4, 4)/10, speedy=-0.5, color=purplered)
ball4 = Ball(x=500, y=420, speedx=randrange(-4, 4)/10, speedy=-0.3, color=yellow)
ball5 = Ball(x=350, y=240, speedx=randrange(-4, 4)/10, speedy=-0.4, color=red)
ball6 = Ball(x=160, y=160, speedx=randrange(-4, 4)/10, speedy=-0.3, color=bleue)
ball7 = Ball(x=240, y=620, speedx=randrange(-4, 4)/10, speedy=-0.3, color=pink)
ball8 = Ball(x=450, y=660, speedx=-randrange(-4, 4)/10, speedy=-0.5, color=nao)
ball9 = Ball(x=710, y=710, speedx=randrange(-4, 4)/10, speedy=-0.5, color=purpleblue)
ball10 = Ball(x=340, y=540, speedx=randrange(-4, 4)/10, speedy=-0.5, color=gren)

balls = [ball1, ball2, ball3, ball4, ball5, ball6, ball7, ball8, ball9, ball10]


def close():
    pygame.quit()
    sys.exit()


def principal():
    loop = True

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()

        for ball in balls:
            pass
            # ball.forca_aplicada()
        janela.fill(black)
        checkcollisions()
        for ball in balls:
            ball.principal()
        pygame.display.update()


principal()
