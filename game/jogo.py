import sys
import os
import pygame
import random

# Criando a gravidade
gravity = 3.5
atrito = 1.005

# Definindo algumas cores
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
            BackGround = pygame.image.load(imagem)  # da tela de fundo
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
        self.mask = pygame.mask.from_surface(self.image)
        self.score = 0
        self.speedX = 0
        self.speedY = 0

    def update(self):
        self.rect.x += self.speedX
        self.rect.y += self.speedY


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
        self.rect.x = colum
        self.rect.bottom = row
        self.mask = pygame.mask.from_surface(self.image)
        self.score = 0
        self.speedX = 0
        self.speedY = 0

    def update(self):
        self.rect.x += self.speedX
        self.rect.y += self.speedY


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
        self.rect.bottom = row
        self.mask = pygame.mask.from_surface(self.image)
        self.speedX = 0
        self.speedY = 0

    def update(self):
        self.rect.x += self.speedX
        self.rect.y += self.speedY


class Campo(pygame.sprite.Sprite):
    def __init__(self):

        imgfield = os.path.join('Imagem', 'field.png')
        print(imgfield)
        try:                                     # Importando a imagem
            pitch = pygame.image.load(imgfield)  # do campo
        except pygame.error:
            print("Erro ao carregar o campo")
            sys.exit()

        pygame.sprite.Sprite.__init__(self)

        self.image = pitch
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()


class GolEsquerdo(pygame.sprite.Sprite):
    def __init__(self):

        imggol1 = os.path.join('Imagem', 'gol-esq.png')

        print(imggol1)
        try:                                    # Importando a imagem
            g_esq = pygame.image.load(imggol1)  # do gol esquerdo
        except pygame.error:
            print("Erro ao carregar imagem do gol esquerdo")
            sys.exit()

        pygame.sprite.Sprite.__init__(self)

        self.image = g_esq
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.bottom = 672
        self.mask = pygame.mask.from_surface(self.image)


class GolDireito(pygame.sprite.Sprite):
    def __init__(self):

        imggol2 = os.path.join('Imagem', 'gol-dir.png')

        print(imggol2)
        try:                                    # Impotando a imagem
            g_dir = pygame.image.load(imggol2)  # do gol direito
        except pygame.error:
            print("Erro ao carregar imagem do gol direito")
            sys.exit()

        pygame.sprite.Sprite.__init__(self)

        self.image = g_dir
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 1177
        self.rect.bottom = 672


class Endscreen(pygame.sprite.Sprite):
    def __init__(self):

        imagem = os.path.join('Imagem', 'endscreen.png')
        print(imagem)
        try:                                       # Importanto a imagem
            EndScreen = pygame.image.load(imagem)  # da endscreen
        except pygame.error:
            print("Erro ao carregar imagem final")
            sys.exit()

        pygame.sprite.Sprite.__init__(self)

        self.image = EndScreen


