class Pacman:
    def __init__(self, pos, level, rect):
        self.level = level # reference to object
        self.direction = '' # nothing means stil
        self.speed = 1.5 # 1 tile / s. 1 tile = 35 pixels^2
        self.pos = list(pos)
        self.rect = rect
        self.deg = [] # n, s, e, w
        self.rotation = 0 # rotate 360-current roation and then do the correct rotation. Makes this a bit easier
     # coordinates in Level.map # coordinates got from surfaces used to determine a collision with any given thing
    def turn(d):
        self.direction = d
    def getPos(self, x):
        pass
    def pointOnCircum():
        pass 
    
        
