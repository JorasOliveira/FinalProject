import sys

import os

#import place as place

import pygame

grey = (127, 127, 127)

class Background(pygame.sprite.Sprite):
    def __init__(self):

        imagem = os.path.join('Imagem', 'fundo.PNG')
        print(imagem)
        try:  # Importanto a imagem
            BackGround = pygame.image.load(imagem)  # do jogador 1
        except pygame.error:
            print("Erro ao carregar imagem do jogador")

        pygame.sprite.Sprite.__init__(self)

        self.image = BackGround

class jogador1(pygame.sprite.Sprite):

    def __init__(self, colum, row, block):

        imagem = os.path.join('Imagem', 'ribamar.png')
        print(imagem)
        try:  # Importanto a imagem
            player1Img = pygame.image.load(imagem)  # do jogador 1
        except pygame.error:
            print("Erro ao carregar imagem do jogador")

        pygame.sprite.Sprite.__init__(self)

        self.image = player1Img
        self.posX = colum
        self.posY = row
        self.blocks = block


class jogador2(pygame.sprite.Sprite):

    def __init__(self, colum, row,  block):

        imagem = os.path.join('Imagem', 'mece.png')
        print(imagem)
        try:  # Importanto a imagem
            player2Img = pygame.image.load(imagem)  # do jogador 2
        except pygame.error:
            print("Erro ao carregar imagem do jogador")

        pygame.sprite.Sprite.__init__(self)

        self.image = player2Img
        self.posX = colum
        self.posY = row
        self.blocks = block

class bola(pygame.sprite.Sprite):

    def __init__(self,  colum, row, block):

        imagem = os.path.join('Imagem', 'jabulani.png')
        print(imagem)
        try:  # Importanto a imagem
            ball = pygame.image.load(imagem)  # do jogador 1
        except pygame.error:
            print("Erro ao carregar imagem do jogador")

        pygame.sprite.Sprite.__init__(self)

        self.image = ball
        self.posX = colum
        self.posY = row
        self.blocks = block


def main():  # main routine
    pygame.init()

    displayX = 1336
    displayY = 752

    surf = pygame.display.set_mode([displayX, displayY])

    BackGround = Background()

    pygame.display.update()

    clock = pygame.time.Clock()

    posY = int(displayY / 4)
    posX = int(displayX / 4)
    deltaH_pos = 1
    deltaV_pos = 1

    p1 = jogador1(posX, posY, 'block')
    p2 = jogador2(posX*3, posY, 'block')
    jabulani = bola(displayX/2, displayY/2, 'block')

    while True:
        surf.fill([255, 255, 255])
        surf.blit(BackGround.image, [0, 0])

        delta_time = clock.tick(144)

        events = pygame.event.get()

        surf.blit(p1.image, [p1.posX, p1.posY])
        surf.blit(p2.image, [p2.posX, p2.posY])
        surf.blit(jabulani.image, [jabulani.posX, jabulani.posY])

        for event in events:
            print(events)
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    p1.posX -= deltaH_pos              
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    p1.posX += deltaH_pos              
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    p2.posX -= deltaH_pos              
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    p2.posX += deltaH_pos



        pygame.display.flip()  # faz o update da imagine, usando troca de memory bugger


if __name__ == '__main__':
    main()
