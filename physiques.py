import pygame
from random import randint
pygame.init()

def redrawGameWindow():
    pygame.draw.rect(win,(0,0,0),(0,0,500,500))
    pygame.draw.rect(win,(255,255,255),(player.x-(player.width/2),player.y-(player.height/2),width,height))
    for i in rigi_list:
        pygame.draw.rect(win,(255,0,0),(i.x-(i.width/2),i.y-(i.height/2),i.width,i.height))
    pygame.display.update()

class RigidBody:
    def __init__(self, width, height, center_x, center_y, image=None):
        self.x = center_x
        self.y = center_y
        self.width = width
        self.height = height
        self.image = image

    def collisionCheck(self, character):
        detect=(self.x - (self.width/2)<character.x<self.x + (self.width/2),self.y - (self.height/2)<character.y<self.y + (self.height/2))
        return detect

class Character:
    def __init__(self, width, height, spawn_x, spawn_y, velocity_x, velocity_y, image=None, grav=False):
        self.width = width
        self.height = height
        self.x = spawn_x
        self.y = spawn_y
        self.vel_x = velocity_x
        self.vel_y = velocity_y
        self.rectangle = (self.x-self.width/2,self.y-self.height/2, width, height)

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Bilibu")
width = 64
height = 64
x = 0
y = 0
velocity = 2
run = True
grav = 1
char = pygame.image.load('/home/guillaume/Documents/python/Pygame/truc1/standing.png')
player = Character(64,64,300,300,10,10, char)
global gravi_list
gravi_list = []
global nograv_list
nograv_list = []
global rigi_list
rigi_list = []
gravi_list.append(player)
rigi_list.append(RigidBody(300,100,300,300))
rigi_list.append(RigidBody(500,100,250,450))
inJump = False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    player = gravi_list[0]
    if keys[pygame.K_RIGHT]:
        player.vel_x = 1
    elif keys[pygame.K_LEFT]:
        player.vel_x = -1
    if keys[pygame.K_UP]:
        player.vel_y = 5
    player.x += player.vel_x
    player.y -= player.vel_y
    for i in rigi_list:
        collisionCheck = i.collisionCheck(player)
        print(collisionCheck)
        if collisionCheck[0]:
            if player.x >= i.x + (i.width/2):
                player.x = i.x + (i.width/2)
            else:
                player.x = i.x - (i.width/2)
        if collisionCheck[1]:
            if player.y >= i.y + (i.height/2):
                player.y = i.y + (i.height/2)
            else:
                player.y = i.y - (i.height/2)
    print(player.x);print(player.y)
    if player.vel_y != 0:
        print("Nope")
        player.vel_y -= grav
    redrawGameWindow()
    player.vel_x = 0
    player.vel_y = 0

pygame.quit()
