import pygame
import sys
import random

pygame.init()

LARGURA = 1280
ALTURA = 720
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Código Galaxy - Runner Quiz")

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA_ESCURO = (40, 40, 40)
VERDE = (50, 200, 50)
VERMELHO = (220, 40, 40)
AZUL_ESCURO = (30, 40, 70)
VERMELHO_ESCURO = (70, 30, 30)

TAM_OBSTACULO = (140, 180)
ALTURA_CHAO = 80 
ALTURA_FIXA_PERSONAGEM = 160 

banco_perguntas = [
    {"tema": "Lógica de Programação", "pergunta": "O que é uma variável?", "opcoes": ["1) Um espaço na memória para guardar dados", "2) Um erro no código", "3) Um laço de repetição", "4) Uma tela de erro"], "resposta_correta": 0},
    {"tema": "Lógica de Programação", "pergunta": "Qual estrutura é usada para repetição?", "opcoes": ["1) IF / ELSE", "2) FOR / WHILE", "3) TRY / CATCH", "4) AND / OR"], "resposta_correta": 1},
    {"tema": "Lógica de Programação", "pergunta": "O que é um algoritmo?", "opcoes": ["1) Um vírus de computador", "2) Uma sequência de passos lógicos para resolver um problema", "3) Uma peça de hardware", "4) Um tipo de teclado"], "resposta_correta": 1},
    {"tema": "Lógica de Programação", "pergunta": "Qual é o tipo de dado para Verdadeiro ou Falso?", "opcoes": ["1) Integer (Inteiro)", "2) String (Texto)", "3) Boolean (Booleano)", "4) Float (Decimal)"], "resposta_correta": 2},
    {"tema": "Lógica de Programação", "pergunta": "Para que serve uma função (ou método)?", "opcoes": ["1) Para travar o sistema", "2) Para mudar a cor da tela", "3) Para repetir o mesmo código infinitamente", "4) Para agrupar códigos que executam uma tarefa específica"], "resposta_correta": 3},
    {"tema": "Lógica de Programação", "pergunta": "O que faz o comando 'return'?", "opcoes": ["1) Reinicia o computador", "2) Devolve um valor como resultado de uma função", "3) Apaga o último caractere", "4) Volta para a tela anterior"], "resposta_correta": 1},
    {"tema": "Banco de Dados", "pergunta": "Qual comando SQL é usado para buscar dados?", "opcoes": ["1) UPDATE", "2) DELETE", "3) INSERT", "4) SELECT"], "resposta_correta": 3},
    {"tema": "Banco de Dados", "pergunta": "O que é uma Primary Key (Chave Primária)?", "opcoes": ["1) Um identificador único para um registro numa tabela", "2) Um tipo de dado de texto", "3) Um comando de exclusão"], "resposta_correta": 0},
    {"tema": "Banco de Dados", "pergunta": "Para que serve a cláusula WHERE em SQL?", "opcoes": ["1) Para criar uma nova tabela", "2) Para ordenar os resultados", "3) Para filtrar os registros com base numa condição", "4) Para agrupar dados repetidos"], "resposta_correta": 2},
    {"tema": "Banco de Dados", "pergunta": "O que significa a sigla SGBD?", "opcoes": ["1) Sistema Global de Busca Dinâmica", "2) Sistema de Gerenciamento de Banco de Dados", "3) Servidor Geral de Bytes e Dados", "4) Sistema Gerador de Backups Diários"], "resposta_correta": 1},
    {"tema": "Banco de Dados", "pergunta": "O que faz o comando JOIN?", "opcoes": ["1) Apaga duas tabelas de uma vez", "2) Junta o código do frontend com o backend", "3) Combina colunas de uma ou mais tabelas baseadas num valor comum", "4) Cria um backup da base de dados"], "resposta_correta": 2},
    {"tema": "Banco de Dados", "pergunta": "Qual comando SQL é utilizado para adicionar novos registos a uma tabela?", "opcoes": ["1) ADD NEW", "2) INSERT INTO", "3) CREATE ROW", "4) UPDATE"], "resposta_correta": 1},
    {"tema": "Engenharia de Software", "pergunta": "O que significa 'Bug' na programação?", "opcoes": ["1) Uma nova funcionalidade", "2) Uma falha ou erro no código", "3) Um tipo de servidor", "4) A interface do utilizador"], "resposta_correta": 1},
    {"tema": "Engenharia de Software", "pergunta": "Qual destas é uma metodologia Ágil?", "opcoes": ["1) Cascata (Waterfall)", "2) Scrum", "3) Modelo em Espiral", "4) Programação Estruturada"], "resposta_correta": 1},
    {"tema": "Engenharia de Software", "pergunta": "O que é o Git?", "opcoes": ["1) Um sistema de controle de versões de código", "2) Uma linguagem de programação para jogos", "3) Um antivírus gratuito", "4) Um modelo de teclado mecânico"], "resposta_correta": 0},
    {"tema": "Engenharia de Software", "pergunta": "O que é uma API?", "opcoes": ["1) Um tipo de cabo de rede", "2) Um programa de desenho vectorial", "3) Uma interface que permite a comunicação entre sistemas", "4) Uma lei de proteção de dados"], "resposta_correta": 2},
    {"tema": "Engenharia de Software", "pergunta": "No contexto do Scrum, o que é uma 'Sprint'?", "opcoes": ["1) Uma corrida rápida no escritório", "2) Um ciclo de desenvolvimento curto e fixo", "3) Um erro crítico no sistema", "4) O momento em que o projeto é cancelado"], "resposta_correta": 1},
    {"tema": "Engenharia de Software", "pergunta": "O que significa a palavra 'Deploy'?", "opcoes": ["1) Apagar o código fonte", "2) Procurar erros no código", "3) Colocar a aplicação em produção, disponível para os utilizadores", "4) Escrever a documentação do projeto"], "resposta_correta": 2},
    {"tema": "Redes de Computadores", "pergunta": "O que é um endereço IP?", "opcoes": ["1) O nome do monitor", "2) A velocidade da internet", "3) O identificador único de um dispositivo na rede", "4) Um cabo de conexão de áudio"], "resposta_correta": 2},
    {"tema": "Redes de Computadores", "pergunta": "Qual protocolo é usado para navegar em sites seguros?", "opcoes": ["1) FTP", "2) SMTP", "3) HTTPS", "4) DHCP"], "resposta_correta": 2},
    {"tema": "Redes de Computadores", "pergunta": "O que o protocolo DNS faz?", "opcoes": ["1) Protege o computador de vírus", "2) Traduz nomes de domínio (ex: google.com) para endereços IP", "3) Aumenta a velocidade do Wi-Fi", "4) Envia emails"], "resposta_correta": 1},
    {"tema": "Redes de Computadores", "pergunta": "Qual é a porta padrão para o tráfego web não encriptado (HTTP)?", "opcoes": ["1) Porta 21", "2) Porta 25", "3) Porta 443", "4) Porta 80"], "resposta_correta": 3},
    {"tema": "Redes de Computadores", "pergunta": "O que significa a sigla LAN?", "opcoes": ["1) Local Area Network (Rede de Área Local)", "2) Large Area Network (Rede de Grande Área)", "3) Logical Access Node (Nó de Acesso Lógico)", "4) Link Area Node (Nó de Área de Ligação)"], "resposta_correta": 0},
    {"tema": "Redes de Computadores", "pergunta": "Para que serve o comando 'ping'?", "opcoes": ["1) Para reiniciar o servidor remoto", "2) Para testar a conectividade entre dois equipamentos de rede", "3) Para limpar o cache do navegador", "4) Para descarregar ficheiros grandes"], "resposta_correta": 1}
]

