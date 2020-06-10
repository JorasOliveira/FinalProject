import sys

import os

# import place as place

import pygame


gravity = 3.5


black = (0, 0, 0)
grey = (127, 127, 127)
white = (255, 255, 255)
yellow = (255, 255, 0)


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
    def __init__(self, column, row, block):

        imagem = os.path.join('Imagem', 'ribamar.png')
        print(imagem)
        try:  # Importanto a imagem
            player1Img = pygame.image.load(imagem)  # do jogador 1
        except pygame.error:
            print("Erro ao carregar imagem do jogador")

        pygame.sprite.Sprite.__init__(self)

        self.image = player1Img

        self.blocks = block

        self.rect = self.image.get_rect()

        self.rect.x = column
        self.rect.bottom = row

        self.score = 0



class jogador2(pygame.sprite.Sprite):
    def __init__(self, colum, row, block):

        imagem = os.path.join('Imagem', 'mece.png')
        print(imagem)
        try:  # Importanto a imagem
            player2Img = pygame.image.load(imagem)  # do jogador 2
        except pygame.error:
            print("Erro ao carregar imagem do jogador")

        pygame.sprite.Sprite.__init__(self)

        self.image = player2Img

        self.blocks = block

        self.rect = self.image.get_rect()

        self.score = 0
        self.rect.x = colum
        self.rect.bottom = row


class bola(pygame.sprite.Sprite):
    def __init__(self, colum, row, block):

        imagem = os.path.join('Imagem', 'jabulani.png')
        print(imagem)
        try:  # Importanto a imagem
            ball = pygame.image.load(imagem)  # do jogador 1
        except pygame.error:
            print("Erro ao carregar imagem do jogador")

        pygame.sprite.Sprite.__init__(self)

        self.image = ball
        self.blocks = block
        self.rect = self.image.get_rect()

        self.rect.x = colum
        self.rect.y = row

class campo(pygame.sprite.Sprite):
    def __init__(self):

        imgfield = os.path.join('Imagem', 'field.png')
        print(imgfield)
        try:
            pitch = pygame.image.load(imgfield)  #Campo
        except pygame.error:
            print("Erro")

        pygame.sprite.Sprite.__init__(self)

        self.imgfield = pitch

def main():  # main routine
    pygame.init()

    displayX = 1336
    displayY = 752

    surf = pygame.display.set_mode([displayX, displayY])

    BackGround = Background()

    pygame.display.update()

    font = pygame.font.Font(pygame.font.get_default_font(), 35)

    clock = pygame.time.Clock()

    posY = int(displayY / 4)
    posX = int(displayX / 4)
    deltaPosX = 5
    deltaPosY= 10

    p1 = jogador1(posX, posY, 'block')
    p2 = jogador2(posX*3, posY, 'block')
    jabulani = bola(displayX/2, displayY/2, 'block')
    cancha = campo()

    PlacarEsquerda = p1.score
    PlacarDireita = p2.score


    while True:
        surf.fill(white)
        surf.blit(BackGround.image, [0, 0])

        delta_time = clock.tick(144)

        events = pygame.event.get()

        surf.blit(p1.image, p1.rect)
        surf.blit(p2.image, p2.rect)
        surf.blit(jabulani.image, jabulani.rect)
        surf.blit(cancha.imgfield, [0,672])

        for event in events:
            print(events)
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE \
                or p1.score == 7 or p2.score == 7:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        p1.rect.x -= deltaPosX
                    if event.key == pygame.K_d:
                        p1.rect.x += deltaPosX
                    if event.key == pygame.K_LEFT:
                        p2.rect.x -= deltaPosX
                    if event.key == pygame.K_RIGHT:
                        p2.rect.x += deltaPosX
                    if event.key == pygame.K_w:
                        p1.rect.y += deltaPosY
                    if event.key == pygame.K_UP:
                        p2.rect.y += deltaPosY


        p1.rect.y += gravity

        p2.rect.y += gravity

        #p2.posX += deltaH_pos

        #Adicionando os placares:
        
        TextoEsquerda = font.render("Ribamar: {0}".format(PlacarEsquerda), True, yellow)
        TextoDireita = font.render("Messi Careca: {0}".format(PlacarDireita), True, yellow)
        surf.blit(TextoEsquerda, (10, 0))
        surf.blit(TextoDireita, (1045, 0))
        pygame.display.flip()  # faz o update da imagine, usando troca de memory bugger
if __name__ == '__main__':
    main()
