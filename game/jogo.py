import sys

import os

# import place as place

import pygame

# Criando a gravidade
gravity = 3.5

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
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()


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

    displayX = 1336
    displayY = 752

    surf = pygame.display.set_mode([displayX, displayY])

    backGround = Background()

    startScreen = Startscreen()

    endScreen = Endscreen()

    start = True

    pygame.display.update()

    fontScore = pygame.font.Font(pygame.font.get_default_font(), 35)
    fontInstructions = pygame.font.Font(pygame.font.get_default_font(), 20)

    clock = pygame.time.Clock()

    posY = int(displayY / 4)
    posX = int(displayX / 6)
    deltaPosX = 0
    deltaPosXp1 = 0
    deltaPosXp2 = 0
    deltaPosY = 50

    p1 = Jogador1(posX, posY, 'block')
    p2 = Jogador2(1336 - 350, posY, 'block')
    jabulani = Bola(displayX / 2, displayY / 2, 'block')
    cancha = Campo()
    golEsq = GolEsquerdo()
    golDir = GolDireito()
    
    torcida = os.path.join('Som', 'Torcida.ogg') #Som ambiente de torcida
    pygame.mixer.music.load(torcida) #Carrega som
    pygame.mixer.music.set_volume(0.05) #Volume
    pygame.mixer.music.play(-1) #Toca som

    sompulo = os.path.join('Som', 'Pular.ogg') #som do pulo
    pulo = pygame.mixer.Sound(sompulo) #carrega som
    somchute = os.path.join('Som', 'Chute.ogg') #som do chute
    chute = pygame.mixer.Sound(somchute) #carrega som
    somgol = os.path.join('Som', 'Gol.ogg') #som do gol
    gol = pygame.mixer.Sound(somgol) #carrega som

    placarEsquerda = p1.score
    placarDireita = p2.score

    while True:
        surf.fill(black)

        delta_time = clock.tick(60)

        events = pygame.event.get()

        # Editando as teclas do teclado para dar para jogar:
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
                if event.key == pygame.K_a:
                    deltaPosXp2 = -3.5
                    #p1.rect.x -= deltaPosX

                if event.key == pygame.K_d:
                    deltaPosXp2 = 3.5
                    #p1.rect.x += deltaPosX

                if event.key == pygame.K_LEFT:
                    deltaPosXp1 = -3.5
                    #p2.rect.x -= deltaPosX

                if event.key == pygame.K_RIGHT:
                    deltaPosXp1 = 3.5
                    #p2.rect.x += deltaPosX

                if event.key == pygame.K_w:
                    p1.rect.y -= deltaPosY

                if event.key == pygame.K_UP:
                    p2.rect.y -= deltaPosY
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    deltaPosXp1 = 0
                if event.key == pygame.K_LEFT:
                    deltaPosXp1 = 0
                if event.key == pygame.K_a:
                    deltaPosXp2 = 0
                if event.key == pygame.K_d:
                    deltaPosXp2 = 0
            

            # p1.rect.y += gravity
            # p2.rect.y += gravity
            # jabulani.rect.y += gravity

        p2.rect.x += deltaPosXp1
        p1.rect.x += deltaPosXp2


        

        # Adicionando a tela inicial e fazendo o jogo rodar:
        if start:

            surf.blit(p1.image, p1.rect)
            surf.blit(p2.image, p2.rect)
            surf.blit(jabulani.image, jabulani.rect)
            surf.blit(startScreen.image, [displayX / 10, displayY / 10])

        else:



            # if p2.rect.y == 672:
            #     p2.rect.y = 0
            #
            # if jabulani.rect.y == 672:
            #     jabulani.rect.y = 0
            if pygame.sprite.collide_mask(jabulani, cancha):
                jabulani.rect.y += deltaPosY
                
            else:
                p1.rect.y += gravity
                p2.rect.y += gravity
                jabulani.rect.y += gravity

            # p2.posX += deltaH_pos

            # Adicionando as imagens do jogo
            surf.blit(backGround.image, [0, 0])
            surf.blit(p1.image, p1.rect)
            surf.blit(p2.image, p2.rect)
            surf.blit(jabulani.image, jabulani.rect)
            surf.blit(cancha.image, [0, 672])
            surf.blit(golEsq.image, [0, 320])
            surf.blit(golDir.image, [1177, 320])

            # Adicionando os placares:
            textoEsquerda = fontScore.render("Ribamar: {0}".format(placarEsquerda), True, yellow)
            textoDireita = fontScore.render("Messi Careca: {0}".format(placarDireita), True, yellow)
            surf.blit(textoEsquerda, (10, 0))
            surf.blit(textoDireita, (1045, 0))

            # Adicionando a tela final do jogo:
            if p1.score == 7:
                surf.fill(black)
                surf.blit(endScreen.image, [displayX / 5, displayY / 5])
                textoVencedor1 = fontInstructions.render("Jogador 1 venceu!", True, white)
                textoInstrucoes1 = fontInstructions.render("Pressione 'Enter' para jogar novamente", True, white)
                textoInstrucoes2 = fontInstructions.render("Pressione 'ESC' para sair", True, white)
                surf.blit(p1.image, (displayX * 0.47, displayY / 3))
                surf.blit(textoVencedor1, [displayX * 4 / 9, displayY / 3])
                surf.blit(textoInstrucoes1, [displayX * 4 / 11, displayY * 3 / 5])
                surf.blit(textoInstrucoes2, [(displayX / 2) - (textoInstrucoes2.get_rect().width / 2), displayY  * 11 / 17])


            if p2.score == 7:
                surf.fill(black)
                surf.blit(endScreen.image, [displayX / 5, displayY / 5])
                textoVencedor1 = fontInstructions.render("Jogador 2 venceu!", True, white)
                textoInstrucoes1 = fontInstructions.render("Pressione 'Enter' para jogar novamente", True, white)
                textoInstrucoes2 = fontInstructions.render("Pressione 'ESC' para sair", True, white)
                surf.blit(p2.image, (displayX * 0.47, displayY / 3))
                surf.blit(textoVencedor1, [displayX * 4 / 9, displayY / 3])
                surf.blit(textoInstrucoes1, [displayX * 4 / 11, displayY * 3 / 5])
                surf.blit(textoInstrucoes2, [(displayX / 2) - (textoInstrucoes2.get_rect().width / 2), displayY  * 11 / 17])

        pygame.display.flip()  # faz o update da imagine, usando troca de memory bugger


if __name__ == '__main__':
    main()
