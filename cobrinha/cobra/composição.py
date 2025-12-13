
import pygame
import random
def rodando(quadrado, velocidade, cores, larg, alt, tela, tempo ):
    def cobra(tamanho, pixels):
        for pixels in pixels:
            pygame.draw.rect(tela, cores['branco'], [pixels[0], pixels[1], tamanho, tamanho])

    def pontuação(p):
        fonte = pygame.font.SysFont('Helvetica', 25)
        texto = fonte.render(f'Pontos: {p}', True, cores['vermelho'])
        tela.blit(texto, [1, 1])

    def escolhendo_velocidade(tecla):
        if tecla == pygame.K_DOWN:
            velocidade_x = 0
            velocidade_y = quadrado
        elif tecla == pygame.K_UP:
            velocidade_x = 0
            velocidade_y = -quadrado
        elif tecla == pygame.K_RIGHT:
            velocidade_x = quadrado
            velocidade_y = 0
        elif tecla == pygame.K_LEFT:
            velocidade_x = -quadrado
            velocidade_y = 0
        return velocidade_x, velocidade_y


    def gerador_comida():
        comida_x = round(random.randrange(0, larg - quadrado) / quadrado) * quadrado
        comida_y = round(random.randrange(0, alt - quadrado) / quadrado) * quadrado
        return comida_x , comida_y
        
    def desenhar_comida(tamanho, comida_x, comida_y):
        pygame.draw.rect(tela, cores['verde'], [comida_x, comida_y, tamanho, tamanho])
    fim = True
    x = larg/ 2
    y = alt / 2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []

    comida_x, comida_y = gerador_comida()
    
    while fim:
        tela.fill(cores['preto'])
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim = False
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = escolhendo_velocidade(evento.key)
        desenhar_comida(quadrado, comida_x, comida_y)

        if x < 0 or x >= larg or y < 0 or y >= alt:
            fim = False

        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim = False

        x += velocidade_x
        y += velocidade_y
        cobra(quadrado,pixels)
        pontuação(tamanho_cobra - 1)

        pygame.display.update()
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerador_comida()
        tempo.tick(velocidade)
