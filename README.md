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

 
