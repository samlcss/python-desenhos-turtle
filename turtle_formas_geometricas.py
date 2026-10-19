# -*- coding: utf-8 -*-
"""
Desenha múltiplas formas geométricas (quadrado e triângulo colorido) em uma mesma tela.
"""

import turtle

def quadrado(t, tamanho, graus=90):
    for _ in range(4):
        t.forward(tamanho)
        t.right(graus)

def triangulo(t, tamanho, graus=120):
    cores = ["red", "purple", "orange"]
    for i in range(3):
        t.color(cores[i])
        t.left(graus)
        t.forward(tamanho)

def main():
    screen = turtle.Screen()
    screen.title("Formas Geométricas com Turtle")
    screen.bgcolor("lightyellow")

    t = turtle.Turtle()
    t.pensize(4)
    t.color("blue")
    t.shape("turtle")
    t.speed(2)

    quadrado(t, 200, 90)
    triangulo(t, 150, 120)

    turtle.mainloop()

if __name__ == "__main__":
    main()
