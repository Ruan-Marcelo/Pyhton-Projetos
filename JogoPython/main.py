import pygame
import sys

from player import Player
from inimigo import Inimigo
from fases import desenhar_fundo

pygame.init()

# =========================
# CONFIGURAÇÕES
# =========================
LARGURA = 800
ALTURA = 450

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Saiyan Legacy")

clock = pygame.time.Clock()
FPS = 60

# =========================
# ESTADOS DO JOGO
# =========================
MENU = "menu"
JOGANDO = "jogando"
GAME_OVER = "game_over"

estado_jogo = MENU

# =========================
# PLAYER
# =========================
player = Player(100, 300)

# =========================
# INIMIGO
# =========================
inimigo = Inimigo(600, 300)

# =========================
# FONTES
# =========================
fonte_titulo = pygame.font.SysFont("Arial", 60)
fonte_menu = pygame.font.SysFont("Arial", 30)

# =========================
# TEXTO
# =========================
def desenhar_texto(texto, fonte, cor, x, y):

    render = fonte.render(texto, True, cor)

    tela.blit(render, (x, y))

# =========================
# RESETAR JOGO
# =========================
def resetar_jogo():

    global player
    global inimigo
    global estado_jogo

    player = Player(100, 300)

    inimigo = Inimigo(600, 300)

    estado_jogo = JOGANDO

# =========================
# LOOP PRINCIPAL
# =========================
while True:

    # =========================
    # EVENTOS
    # =========================
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:

            # =========================
            # MENU
            # =========================
            if estado_jogo == MENU:

                if evento.key == pygame.K_RETURN:
                    estado_jogo = JOGANDO

            # =========================
            # GAME OVER
            # =========================
            elif estado_jogo == GAME_OVER:

                if evento.key == pygame.K_r:
                    resetar_jogo()

            # =========================
            # JOGO
            # =========================
            elif estado_jogo == JOGANDO:

                if evento.key == pygame.K_SPACE:
                    player.pular()

    # =========================
    # MENU INICIAL
    # =========================
    if estado_jogo == MENU:

        desenhar_fundo(tela)

        # ESCURECER FUNDO
        overlay = pygame.Surface((800, 450))
        overlay.set_alpha(120)
        overlay.fill((0, 0, 0))

        tela.blit(overlay, (0, 0))

        # TÍTULO
        desenhar_texto(
            "SAIYAN LEGACY",
            fonte_titulo,
            (255,255,255),
            180,
            120
        )

        # TEXTO
        desenhar_texto(
            "PRESSIONE ENTER PARA COMEÇAR",
            fonte_menu,
            (255,255,255),
            170,
            240
        )

    # =========================
    # JOGO
    # =========================
    elif estado_jogo == JOGANDO:

        desenhar_fundo(tela)

        teclas = pygame.key.get_pressed()

        # PLAYER
        player.movimento(teclas)
        player.update()
        player.desenhar(tela)

        # INIMIGO
        inimigo.update()
        inimigo.desenhar(tela)

        # COLISÃO
        if player.rect.colliderect(inimigo.rect):

            player.vida -= 1

            player.x = 100

            pygame.time.delay(300)

        # VIDA
        desenhar_texto(
            f"VIDA: {player.vida}",
            fonte_menu,
            (255,255,255),
            20,
            20
        )

        # GAME OVER
        if player.vida <= 0:
            estado_jogo = GAME_OVER

    # =========================
    # GAME OVER
    # =========================
    elif estado_jogo == GAME_OVER:

        desenhar_fundo(tela)

        # ESCURECER
        overlay = pygame.Surface((800, 450))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))

        tela.blit(overlay, (0, 0))

        # GAME OVER
        desenhar_texto(
            "GAME OVER",
            fonte_titulo,
            (255,0,0),
            220,
            120
        )

        # REINICIAR
        desenhar_texto(
            "APERTE R PARA TENTAR NOVAMENTE",
            fonte_menu,
            (255,255,255),
            140,
            240
        )

    # =========================
    # UPDATE
    # =========================
    pygame.display.update()

    clock.tick(FPS)