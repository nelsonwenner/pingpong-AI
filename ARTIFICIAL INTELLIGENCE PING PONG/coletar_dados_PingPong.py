import pygame
from pygame.locals import *
from controle_de_dados_PingPong import *
from random import randint

class Pingpong:
    def __init__(self):
        self.start = pygame.init()
        self.criar_respositorio_de_dados = criando_repositorio_dados_pingpong()
        self.nome_arquivo_dados = "dados-" + str(randint(0, 100)) + ".txt"
        self.tela = pygame.display.set_mode([950, 600])
        self.nome = pygame.display.set_caption("Coletor de dados Ping Pong")
        self.taxa_atualizacao_frame = pygame.time.Clock()
        self.corBranca = (255, 255, 255)
        self.corPreto = (0, 0, 0)
        self.barrinha_x = randint(0, 830)
        self.barrinha_y = 470
        self.barrinha_altura = 20
        self.barrinha_largura = 120
        self.barrinha_velocidade = 20
        self.quadradinho_x = randint(0, 870)
        self.quadradinho_y = 0
        self.quadradinho_altura = 20
        self.quadradinho_largura = 20
        self.quadradinho_velocidade = 10
        self.APRENDIZAGEM_DADOS = []
        self.ativar = None
        self.lado_quadradinho = None
        self.sair = False

    def iniciar(self):
        while self.sair != True:
            try:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        criar_arquivoTXT(self.nome_arquivo_dados)
                        guardar_arquivoTXT(self.APRENDIZAGEM_DADOS, self.nome_arquivo_dados)
                        self.sair = True

                    if event.type == KEYDOWN:  # Escutando teclado
                        if event.key == K_LEFT:  # Tecla esquerda
                            self.ativar = 0
                        if event.key == K_RIGHT:  # Tecla direita
                            self.ativar = 1

                self.movimento(self.ativar)
                self.lado_bolinha()
                self.APRENDIZAGEM_DADOS.append([[self.quadradinho_x, self.barrinha_x + self.barrinha_largura // 2], [self.lado_quadradinho]])

            except Exception:
                continue

        print("\nBase de dados salva: {}".format(self.nome_arquivo_dados))
        pygame.quit()

    def lado_bolinha(self):
        if self.quadradinho_x > self.barrinha_x + self.barrinha_largura // 2:
            self.lado_quadradinho = 1
        elif self.lado_quadradinho < self.barrinha_x:
            self.lado_quadradinho = 0

    def barrinha(self):
        return pygame.draw.rect(self.tela, self.corBranca, [self.barrinha_x, self.barrinha_y, self.barrinha_largura, self.barrinha_altura])

    def quadradinho(self):
        return pygame.draw.rect(self.tela, self.corBranca, [self.quadradinho_x, self.quadradinho_y, self.quadradinho_largura, self.quadradinho_altura])

    def loop_quadradinho(self):
        if self.quadradinho_y >= 593:
            criar_arquivoTXT(self.nome_arquivo_dados)
            guardar_arquivoTXT(self.APRENDIZAGEM_DADOS, self.nome_arquivo_dados)
            self.sair = True

    def impedir_laterais(self):
        if self.barrinha_x <= 0:
            self.barrinha_x = 0
        if self.barrinha_x >= 830:
            self.barrinha_x = 830

    def colisao(self):
        if self.quadradinho().colliderect(self.barrinha()):
            self.quadradinho_y = 0
            self.quadradinho_x = randint(0, 880)

    def movimento(self, ativar):
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if ativar == 0:
            if keys[K_LEFT]:
                self.barrinha_x -= self.barrinha_velocidade

        elif ativar == 1:
            if keys[K_RIGHT]:
                self.barrinha_x += self.barrinha_velocidade

        self.tela.fill(self.corPreto)
        self.impedir_laterais()
        self.colisao()
        self.barrinha()
        self.quadradinho_y += self.quadradinho_velocidade
        self.loop_quadradinho()
        self.quadradinho()
        self.taxa_atualizacao_frame.tick(15)
        pygame.display.flip()


if __name__ == '__main__':
    Pingpong().iniciar()