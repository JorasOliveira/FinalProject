import sys

import os

import place as place
import pygame

grey = (127, 127, 127)


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


# class jogador2(pygame.sprite.Sprite):
#
#     def __init__(self, colum, row,  block):
#
#         imagem = os.path.join('Imagem', 'mece.pgn')
#         print(imagem)
#         try:  # Importanto a imagem
#             player2Img = pygame.image.load(imagem)  # do jogador 2
#         except pygame.error:
#             print("Erro ao carregar imagem do jogador")
#
#         pygame.sprite.Sprite.__init__(self)
#
#         self.image = player2Img
#         self.posX = colum
#         self.posY = row
#         self.blocks = block

# class bola(pygame.sprite.Sprite):
#
#     def __init__(self,  colum, row, block):
#
#         imagem = os.path.join('Imagem', 'jabulani')
#         print(imagem)
#         try:  # Importanto a imagem
#             ball = pygame.image.load(imagem)  # do jogador 1
#         except pygame.error:
#             print("Erro ao carregar imagem do jogador")
#
#         pygame.sprite.Sprite.__init__(self)
#
#         self.image = ball
#         self.posX = colum
#         self.posY = row
#         self.blocks = block


def main():  # main routine
    pygame.init()

    displayX = 1280
    displayY = 720

    surf = pygame.display.set_mode([displayX, displayY])

    pygame.display.update()

    clock = pygame.time.Clock()

    posY = int(displayY / 4)
    posX = int(displayX / 4)
    deltaH_pos = 1
    deltaV_pos = 1

    p1 = jogador1(posX, posY, 'block')
    # p2 = jogador2(700, 700, 'block')
    # jabulani = bola(0, 0, 'block')

    while True:
        surf.fill(grey)
        delta_time = clock.tick(144)

        events = pygame.event.get()

        surf.blit(p1.image, [p1.posX, p1.posY])
        # surf.bli(p2.image, [p2.posX, p2.posY])
        # surf.blit(jabulani.image, [jabulani.posX, jabulani.posY])

        for event in events:
            print(events)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.draw.circle(surf, [0, 0, 255], [posY, posX], 50)  # update da posicao do ciruclo

        # descobre aonde o circulo esta  e decide qual movimento deve fazer

        if posY <= 50:
            deltaH_pos = 1

        if posY >= displayY - 100:
            deltaH_pos = -1

        if posX <= 50:
            deltaV_pos = 1

        if posX >= displayX - 100:
            deltaV_pos = -1

        posY += deltaH_pos
        posX += deltaV_pos

        pygame.display.flip()  # faz o update da imagine, usando troca de memory bugger


if __name__ == '__main__':
    main()
