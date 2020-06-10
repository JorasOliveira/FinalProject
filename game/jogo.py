import sys

import os

# import place as place

import pygame

gravity = 3.5

black = (0, 0, 0)
grey = (127, 127, 127)
white = (255, 255, 255)
yellow = (255, 255, 0)
blue = (0, 0, 255)


class Background(pygame.sprite.Sprite):
    def __init__(self):

        imagem = os.path.join('Imagem', 'fundo.PNG')
        print(imagem)
        try:                                        # Importanto a imagem
            BackGround = pygame.image.load(imagem)  # do jogador 1
        except pygame.error:
            print("Erro ao carregar imagem de fundo")
            sys.exit()

        pygame.sprite.Sprite.__init__(self)

        self.image = BackGround


class Startscreen(pygame.sprite.Sprite):
    def __init__(self):

        imagem = os.path.join('Imagem', 'startscreen.png')
        print(imagem)
        try:                                         # Importanto a imagem
            StartScreen = pygame.image.load(imagem)  # da Tela Inicial
        except pygame.error:
            print("Erro ao carregar imagem inicial")
            sys.exit()

        pygame.sprite.Sprite.__init__(self)

        self.image = StartScreen


class Jogador1(pygame.sprite.Sprite):
    def __init__(self, column, row, block):

        imagem = os.path.join('Imagem', 'ribamar.png')
        print(imagem)
        try:                                        # Importanto a imagem
            player1Img = pygame.image.load(imagem)  # do jogador 1
        except pygame.error:
            print("Erro ao carregar imagem do jogador 1")
            sys.exit()

        pygame.sprite.Sprite.__init__(self)

        self.image = player1Img
        self.blocks = block
        self.rect = self.image.get_rect()
        self.rect.x = column
        self.rect.bottom = row
        self.score = 0


class Jogador2(pygame.sprite.Sprite):
    def __init__(self, colum, row, block):

        imagem = os.path.join('Imagem', 'mece.png')
        print(imagem)
        try:                                        # Importanto a imagem
            player2Img = pygame.image.load(imagem)  # do jogador 2
        except pygame.error:
            print("Erro ao carregar imagem do jogador 2")
            sys.exit()

        pygame.sprite.Sprite.__init__(self)

        self.image = player2Img
        self.blocks = block
        self.rect = self.image.get_rect()
        self.score = 0
        self.rect.x = colum
        self.rect.bottom = row


class Bola(pygame.sprite.Sprite):
    def __init__(self, colum, row, block):

        imagem = os.path.join('Imagem', 'jabulani.png')
        print(imagem)
        try:                                  # Importanto a imagem
            ball = pygame.image.load(imagem)  # da bola
        except pygame.error:
            print("Erro ao carregar a bola")
            sys.exit()

        pygame.sprite.Sprite.__init__(self)

        self.image = ball
        self.blocks = block
        self.rect = self.image.get_rect()
        self.rect.x = colum
        self.rect.y = row


class Campo(pygame.sprite.Sprite):
    def __init__(self):

        imgfield = os.path.join('Imagem', 'field.png')
        print(imgfield)
        try:
            pitch = pygame.image.load(imgfield)  # Campo
        except pygame.error:
            print("Erro ao carregar o campo")
            sys.exit()

        pygame.sprite.Sprite.__init__(self)

        self.imgfield = pitch


class GolEsquerdo(pygame.sprite.Sprite):
    def __init__(self):

        imggol1 = os.path.join('Imagem', 'gol-esq.png')
        print(imggol1)
        try:
            g_esq = pygame.image.load(imggol1)  # Gol esquerdo
        except pygame.error:
            print("Erro")
            sys.exit()

        pygame.sprite.Sprite.__init__(self)

        self.image = g_esq


class GolDireito(pygame.sprite.Sprite):
    def __init__(self):

        imggol2 = os.path.join('Imagem', 'gol-dir.png')
        print(imggol2)
        try:
            g_dir = pygame.image.load(imggol2)  # Gol direito
        except pygame.error:
            print("Erro")
            sys.exit()

        pygame.sprite.Sprite.__init__(self)

        self.image = g_dir


class Endscreen(pygame.sprite.Sprite):
    def __init__(self):

        imagem = os.path.join('Imagem', 'endscreen.png')
        print(imagem)
        try:  # Importanto a imagem
            EndScreen = pygame.image.load(imagem)  # do jogador 1
        except pygame.error:
            print("Erro ao carregar imagem final")
            sys.exit()

        pygame.sprite.Sprite.__init__(self)

        self.image = EndScreen


def main():  # main routine
    pygame.init()

    displayX = 1336
    displayY = 752

    surf = pygame.display.set_mode([displayX, displayY])

    backGround = Background()

    startScreen = Startscreen()

    endScreen = Endscreen()

    start = True

    pygame.display.update()

    font = pygame.font.Font(pygame.font.get_default_font(), 35)

    clock = pygame.time.Clock()

    posY = int(displayY / 4)
    posX = int(displayX / 6)
    deltaPosX = 5
    deltaPosY = 50

    p1 = Jogador1(posX, posY, 'block')
    p2 = Jogador2(1336 - 350, posY, 'block')
    jabulani = Bola(displayX / 2, displayY / 2, 'block')
    cancha = Campo()
    golEsq = GolEsquerdo()
    golDir = GolDireito()

    placarEsquerda = p1.score
    placarDireita = p2.score

    while True:
        surf.fill(black)

        delta_time = clock.tick(60)

        events = pygame.event.get()

        for event in events:

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                start = False

            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
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
                        p1.rect.y -= deltaPosY

                    if event.key == pygame.K_UP:
                        p2.rect.y -= deltaPosY

            # p1.rect.y += gravity
            # p2.rect.y += gravity
            # jabulani.rect.y += gravity

        if start:

            surf.blit(p1.image, p1.rect)
            surf.blit(p2.image, p2.rect)
            surf.blit(jabulani.image, jabulani.rect)
            surf.blit(startScreen.image, [displayX / 10, displayY / 10])

        else:

            if p1.rect.y == 672:
                p1.rect.y = 0

            if p2.rect.y == 672:
                p2.rect.y = 0

            if jabulani.rect.y == 672:
                jabulani.rect.y = 0

            else:
                p1.rect.y += gravity
                p2.rect.y += gravity
                jabulani.rect.y += gravity

            # p2.posX += deltaH_pos

            surf.blit(backGround.image, [0, 0])
            surf.blit(p1.image, p1.rect)
            surf.blit(p2.image, p2.rect)
            surf.blit(jabulani.image, jabulani.rect)
            surf.blit(cancha.imgfield, [0, 672])
            surf.blit(golEsq.image, [0, 320])
            surf.blit(golDir.image, [1177, 320])
            # print(events)

            # Adicionando os placares:
            textoEsquerda = font.render("Ribamar: {0}".format(placarEsquerda), True, yellow)
            textoDireita = font.render("Messi Careca: {0}".format(placarDireita), True, yellow)
            surf.blit(textoEsquerda, (10, 0))
            surf.blit(textoDireita, (1045, 0))

        if p1.score == 7 or p2.score == 7:
            pygame.draw.rect(surf, black, [1072, 603, 1072, 603])

        pygame.display.flip()  # faz o update da imagine, usando troca de memory bugger


if __name__ == '__main__':
    main()
