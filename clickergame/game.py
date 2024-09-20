import pygame
from entities import *
from config import *


pygame.init()

class Game:

    def __init__(self):

        self.fps = FPS
        self.size = (WIDTH,HEIGHT)
        self.clock = pygame.time.Clock()
        self.win = pygame.display.set_mode(self.size)
        self.entities = []
        self.running = True

        self.score = 0

        self.cookie = Entity(WIDTH/2, HEIGHT/2, 150,150, 'assets/sprites/cookie.png', self)
        self.entities.append(self.cookie)

        self.font = pygame.font.Font("assets/fonts/slkscr.ttf", 150)

        self.score_surface = self.font.render(str(self.score), True, (0,0,0))


        self.upgrader = Upgrader(50, 550, 75,75, (0,0,0), "assets/sprites/Button+1.png", self)

        self.entities.append(self.upgrader)

        self.increment = incrment

    def update(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                if self.cookie.Clicked(pygame.mouse.get_pos()):

                    self.cookie.popup(self.cookie.Clicked(pygame.mouse.get_pos()), 'assets/sprites/cookie.png')
                    self.score += self.increment
                    print(self.score)

                if self.upgrader.Clicked(pygame.mouse.get_pos()):

                    self.upgrader.popup(self.upgrader.Clicked(pygame.mouse.get_pos()), 'assets/sprites/Button+1.png')
                    self.increment += 1


            if event.type == pygame.MOUSEBUTTONUP:

                self.cookie.popup(False, 'assets/sprites/cookie.png')
                self.upgrader.popup(False, 'assets/sprites/Button+1.png')


        for entity in self.entities:
            entity.update()
            self.win.blit(self.score_surface, (300, 0))



    def run(self):

        while self.running:
            self.win.fill("white")
            self.clock.tick(self.fps)
            self.update()

            self.score_surface = self.font.render(str(self.score), True, (0,0,0))

            pygame.display.update()


if  __name__ == '__main__':
    game = Game()
    game.run()
