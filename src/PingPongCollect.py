from database.controller.db import *
from pygame.locals import *
from random import randint
import pygame


class Pingpong:

    color_white = (255, 255, 255)
    color_black = (0, 0, 0)

    pallet_x = randint(0, 830)
    pallet_y = 470
    pallet_velocity = 20
    pallet_height = 20
    pallet_width = 120

    ball_x = 500
    ball_y = 0
    ball_height = 20
    ball_width = 20

    learning_data = []
   
    side_ball = None
    activate = None
    exit = False

    def __init__(self):
        self.name = pygame.display.set_caption("Data collector pingpong")
        self.name_file_data = "data-{}.txt".format(str(randint(0, 100)))
        self.screen = pygame.display.set_mode([950, 600])
        self.frame = pygame.time.Clock()
        self.start = pygame.init()

    def running(self):
        while not self.exit:
            try:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        create_file(self.name_file_data, '/')
                        save_data(self.learning_data, self.name_file_data, '/')
                        self.exit = True

                    if event.type == KEYDOWN:  # Escutando teclado
                        if event.key == K_LEFT:  # Tecla esquerda
                            self.activate = 0
                        if event.key == K_RIGHT:  # Tecla direita
                            self.activate = 1

                self.movement(self.activate)
                self.get_side_ball()

                self.learning_data.append({
                'ball_x': self.ball_x, 
                'pallet_x': self.pallet_x + self.pallet_width // 2, 
                'side_ball': self.side_ball})

            except Exception:
                continue

        print("\nSaved database: {}".format(self.name_file_data))
        pygame.quit()

    def get_side_ball(self):
        if self.ball_x > self.pallet_x + self.pallet_width // 2:
            self.side_ball = 1
        elif self.side_ball < self.pallet_x:
            self.side_ball = 0

    def pallet(self):
        return pygame.draw.rect(self.screen, self.color_white, 
        [self.pallet_x, self.pallet_y, self.pallet_width, self.pallet_height])

    def ball(self):
        return pygame.draw.rect(self.screen, self.color_white, 
        [self.ball_x, self.ball_y, self.ball_width, self.ball_height])

    def loop_ball(self):
        if self.ball_y >= 593:
            create_file(self.name_file_data)
            save_data(self.learning_data, self.name_file_data)
            self.exit = True

    def prevent_sides(self):
        if self.pallet_x <= 0:
            self.pallet_x = 0
        if self.pallet_x >= 830:
            self.pallet_x = 830

    def collision(self):
        if self.ball().colliderect(self.pallet()):
            self.ball_y = 0
            self.ball_x = randint(0, 880)

    def movement(self, activate):
        
        pygame.event.pump()
        keys = pygame.key.get_pressed()

        if activate == 0:
            if keys[K_LEFT]:
                self.pallet_x -= self.pallet_velocity

        elif activate == 1:
            if keys[K_RIGHT]:
                self.pallet_x += self.pallet_velocity

        self.screen.fill(self.color_black)
        self.prevent_sides()
        self.collision()
        self.pallet()
        self.ball_y += self.pallet_velocity
        self.loop_ball()
        self.ball()
        self.frame.tick(15)
        pygame.display.flip()


if __name__ == '__main__':
    Pingpong().running()