#Autor: Daniela Estrella Tovar
#Hacer una función que dados tres parametros relacionados con el círculo, dibuje figuras similares a las que realiza un espírografo.

import pygame
import math
import random

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)

#Funcion para generar color
def generarColor():
    rojo= random.randint(0,255)
    verde= random.randint(0,255)
    azul= random.randint(0,255)

    return(rojo,verde,azul)

# Estructura básica de un programa que usa pygame para dibujar
def dibujarFigura(r, R, l):
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        colorAleatorio = generarColor()
        for angulo in range(0, (360*(r//math.gcd(r,R))+1)):
            a = math.radians(angulo)
            k = r/R
            x = int(R*((1-k)*math.cos(a)+l*k*math.cos(((1-k)/k)*a)))
            y = int(R*((1-k)*math.sin(a)-l*k*math.sin(((1-k)/k)*a)))

            pygame.draw.circle(ventana, (colorAleatorio), (x + ANCHO//2, ALTO // 2 - y), 1)



        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(10)


    pygame.quit()



def main():
    r = int(input("Teclea con numeros enteros r: "))
    R = int(input("Teclea con números en enteros R: "))
    l= float(input("Teclea con números decimales l:"))

    dibujarFigura(r,R,l)



main()