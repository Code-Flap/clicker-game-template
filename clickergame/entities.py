import pygame


class Entity:

    def __init__(self, x, y, width, height, img, game):

        self.game = game

        self.width = width
        self.height = height

        self.x = x
        self.y = y

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.img = pygame.image.load(img).convert_alpha()

        self.img = pygame.transform.scale(self.img, (self.width, self.height))

        self.clicked = False


        self.game.entities.append(self)


    def update(self):

        self.game.win.blit(self.img, (self.x-(self.width/2), self.y-(self.height/2)))


    def Clicked(self, mouse_cords):

        # print(mouse_cords)

        MouseRect = pygame.Rect(mouse_cords[0], mouse_cords[1], 32, 32)

        if MouseRect.colliderect(self.rect):
            self.clicked = True
        else:
            self.clicked = False

        return self.clicked

    def popup(self, _situation, img):

        if _situation:
            self.img = pygame.image.load(img).convert_alpha()
            self.img = pygame.transform.scale(self.img, (self.width+20, self.height+20))
            self.rect = pygame.Rect(self.x, self.y, self.width+20, self.height+20)

        else:
            self.img = pygame.image.load(img).convert_alpha()
            self.img = pygame.transform.scale(self.img, (self.width, self.height))
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)



class Upgrader(Entity):

    def __init__(self, x, y, width, height, color, img, game):

        super().__init__(
            x=x,
            y=y,
            width=width,
            height=height,
            img=img,
            game=game
        )
