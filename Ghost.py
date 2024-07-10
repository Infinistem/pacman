import pygame, sys, math, heapq

WIDTH = 730
HEIGHT = 800


class Ghost:
    def __init__(self, rect, name, id, level, pacman):
        self.state = ""
        self.level = level
        self.pacman = pacman
        self.ids = id
        self.name = name
        self.sprite = "Images" + "\\" + name + '.png'
        self.target = [] # x, y position in map array
        self.scatter = False
        self.rect = rect
        self.direction = 'N' 
        self.speed = 1 
        self.path = []
        self.speedIncrease = .1 # every level increase the speed!
    def findTarget(self):
        if self.name == 'Blinky': # find the target destination. Blinky always targets pacman in a chase like pattern
            col, row = self.level.getArrayCoords([self.pacman.rect.left, self.pacman.rect.top])
            self.target = [row, col] # always try to go to pacmans position
    def findPathToTarget(self):
        pass
    def followPath(self):
        if self.direction == 'N':
            pass
        

    
