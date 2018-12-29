import pygame
from pygame.locals import *
from random import randint
from DB_PingPong import *

class Pingpong:
    def __init__(self):
        self.start = pygame.init()
        self.tela = pygame.display.set_mode([600, 400])
        self.corBranca = (255, 255, 255)
        self.corPreto = (0, 0, 0)
        self.barrinha_x = randint(0, 500)
        self.barrinha_y = 340
        self.barrinha_altura = 20
        self.barrinha_largura = 100
        self.quadradinho_x = randint(0, 580)
        self.quadradinho_y = 10
        self.quadradinho_altura = 20
        self.quadradinho_largura = 20
        self.contador_placar = 0
        self.quadradinho_velocidade = 10
        self.barrinha_velocidade = 20
        self.nome = pygame.display.set_caption("COLETAR DADOS Pig Pong")
        self.taxa_atualizacao_frame = pygame.time.Clock()

    def barrinha(self):
        return pygame.draw.rect(self.tela, self.corBranca, [self.barrinha_x, self.barrinha_y, self.barrinha_largura, self.barrinha_altura])

    def quadradinho(self):
        return pygame.draw.rect(self.tela, self.corBranca, [self.quadradinho_x, self.quadradinho_y, self.quadradinho_largura, self.quadradinho_altura])

    def DB_movimento(self):
        return [self.quadradinho_x, self.barrinha_x + self.barrinha_largura // 2]

    def loop_quadradinho(self):
        if self.quadradinho_y >= 400:
            self.quadradinho_y = 0
            self.contador_placar = 0
            self.quadradinho_x = randint(0, 580)

    def impedir_laterais(self):
        if self.barrinha_x <= 0:
            self.barrinha_x = 0
        if self.barrinha_x >= 500:
            self.barrinha_x = 500

    def colisao(self):
        if self.quadradinho().colliderect(self.barrinha()):
            self.quadradinho_y = 0
            self.contador_placar += 1
            self.quadradinho_x = randint(0, 580)

    def maior_pontuacao(self):
        if self.contador_placar > self.score_maximo:
            self.score_maximo = self.contador_placar

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
        self.loop_quadradinho()
        self.quadradinho_y += self.quadradinho_velocidade
        self.impedir_laterais()
        self.quadradinho()
        self.barrinha()
        self.colisao()
        pygame.display.flip()
        self.taxa_atualizacao_frame.tick(27)


if __name__ == '__main__':
    game = Pingpong()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    game.iniciar(0)
                if event.key == K_RIGHT:
                    game.iniciar(1)






