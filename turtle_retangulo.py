# -*- coding: utf-8 -*-
"""
Desenha um retângulo utilizando Turtle Graphics com delay de visualização.
"""

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(1)

# Desenha os lados do retângulo
t.forward(200)
t.right(90)
t.forward(100)
t.right(90)
t.forward(200)
t.right(90)
t.forward(100)

turtle.done()
