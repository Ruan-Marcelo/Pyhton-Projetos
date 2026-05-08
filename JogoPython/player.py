import pygame

class Player:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.largura = 64
        self.altura = 64

        self.velocidade = 5

        self.velocidade_y = 0
        self.gravidade = 1

        self.pulando = False

        self.vida = 3

        # =========================
        # IMAGEM
        # =========================
        self.imagem = pygame.image.load(
            "assets/player/kidboo.png"
        )

        self.imagem = pygame.transform.scale(
            self.imagem,
            (self.largura, self.altura)
        )

        self.rect = self.imagem.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

    def movimento(self, teclas):

        if teclas[pygame.K_a]:
            self.x -= self.velocidade

        if teclas[pygame.K_d]:
            self.x += self.velocidade

    def pular(self):

        if not self.pulando:
            self.pulando = True
            self.velocidade_y = -15

    def update(self):

        self.velocidade_y += self.gravidade
        self.y += self.velocidade_y

        # CHÃO
        if self.y >= 300:
            self.y = 300
            self.velocidade_y = 0
            self.pulando = False

        self.rect.x = self.x
        self.rect.y = self.y

    def desenhar(self, tela):

        tela.blit(
            self.imagem,
            (self.x, self.y)
        )