fundo_x = 0
velocidade_fundo = 4  
vidas = 3
pontuacao = 0
pergunta_atual = None
resultado_msg = ""
tempo_msg = 0
tempo_morte = 0

def carregar_com_proporcao(caminho, altura_alvo):
    img = pygame.image.load(caminho).convert_alpha()
    largura_original, altura_original = img.get_size()
    proporcao = largura_original / altura_original
    nova_largura = int(altura_alvo * proporcao)
    return pygame.transform.scale(img, (nova_largura, altura_alvo))

try:
    img_corre = [
        carregar_com_proporcao('./images/personagem_correndo1.png', ALTURA_FIXA_PERSONAGEM),
        carregar_com_proporcao('./images/personagem_correndo2.png', ALTURA_FIXA_PERSONAGEM),
        carregar_com_proporcao('./images/personagem_correndo3.png', ALTURA_FIXA_PERSONAGEM)
    ]
    img_morto = [
        carregar_com_proporcao('./images/personagem_morto1.png', ALTURA_FIXA_PERSONAGEM),
        carregar_com_proporcao('./images/personagem_morto2.png', ALTURA_FIXA_PERSONAGEM),
        carregar_com_proporcao('./images/personagem_morto3.png', ALTURA_FIXA_PERSONAGEM)
    ]
    img_coracao = pygame.transform.scale(pygame.image.load('./images/coracao.webp').convert_alpha(), (70, 70))

    img_goku = pygame.transform.scale(pygame.image.load('./images/goku.png').convert_alpha(),
        TAM_OBSTACULO
    )

    img_goku_certo = pygame.transform.scale(pygame.image.load('./images/goku-certo.png').convert_alpha(),
        TAM_OBSTACULO
    )
    fundo_original = pygame.image.load('./images/fundo.png').convert()
    nova_largura_f = int(fundo_original.get_width() * (ALTURA / fundo_original.get_height()))
    img_fundo = pygame.transform.scale(fundo_original, (nova_largura_f, ALTURA))
    largura_fundo = img_fundo.get_width()
    tem_imagens = True
    tem_coracao_img = True