def main():  # main routine
    pygame.init()

    # dimensoes do display, em X e Y
    displayX = 1336
    displayY = 752

    surf = pygame.display.set_mode([displayX, displayY])  # cria o display

    backGround = Background()

    startScreen = Startscreen()

    endScreen = Endscreen()

    # Criando os booleanos para configurar a tela inicial e final:
    start = True
    end = True

    pygame.display.update()

    fontScore = pygame.font.Font(pygame.font.get_default_font(), 35)
    fontInstructions = pygame.font.Font(pygame.font.get_default_font(), 20)

    clock = pygame.time.Clock()

    posY = int(displayY / 4)
    posX = int(displayX / 6)
    deltaPosX = 3.5
    deltaPosY = 50

    # cria os objetos dos jogadores/suas sprites
    p1 = Jogador1(posX, posY, 'block')
    p2 = Jogador2(1336 - 350, posY, 'block')
    jabulani = Bola(displayX / 2, displayY / 2, 'block')
    cancha = Campo()
    golEsq = GolEsquerdo()
    golDir = GolDireito()
    # golDoRibamar = pygame.draw.rect(surf, white, (85, 325, 10, 340))  # Linha de ponto gol esquerdo
    # golDoMese = pygame.draw.rect(surf, white, ((1336 - 85), 325, 10, 340))  # Linha de ponto gol direito
    # print(golDoRibamar)

    sprites = pygame.sprite.Group()  # criando o grupo de sprites
    sprites.add(p1, p2, jabulani)  # adiciona as sprites ao grupo de sprites

    # inicializa a musica de fundo
    torcida = os.path.join('Som', 'Torcida.ogg')  # Som ambiente de torcida
    pygame.mixer.music.load(torcida)  # Carrega som
    pygame.mixer.music.set_volume(0.05)  # Volume
    pygame.mixer.music.play(-1)  # Toca som

    # inicia os outros sons
    sompulo = os.path.join('Som', 'Pular.ogg')  # som do pulo
    pulo = pygame.mixer.Sound(sompulo)  # carrega som
    somchute = os.path.join('Som', 'Chute.ogg')  # som do chute
    chute = pygame.mixer.Sound(somchute)  # carrega som
    somgol = os.path.join('Som', 'Gol.ogg')  # som do gol
    gol = pygame.mixer.Sound(somgol)  # carrega som
    gol.set_volume(0.7)

    while True:
        surf.fill(black)

        delta_time = clock.tick(60)

        events = pygame.event.get()

        # inicia as variaveis para os placares
        placarEsquerda = p1.score
        placarDireita = p2.score

        # Editando as teclas do teclado para dar para jogar:
        for event in events:

            # quitando o jogo
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            # detectando o enter para iniciar o jogo
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                start = False

            # reincia o jogo caso queiram jogar denovo apos
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and (p1.score >= 7 or p2.score >= 7):
                p1.score = 0
                p2.score = 0

                jabulani.rect.x = displayX / 2
                jabulani.rect.y = displayY / 2
                jabulani.speedX = 0
                jabulani.speedY = 0

                p1.rect.x = posX
                p1.rect.y = posY
                p1.speedX = 0
                p1.speedY = 0

                p2.rect.x = 1336 - 350
                p2.rect.y = posY
                p2.speedX = 0
                p2.speedY = 0

            # quitando o jogo, fora da tela inicial
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            # detectando as key presses e fazendo o movimento referente
            if event.type == pygame.KEYDOWN:

                # jogador 1, se move com WAD
                if event.key == pygame.K_a:  # a para esquerda
                    p1.speedX -= deltaPosX
                    p1.rect.x -= deltaPosX

                if event.key == pygame.K_d:  # d para direita
                    p1.speedX += deltaPosX

                # jogador 2, se move com as setas
                if event.key == pygame.K_LEFT:  # seta da esquerda para esquerda
                    p2.speedX -= deltaPosX

                if event.key == pygame.K_RIGHT:  # seta da direita para direita
                    p2.speedX += deltaPosX

                if event.key == pygame.K_w:  # w faz o jogador 1 pular
                    p1.rect.y -= deltaPosY
                    pulo.play()

                if event.key == pygame.K_UP:  # seta para cima faz o jogador 2 pular
                    p2.rect.y -= deltaPosY
                    pulo.play()

        # Adicionando a tela inicial e fazendo o jogo rodar:
        if start:

            surf.blit(p1.image, p1.rect)
            surf.blit(p2.image, p2.rect)
            surf.blit(jabulani.image, jabulani.rect)
            surf.blit(startScreen.image, [displayX / 10, displayY / 10])

        # pygame.sprite.spritecollide_rect()
        # sai da tela inicial e comeca o jogo
        else:

            # calculando colisoes
            for sprite in sprites:

                if sprite.rect.bottom > 672:
                    sprite.rect.bottom = 672
                    sprite.speedY = 0

                if sprite.rect.x <= 0:
                    sprite.rect.x = 0

                if sprite.rect.x >= 1336 - sprite.rect.width:
                    sprite.rect.x = 1336 - sprite.rect.width

                if pygame.sprite.collide_mask(p1, jabulani):

                    jabulani.speedX = p1.speedX * (random.uniform(1, 5))
                    jabulani.speedY = -p1.speedY * (random.uniform(5, 8))
                    chute.play()

                if pygame.sprite.collide_mask(p2, jabulani):
                    jabulani.speedX = p2.speedX * (random.uniform(1, 5))
                    jabulani.speedY = -p2.speedY * (random.uniform(5, 8))
                    chute.play()

                if pygame.sprite.collide_rect(jabulani, golDir):
                    p1.score += 1
                    gol.play()

                    jabulani.rect.x = displayX / 2
                    jabulani.rect.y = displayY / 2
                    jabulani.speedX = 0
                    jabulani.speedY = 0

                    p1.rect.x = posX
                    p1.rect.y = posY
                    p1.speedX = 0
                    p1.speedY = 0

                    p2.rect.x = 1336 - 350
                    p2.rect.y = posY
                    p2.speedX = 0
                    p2.speedY = 0

                if pygame.sprite.collide_rect(jabulani, golEsq):
                    p2.score += 1
                    gol.play()

                    jabulani.rect.x = displayX / 2
                    jabulani.rect.y = displayY / 2
                    jabulani.speedX = 0
                    jabulani.speedY = 0

                    p1.rect.x = posX
                    p1.rect.y = posY
                    p1.speedX = 0
                    p1.speedY = 0

                    p2.rect.x = 1336 - 350
                    p2.rect.y = posY
                    p2.speedX = 0
                    p2.speedY = 0

                jabulani.speedY += gravity/20
                p1.speedY += gravity/30
                p2.speedY += gravity/30
                jabulani.speedX /= atrito

                if 0.1 >= jabulani.speedX >= -0.5:
                    jabulani.speedX = 0

                p1.speedX /= atrito
                if 0.1 >= p1.speedX >= -0.5:
                    p1.speedX = 0
                p2.speedX /= atrito

                if 0.1 >= p2.speedX >= -0.5:
                    p2.speedX = 0

            sprites.update()

            # Adicionando as imagens do jogo
            surf.blit(backGround.image, [0, 0])  # imagem de fundo
            surf.blit(p1.image, p1.rect)  # player 1
            surf.blit(p2.image, p2.rect)  # player 2
            surf.blit(jabulani.image, jabulani.rect)  # bola
            surf.blit(cancha.image, [0, 672])  # campo
            surf.blit(golEsq.image, golEsq.rect)  # gol da esquerda
            surf.blit(golDir.image, [1177, 320])  # gol da direita
            goldDoRibamar = pygame.draw.rect(surf, white, (85,325,10,340)) # Linha de ponto gol esquerdo
            goldDoMese = pygame.draw.rect(surf, white, ((1336-85),325,10,340)) # Linha de ponto gol direito

            # Adicionando os placares:
            textoEsquerda = fontScore.render("Ribamar: {0}".format(placarEsquerda), True, yellow)
            textoDireita = fontScore.render("Messi Careca: {0}".format(placarDireita), True, yellow)
            surf.blit(textoEsquerda, (10, 0))
            surf.blit(textoDireita, (1045, 0))

            # Adicionando a tela final do jogo:
            if p1.score >= 7:
                surf.fill(black)
                surf.blit(endScreen.image, [displayX / 5, displayY / 5])
                textoVencedor1 = fontInstructions.render("Jogador 1 venceu!", True, white)
                textoInstrucoes1 = fontInstructions.render("Pressione 'Enter' para jogar novamente", True, white)
                textoInstrucoes2 = fontInstructions.render("Pressione 'ESC' para sair", True, white)
                surf.blit(p1.image, (displayX * 0.47, displayY / 3))
                surf.blit(textoVencedor1, [displayX * 4 / 9, displayY / 3])
                surf.blit(textoInstrucoes1, [displayX * 4 / 11, displayY * 3 / 5])
                surf.blit(textoInstrucoes2,
                          [(displayX / 2) - (textoInstrucoes2.get_rect().width / 2), displayY * 11 / 17])

            if p2.score >= 7:
                surf.fill(black)
                surf.blit(endScreen.image, [displayX / 5, displayY / 5])
                textoVencedor1 = fontInstructions.render("Jogador 2 venceu!", True, white)
                textoInstrucoes1 = fontInstructions.render("Pressione 'Enter' para jogar novamente", True, white)
                textoInstrucoes2 = fontInstructions.render("Pressione 'ESC' para sair", True, white)
                surf.blit(p2.image, (displayX * 0.47, displayY / 3))
                surf.blit(textoVencedor1, [displayX * 4 / 9, displayY / 3])
                surf.blit(textoInstrucoes1, [displayX * 4 / 11, displayY * 3 / 5])
                surf.blit(textoInstrucoes2,
                          [(displayX / 2) - (textoInstrucoes2.get_rect().width / 2), displayY * 11 / 17])

        pygame.display.flip()  # faz o update da imagine, usando troca de memory bugger


if __name__ == '__main__':
    main()
