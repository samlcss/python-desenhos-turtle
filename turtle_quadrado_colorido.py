# -*- coding: utf-8 -*-
"""
Desenha um quadrado estilizado com cor de fundo, cor de traço e espessura personalizada.
"""

import turtle

def configurar_tela():
    screen = turtle.Screen()
    screen.title("Tartaruga Estilizada!")
    screen.bgcolor("lightyellow")

def main():
    configurar_tela()
    
    t = turtle.Turtle()
    t.shape("turtle")
    t.pensize(4)
    t.color("blue")
    t.speed(1)

    for _ in range(4):
        t.forward(200)
        t.right(90)

    turtle.done()

if __name__ == "__main__":
    main()
