import pygame

class Inimigo:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.largura = 64
        self.altura = 64

        self.velocidade = 2

        self.direcao = 1

        # =========================
        # IMAGEM
        # =========================
        self.imagem = pygame.image.load(
            "assets/inimigos/download.jpeg"
        )

        self.imagem = pygame.transform.scale(
            self.imagem,
            (self.largura, self.altura)
        )

        self.rect = self.imagem.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):

        self.x += self.velocidade * self.direcao

        if self.x >= 700:
            self.direcao = -1

        if self.x <= 500:
            self.direcao = 1

        self.rect.x = self.x

    def desenhar(self, tela):

        tela.blit(
            self.imagem,
            (self.x, self.y)
        )