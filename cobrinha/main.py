import pygame
from cobra.composição import *

pygame.init()
pygame.display.set_caption('Cobrinha Python')
larg, alt = 600, 400
tela = pygame.display.set_mode((larg, alt))
tempo = pygame.time.Clock()

cores = {'preto': (0, 0, 0),
         'branco': (255, 255, 255),
         'vermelho': (255, 0, 0),
         'verde': (0, 255, 0)}
        

quadrado = 20
velocidade = 12

rodando(quadrado, velocidade, cores, larg, alt, tela, tempo )