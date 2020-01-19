from database.controller.db import *
from pygame.locals import *
from random import randint
import pygame, random, time, sys


class PingPongCollect:

    width = 950
    height = 600

    color_white = (255, 255, 255)
    color_black = (0, 0, 0)

    pallet_x = 500
    pallet_y = 470
    pallet_velocity = 20
    pallet_height = 20
    pallet_width = 120

    ball_x = 475
    ball_y = 10
    ball_height = 20
    ball_width = 20
    ball_velocity = 10
    
    learning_data = []
   
    side_ball = 1
    activate = None
    exit = False

    x_change = random.randint(10, 13)
    y_change = random.randint(10, 13)

    def __init__(self):
        self.name = pygame.display.set_caption("Data collector pingpong")
        self.name_file_data = "data-{}.txt".format(str(randint(0, 100)))
        self.screen = pygame.display.set_mode([self.width, self.height])
        self.frame = pygame.time.Clock()
        self.start = pygame.init()

    def running(self):
        while not self.exit:
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    create_file('/database/data/', self.name_file_data)
                    save_data('/database/data/', self.learning_data, self.name_file_data)
                    self.exit = True

                if event.type == KEYDOWN: 
                    if event.key == K_LEFT:  
                        self.activate = 0
                    if event.key == K_RIGHT:
                        self.activate = 1

            self.movement(self.activate)
            self.get_side_ball()

            '''
            index: 0 = ball_x, pallet_x
            index: 1 = side_ball

            '''
            self.learning_data.append([[self.ball_x, self.pallet_x + self.pallet_width // 2], [self.side_ball]])
        
        print("\nSaved database: {}".format(self.name_file_data))
        pygame.quit()
        sys.exit()

    def get_side_ball(self):
        if self.ball_x > self.pallet_x + self.pallet_width // 2:
            self.side_ball = 1
        elif self.side_ball < self.pallet_x:
            self.side_ball = 0

    def pallet(self):
        return pygame.draw.rect(self.screen, self.color_white, 
        [self.pallet_x, self.pallet_y, self.pallet_width, self.pallet_height])

    def ball(self):
        return pygame.draw.circle(self.screen, self.color_white, 
        (self.ball_x, self.ball_y), 15, 0)

    def loop_ball(self):
        if self.ball_y > 580:
            create_file('/database/data/', self.name_file_data)
            save_data('/database/data/', self.learning_data, self.name_file_data)
            self.exit = True

    def ball_physic(self):
        if self.ball_x > (self.width - 15) or self.ball_x < 15:
	        self.x_change = self.x_change * -1
        if self.ball_y > (self.height - 15) or self.ball_y < 15:
	        self.y_change = self.y_change * -1

    def prevent_sides(self):
        if self.pallet_x <= 0:
            self.pallet_x = 0
        if self.pallet_x >= 830:
            self.pallet_x = 830

    def collision(self):
        if self.ball().colliderect(self.pallet()):
            self.y_change = self.y_change * -1

    def movement(self, activate):
        
        pygame.event.pump()
        keys = pygame.key.get_pressed()

        if activate == 0:
            if keys[K_LEFT]:
                self.pallet_x -= self.pallet_velocity

        elif activate == 1:
            if keys[K_RIGHT]:
                self.pallet_x += self.pallet_velocity

        self.ball_x += self.x_change
        self.ball_y += self.y_change

        self.screen.fill(self.color_black)
        self.ball_physic()
        self.prevent_sides()
        self.collision()
        self.ball()
        self.pallet()

        self.loop_ball()
        self.frame.tick(15)
        pygame.display.flip()
        time.sleep(0.015)


if __name__ == '__main__':
    PingPongCollect().running()