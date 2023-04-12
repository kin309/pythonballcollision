# Colisão de Bolas em Python

Colisão de Bolas em Python é um código simples escrito em Python, que gera bolas que ficam quicando na tela e colidindo umas com as outras utilizando as leis da física, foi um dos primeiros programas que eu fiz, eu escolhi o Python por ser uma linguagem simples e quando conclui o código fiquei muito feliz com o resultado e apartir daí comecei a me interessar mais sobre programação.

## Tela do programa

![window](https://user-images.githubusercontent.com/30506992/172245354-da1639ab-14aa-40ba-8a4c-bdaa5515215b.png)

![balls](https://user-images.githubusercontent.com/30506992/172246258-c672f40f-f33d-4c78-a817-d9f90cf5da21.gif)

# Explicação do Código

Para criar esse programa eu utilizei principalmente a biblioteca pygame, que é a melhor biblioteca para criação de jogos em Python.

## Imports

import pygame
import sys
import time
import numpy as np
from random import randrange

Utilizei também outras bibliotecas, para algumas funcionalidades, como por exemplo: 
  1. random: Uma biblioteca que gera números aleatórios.
  2. time: Consegue pausar a execução de código por um período de tempo, além de fornecer data e hora atuais.
  3. numpy: Utilizado para realizar algumas operações matemáticas mais complexas, que foi bastante útil na parte de codificar a física do programa.

## Bolas

O construtor da classe Ball, que possui uma série de parâmetros que definem as propriedades das bolas, como por exemplo, a velocidade atual, a fricção, o tamanho, a cor, etc.

```
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
 ```
 
 Método principal da classe Ball responsável por todas as funcionalidades da classe, e por todos os comportamentos físicos do objeto
 
 ```
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
                
 ```
 ## Outros Métodos e Instâncias dos Objetos
 
 Método responsável pela colisão das bolas
 
 ```
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
 ```
 
 Método responsável por transferir a velocidade de uma bola para outra utilizando a fórmula da colisão elástica
 
 ```
 def compute_velocity(v1, v2, m1, m2, x1, x2):
    return v1 - (2 * m2 / (m1 + m2)) * np.dot(v1 - v2, x1 - x2) / np.linalg.norm(x1 - x2) ** 2 * (x1 - x2)
 ```
 
 Definição das constantes

```
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

```

Instanciação dos Objetos

```
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

```

Método principal onde ocorre o loop do jogo e o programa é executado

```
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
```
