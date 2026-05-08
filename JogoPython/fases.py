import pygame

# =========================
# CARREGAR FUNDO
# =========================
fundo = pygame.image.load(
    "assets/cenarios/cenario.png"
)

# TAMANHO DA TELA
fundo = pygame.transform.scale(
    fundo,
    (800, 450)
)

# =========================
# DESENHAR FUNDO
# =========================
def desenhar_fundo(tela):

    tela.blit(fundo, (0, 0))