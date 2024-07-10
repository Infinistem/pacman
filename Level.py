import pygame, sys, math
WIDTH = 730
HEIGHT = 800
class Level:
    def __init__(self, screen):
        self.screen = screen
        self.width = 35
        self.height = 35
        self.map = []
        self.level = 0
        self.score = 0
        self.fruit = "cherry"
        self.ids = {"Blinky":0, "Pinky":1, "Inky":2, "Clyde":3, "Cherry":12}
        self.surfaces = [[], [], [], [], [],[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []] # log the surfaces in case we need them
        self.circles = []
        self.lives = 'XXX'
        self.extraLive = False # aparently the origonal game gave you a 4th one at 10000 points
        self.reset()
    def render(self):
        r = 0
        self.surfaces = [[], [], [], [], [],[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
        self.circles = []
        if not self.level == 255:
            for x in self.map:
                r+=1
                for y in range(len(x)):
                    row = list(x)
                    if row[y] == 'B':
                        self.surfaces[(r-1)].append(pygame.Rect(35*y, 35*(r-1)+80, self.width, self.height))
                        pygame.draw.rect(self.screen, (0, 0, 200), pygame.Rect(35*y, 35*(r-1)+80, self.width, self.height))
                    elif row[y] == 'Q':
                        self.circles.append(pygame.Rect(35*y+15, 35*(r-1)+100, self.width, self.height))
                        pygame.draw.circle(self.screen,(250, 250, 250),(35*y+15, 35*(r-1)+100), 5)
                    elif row[y] == 'O':
                        self.circles.append(pygame.Rect(35*y+15, 35*(r-1)+100, self.width, self.height))
                        pygame.draw.circle(self.screen,(250, 250, 200),(35*y+15, 35*(r-1)+100), 8)
                    elif row[y] == 'H':
                        self.surfaces[(r-1)].append(pygame.Rect(35*y, 35*(r-1)+80, self.width, self.height/2))
                        pygame.draw.rect(self.screen, (200, 200, 200), pygame.Rect(35*y, 35*(r-1)+80, self.width, self.height/2))
                    elif row[y] == 'F':
                        self.circles.append(pygame.Rect(35*y, 35*(r-1)+80, self.width/2, self.height/2))
                        image = pygame.transform.scale(self.getImg(), (30, 30))
                        self.screen.blit(image, pygame.Rect(35*y, 35*(r-1)+80, self.width/2, self.height/2))
    def getArrayCoords(self,pos): # take an entities position and return what square it has entered
            posx = math.floor((pos[0]) / 35)
            posy = math.floor((pos[1]-80) / 35)
            return posx, posy
    def getImg(self): 
        if self.level == 0:
            self.fruit = "cherry"
            return pygame.image.load("Images\\cherry.png")
        elif self.level == 1:
            self.fruit = 'berry'
            return pygame.image.load("Images\\berry.png")
        elif self.level == 2:
            self.fruit = 'orange'
            return pygame.image.load("Images\\orange.png")
        elif self.level == 3:
            self.fruit = 'apple'
            return pygame.image.load("Images\\apple.png")
        elif self.level == 4:
            self.fruit = 'melon'
            return pygame.image.load("Images\\melon.png")
    def scatterGhosts(self):
        pass
    def reset(self):
        self.map = [
         "NBBBBBBBBBBBBBBBBBBBN", #B F == fruit gen spot H = Hatch, N = nothing, O = power thing, G = Ghosts (just to remidn me doesnt render as tile)
         "NBQQQQQQQQBQQQQQQQQBN",
         "NBOBBQBBBQBQBBBQBBOBN",
         "NBQQQQQQQQQQQQQQQQQBN",
         "NBQBBQBQBBBBBQBQBBQBN",
         "NBQQQQBQQQBQQQBQQQQBN",
         "NBBBBQBQBNBNBQBQBBBBN",
		 "NNNNBNBQNNNNNQBNBNNNN",
		 "BBBBBQBQBBHBBQBQBBBBB",
		 "NNNNNNQQBGGGBQQNNNNNN",
		 "BBBBBQBQBBBBBQBQBBBBB",
		 "NNNNBQBNNNNNNNBQBNNNN",
		 "NBBBBQBNBBBBBNBQBBBBN",
		 "NBQQQQQQQQBQQQQQQQQBN",
		 "NBQBBQBBBQBQBBBQBBQBN",
		 "NBOQBQQQQQFQQQQQBQOBN",
		 "NBBQBQBQBBBBBQBQBQBBN",
		 "NBQQQQBQQQQQQQBQQQQBN",
		 "NBBBBBBBBBBBBBBBBBBBN",
		
        ]


        
