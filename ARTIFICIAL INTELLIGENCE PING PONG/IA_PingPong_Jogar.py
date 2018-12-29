import pygame
from pygame.locals import *
from random import randint
from Rede_Neural import *


class Pingpong:
    def __init__(self):
        self.start = pygame.init()
        self.tela = pygame.display.set_mode([950, 600])
        self.corBranca = (255, 255, 255)
        self.corVermelha = (255, 0, 0)
        self.corPreto = (0, 0, 0)
        self.barrinha_x = randint(0, 830)
        self.barrinha_y = 470
        self.barrinha_altura = 20
        self.barrinha_largura = 120
        self.quadradinho_x = randint(0, 870)
        self.quadradinho_y = 10
        self.quadradinho_altura = 20
        self.quadradinho_largura = 20
        self.contador_placar = 0
        self.quadradinho_velocidade = 10
        self.barrinha_velocidade = 20
        self.nome = pygame.display.set_caption("Inteligência Artificial Ping Pong - Aprendizado supervisionado")
        self.taxa_atualizacao_frame = pygame.time.Clock()
        self.modo_expert = 0
        self.expert_ativar = False
        self.fps = 27

    def barrinha(self):
        return pygame.draw.rect(self.tela, self.corVermelha, [self.barrinha_x, self.barrinha_y, self.barrinha_largura, self.barrinha_altura])

    def quadradinho(self):
        return pygame.draw.rect(self.tela, self.corBranca, [self.quadradinho_x, self.quadradinho_y, self.quadradinho_largura, self.quadradinho_altura])

    def DB_movimento(self):
        return [self.quadradinho_x, self.barrinha_x + self.barrinha_largura // 2]

    def loop_quadradinho(self):
        if self.quadradinho_y >= 593:
            self.quadradinho_y = 0
            self.contador_placar = 0
            self.quadradinho_x = randint(0, 880)

    def impedir_laterais(self):
        if self.barrinha_x <= 0:
            self.barrinha_x = 0
        if self.barrinha_x >= 830:
            self.barrinha_x = 830

    def colisao(self):
        if self.quadradinho().colliderect(self.barrinha()):
            self.quadradinho_y = 0
            self.contador_placar += 1
            self.fps += self.modo_expert
            self.quadradinho_x = randint(0, 880)

    def expert(self):
        if self.expert_ativar == True:
            self.modo_expert = 5

    def iniciar(self, ativar):
        for event in pygame.event.get():
            if event.type == QUIT:
                return quit()

        pygame.event.pump()

        if ativar == 0:
            self.barrinha_x -= self.barrinha_velocidade

        elif ativar == 1:
            self.barrinha_x += self.barrinha_velocidade

        self.tela.fill(self.corPreto)
        self.expert()
        self.contadores("PLACAR: ", self.contador_placar, 410, 580, 505, 579)
        self.loop_quadradinho()
        self.quadradinho_y += self.quadradinho_velocidade
        self.impedir_laterais()
        self.quadradinho()
        self.barrinha()
        self.colisao()
        pygame.display.flip()
        self.taxa_atualizacao_frame.tick(self.fps)

    def contadores(self, texto, contador, esquerda_direitaT, alturaT, esqueda_direitaC, alturaC):
        pygame.font.init()
        font_padrao1 = pygame.font.SysFont("ABCD", 30)
        font_padrao2 = pygame.font.SysFont("ABCD", 32)
        text1 = font_padrao1.render(texto, 1, (255, 255, 255))
        text2 = font_padrao2.render(str(contador), 1, (255, 255, 255))
        self.tela.blit(text1, (esquerda_direitaT, alturaT))
        self.tela.blit(text2, (esqueda_direitaC, alturaC))


if __name__ == '__main__':
    game = Pingpong()

    input = np.array(input("dados-33.txt"))
    output = np.array(output("dados-33.txt"))

    w1 = IA_dados_arquivoTXT("peso-w1.txt")

    w2 = IA_dados_arquivoTXT("peso-w2.txt")

    #w1 = None
    #w2 = None

    game.expert_ativar = False

    salvar_pesos = False

    IA = NeuralNetwork(2, 30, 1, input, output, w1, w2, salvar_pesos, 100000)

    IA.verificando_pesos()

    while True:

        #IA.treinamento()
        if IA.resultado_saida(game.DB_movimento()) > 0.5:
            game.iniciar(1)

        else:
            game.iniciar(0)