except Exception as e:
    print("ERRO AO CARREGAR IMAGENS:")
    print(e)

    tem_imagens = False
    tem_coracao_img = False
    largura_fundo = LARGURA

try:
    img_inicio = pygame.transform.scale(pygame.image.load('./images/inicio (1).png').convert(), (LARGURA, ALTURA))
except: pass

try:
    img_fim = pygame.transform.scale(pygame.image.load('./images/fim (1).png').convert(), (LARGURA, ALTURA))
except: pass

class Jogador:
    def __init__(self):
        if tem_imagens:
            self.largura, self.altura = img_corre[0].get_size()
        else:
            self.largura, self.altura = 100, 160
        self.x = 100
        self.y = ALTURA - ALTURA_CHAO - self.altura 
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.estado = "correndo" 
        self.frame_atual = 0
        self.tempo_animacao = 0

    def atualizar(self):
        self.rect.topleft = (self.x, self.y)
        self.tempo_animacao += 1
        if self.tempo_animacao >= 6: 
            self.tempo_animacao = 0
            if self.estado == "correndo":
                self.frame_atual = (self.frame_atual + 1) % len(img_corre)
            elif self.estado == "morto" and self.frame_atual < len(img_morto) - 1:
                self.frame_atual += 1

    def desenhar(self):
        if tem_imagens:
            img = img_morto[self.frame_atual] if self.estado == "morto" else img_corre[self.frame_atual]
            tela.blit(img, (self.x, self.y))
        else:
            pygame.draw.rect(tela, VERMELHO, self.rect)

