from network.NeuralNetwork import *
from pygame.locals import *
from random import randint
import pygame


class Pingpong:

    color_white = (255, 255, 255)
    color_red = (255, 0, 0)
    color_black = (0, 0, 0)

    pallet_x = randint(0, 830)
    pallet_y = 470
    pallet_height = 20
    pallet_width = 120
    pallet_velocity = 20

    ball_x = randint(0, 870)
    ball_y = 10
    ball_height = 20
    ball_width = 20
    ball_velocity = 10

    count_score = 0

    mode_expert = 0

    expert_activate = False

    fps = 27

    def __init__(self):
        self.start = pygame.init()
        self.screen = pygame.display.set_mode([950, 600])
        self.name = pygame.display.set_caption("Artificial Intelligence Ping Pong - Supervised learning")
        self.frame = pygame.time.Clock()

    def pallet(self):
        return pygame.draw.rect(self.screen, self.color_red, [self.pallet_x, self.pallet_y, self.pallet_width, self.pallet_height])

    def ball(self):
        return pygame.draw.rect(self.screen, self.color_white, [self.ball_x, self.ball_y, self.ball_width, self.ball_height])

    def movement(self):
        return [self.ball_x, self.pallet_x + self.pallet_width // 2]

    def loop_ball(self):
        if self.ball_y >= 593:
            self.ball_y = 0
            self.count_score = 0
            self.ball_x = randint(0, 880)

    def prevent_sides(self):
        if self.pallet_x <= 0:
            self.pallet_x = 0
        if self.pallet_x >= 830:
            self.pallet_x = 830

    def collision(self):
        if self.ball().colliderect(self.pallet()):
            self.ball_y = 0
            self.count_score += 1
            self.fps += self.mode_expert
            self.ball_x = randint(0, 880)

    def expert(self):
        if self.expert_activate:
            self.mode_expert = 5

    def play(self, activate):
        for event in pygame.event.get():
            if event.type == QUIT:
                return quit()

        pygame.event.pump()

        if activate == 0:
            self.pallet_x -= self.pallet_velocity

        elif activate == 1:
            self.pallet_x += self.pallet_velocity

        self.screen.fill(self.color_black)
        self.expert()
        self.counter("PLACAR: ", self.count_score, 410, 580, 505, 579)
        self.loop_ball()
        self.ball_y += self.ball_velocity
        self.prevent_sides()
        self.ball()
        self.pallet()
        self.collision()
        pygame.display.flip()
        self.frame.tick(self.fps)

    def counter(self, text, count, left_rightT, heightT, left_rightC, heightC):
        pygame.font.init()
        font_padrao1 = pygame.font.SysFont("ABCD", 30)
        font_padrao2 = pygame.font.SysFont("ABCD", 32)
        text1 = font_padrao1.render(text, 1, (255, 255, 255))
        text2 = font_padrao2.render(str(count), 1, (255, 255, 255))
        self.screen.blit(text1, (left_rightT, heightT))
        self.screen.blit(text2, (left_rightC, heightC))


if __name__ == '__main__':
    game = Pingpong()

    input = np.array(get_data('/database/data/data-94.txt', 0))
    output = np.array(get_data('/database/data/data-94.txt', 1))

    w1 = get_data('/database/weights/weight-w1.txt', flag=False)
    w2 = get_data('/database/weights/weight-w2.txt', flag=False)

    #w1 = None
    #w2 = None

    game.expert_activate = False

    save_weights = False

    IA = NeuralNetwork(2, 30, 1, input, output, w1, w2, save_weights, 100000)

    IA.checking_exists_weights()

    while True:

        #IA.training()

        if IA.result_output(game.movement()) > 0.5:
            game.play(1)
        else:
            game.play(0)