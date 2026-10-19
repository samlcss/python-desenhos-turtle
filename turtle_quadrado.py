# -*- coding: utf-8 -*-
"""
Desenha um quadrado simples utilizando Turtle Graphics.
"""

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(2)

# Desenha os 4 lados do quadrado
for _ in range(4):
    t.forward(100)
    t.right(90)

turtle.done()