class Obstaculo:
    def __init__(self):
        self.largura, self.altura = TAM_OBSTACULO

        self.x = LARGURA
        self.y = ALTURA - ALTURA_CHAO - self.altura

        self.velocidade = 8
        self.colid = False
        self.estado = "parado"

        self.tempo_certo = 0

        self.rect = pygame.Rect(
            self.x,
            self.y,
            self.largura,
            self.altura
        )

    def atualizar(self):
        self.x -= self.velocidade
        self.rect.topleft = (self.x, self.y)
        if self.estado == "certo":
            self.tempo_certo -= 1
            if self.tempo_certo <= 0:
                self.estado = "parado"

    def desenhar(self):
        if tem_imagens:
            if self.estado == "certo":
                tela.blit(img_goku_certo, (self.x, self.y))
            else:
                tela.blit(img_goku, (self.x, self.y))
        else:
            pygame.draw.rect(
                tela,
                VERDE,
                self.rect
            )

def desenhar_hud():
    caixa_p = pygame.Rect(20, 20, 220, 80)
    pygame.draw.rect(tela, AZUL_ESCURO, caixa_p, border_radius=10)
    pygame.draw.rect(tela, (100, 150, 255), caixa_p, width=3, border_radius=10)
    txt_p = fonte_hud.render(f"Pontos: {pontuacao}", True, BRANCO)
    tela.blit(txt_p, (caixa_p.x + 20, caixa_p.centery - txt_p.get_height() // 2))

    largura_hud_v = 280
    caixa_v = pygame.Rect(LARGURA - largura_hud_v - 20, 20, largura_hud_v, 80)
    pygame.draw.rect(tela, VERMELHO_ESCURO, caixa_v, border_radius=10)
    pygame.draw.rect(tela, (255, 100, 100), caixa_v, width=3, border_radius=10)
    
    for i in range(vidas):
        if tem_coracao_img:
            l_cor = img_coracao.get_width()
            a_cor = img_coracao.get_height()
            x_pos = caixa_v.x + 15 + (i * (l_cor + 5))
            y_pos = caixa_v.centery - a_cor // 2
            tela.blit(img_coracao, (x_pos, y_pos))
        else:
            cx, cy = (caixa_v.x + 45) + (i * 65), caixa_v.centery - 10
            pygame.draw.circle(tela, VERMELHO, (cx - 12, cy), 15)
            pygame.draw.circle(tela, VERMELHO, (cx + 12, cy), 15)
            pygame.draw.polygon(tela, VERMELHO, [(cx - 27, cy + 5), (cx + 27, cy + 5), (cx, cy + 35)])

def desenhar_texto_quebrado(texto, fonte, cor, x, y, largura_max):
    palavras = texto.split(' ')
    linhas = []
    linha_atual = ""

    for palavra in palavras:
        teste = linha_atual + palavra + " "

        if fonte.size(teste)[0] <= largura_max:
            linha_atual = teste
        else:
            linhas.append(linha_atual)
            linha_atual = palavra + " "

    linhas.append(linha_atual)

    for i, linha in enumerate(linhas):
        superficie = fonte.render(linha, True, cor)
        tela.blit(superficie, (x, y + i * 50))

    return len(linhas)

def exibir_pergunta():
    overlay = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 200))
    tela.blit(overlay, (0, 0))

    caixa = pygame.Rect(100, 100, LARGURA - 200, ALTURA - 200)

    pygame.draw.rect(tela, CINZA_ESCURO, caixa, border_radius=20)
    pygame.draw.rect(tela, BRANCO, caixa, width=4, border_radius=20)

    fonte_tema = pygame.font.SysFont('Arial', 30, bold=True)
    fonte_pergunta = pygame.font.SysFont('Arial', 40, bold=True)
    fonte_opcao = pygame.font.SysFont('Arial', 30)

    tela.blit(
        fonte_tema.render(
            f"Tema: {pergunta_atual['tema']}",
            True,
            (150, 200, 255)
        ),
        (130, 120)
    )

    linhas = desenhar_texto_quebrado(
        pergunta_atual['pergunta'],
        fonte_pergunta,
        BRANCO,
        130,
        180,
        caixa.width - 60
    )

    y_opcoes = 250 + (linhas * 50)

    for i, opcao in enumerate(pergunta_atual['opcoes']):
        texto = fonte_opcao.render(opcao, True, BRANCO)
        tela.blit(texto, (150, y_opcoes + (i * 60)))

