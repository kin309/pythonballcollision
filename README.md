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

```class Ball:
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