jogador = Jogador()
obstaculo = Obstaculo()
relogio = pygame.time.Clock()
estado_jogo = "START" 
fonte_hud = pygame.font.SysFont('Arial', 32, bold=True)

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if ev.type == pygame.KEYDOWN:
            if estado_jogo in ["START", "GAMEOVER"]:
                if ev.key == pygame.K_SPACE:
                    jogador = Jogador(); obstaculo = Obstaculo()
                    pontuacao = 0; vidas = 3; velocidade_fundo = 3
                    tempo_msg = 0; resultado_msg = "" 
                    estado_jogo = "PLAYING"
            elif estado_jogo == "QUESTION":
                resp = -1
                teclas = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]
                teclas_num = [pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4]
                for i in range(4):
                    if ev.key == teclas[i] or ev.key == teclas_num[i]: resp = i
                if resp != -1:
                    if resp == pergunta_atual['resposta_correta']:
                        resultado_msg = "RESPOSTA CORRETA! +10 Pontos"
                        pontuacao += 10
                        obstaculo.estado = "certo"
                        obstaculo.tempo_certo = 60
                    else:
                        vidas -= 1; resultado_msg = "RESPOSTA ERRADA! -1 Vida"
                    tempo_msg = 60; obstaculo.x = LARGURA + 200
                    if vidas <= 0:
                        jogador.estado = "morto"; jogador.frame_atual = 0
                        estado_jogo = "DYING"; tempo_morte = 120
                    else:
                        estado_jogo = "PLAYING"

    if estado_jogo == "START":
        try: tela.blit(img_inicio, (0, 0))
        except: tela.fill(PRETO)
        pygame.display.flip()
    elif estado_jogo in ["PLAYING", "QUESTION", "DYING"]:
        if estado_jogo == "PLAYING":
            fundo_x = (fundo_x - velocidade_fundo) % -largura_fundo
            obstaculo.atualizar()
            if obstaculo.x < -obstaculo.largura: obstaculo.x = LARGURA
            if jogador.rect.colliderect(obstaculo.rect):
                pergunta_atual = random.choice(banco_perguntas); estado_jogo = "QUESTION"
        jogador.atualizar()
        if tem_imagens:
            for i in range((LARGURA // largura_fundo) + 2):
                tela.blit(img_fundo, (fundo_x + (i * largura_fundo), 0))
        else: tela.fill((20, 20, 50))
        
        if estado_jogo == "DYING":
            tempo_morte -= 1
            if tempo_morte > 60: jogador.desenhar()
            if tempo_morte <= 0: estado_jogo = "GAMEOVER"
        else:
            jogador.desenhar(); obstaculo.desenhar()
        
        desenhar_hud()
        if tempo_msg > 0 and estado_jogo == "PLAYING":
            cor = VERDE if "CORRETA" in resultado_msg else VERMELHO
            txt = pygame.font.SysFont('Arial', 40, bold=True).render(resultado_msg, True, cor)
            tela.blit(txt, (LARGURA//2 - txt.get_width()//2, 100))
            tempo_msg -= 1
        if estado_jogo == "QUESTION": exibir_pergunta()
        pygame.display.flip()
    elif estado_jogo == "GAMEOVER":
        try: tela.blit(img_fim, (0, 0))
        except: tela.fill(PRETO)
        txt_restart = pygame.font.SysFont('Arial', 35, bold=True).render("Pressione ESPAÇO para jogar novamente!", True, BRANCO)
        tela.blit(txt_restart, (LARGURA//2 - txt_restart.get_width()//2, ALTURA - 100))
        pygame.display.flip()
    relogio.tick(60)