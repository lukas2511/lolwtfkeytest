from evdev import InputDevice
from select import select
import pygame
import sys

size = width, height = 1417,595
black = 0, 0, 0
blue = 0, 0, 255

screen = pygame.display.set_mode(size)

keyboard = pygame.image.load("keyboard.png")
keyboardrect = keyboard.get_rect()

keyboardrect.left = 0
keyboardrect.top = 0

screen.fill(black)
screen.blit(keyboard, keyboardrect)
pygame.display.flip()

dev = InputDevice('/dev/input/event0')

keys = {}

positions = {
    '41': (54, 190, 56, 55), # ^
     '2': (112, 190, 56, 55), # 1
     '3': (170, 190, 56, 55), # 2
     '4': (228, 190, 56, 55), # 3
     '5': (286, 190, 56, 55), # 4
     '6': (344, 190, 56, 55), # 5
     '7': (402, 190, 56, 55), # 6
     '8': (460, 190, 56, 55), # 7
     '9': (518, 190, 56, 55), # 8
    '10': (576, 190, 56, 55), # 9
    '11': (634, 190, 56, 55), # 0
    '12': (692, 190, 56, 55), # sz
    '13': (750, 190, 56, 55), # strichdingsi

    '16': (142, 248, 56, 55), # q
    '17': (200, 248, 56, 55), # w
    '18': (258, 248, 56, 55), # e 
    '19': (316, 248, 56, 55), # r
    '20': (374, 248, 56, 55), # t
    '21': (432, 248, 56, 55), # z
    '22': (490, 248, 56, 55), # u
    '23': (548, 248, 56, 55), # i
    '24': (606, 248, 56, 55), # o
    '25': (664, 248, 56, 55), # p
    '26': (722, 248, 56, 55), # ue
    '27': (780, 248, 56, 55), # +*~

    '30': (158, 306, 56, 55), # a
    '31': (216, 306, 56, 55), # s
    '32': (274, 306, 56, 55), # d
    '33': (332, 306, 56, 55), # f
    '34': (390, 306, 56, 55), # g
    '35': (448, 306, 56, 55), # h
    '36': (506, 306, 56, 55), # j
    '37': (564, 306, 56, 55), # k
    '38': (622, 306, 56, 55), # l
    '39': (680, 306, 56, 55), # oe
    '40': (738, 306, 56, 55), # ae
    '43': (796, 306, 56, 55), # #

    '86': (130, 364, 56, 55), # <
    '44': (188, 364, 56, 55), # y
    '45': (246, 364, 56, 55), # x
    '46': (304, 364, 56, 55), # c
    '47': (362, 364, 56, 55), # v
    '48': (420, 364, 56, 55), # b
    '49': (478, 364, 56, 55), # n
    '50': (536, 364, 56, 55), # m
    '51': (594, 364, 56, 55), # ,
    '52': (652, 364, 56, 55), # .
    '53': (710, 364, 56, 55), # -

    '29': (55, 421, 85, 55), # ctrl
   '125': (143, 421, 53, 55), # tux
    '56': (199, 421, 85, 55), # alt
    '57': (286, 421, 402, 55), # space
   '100': (690, 421, 85, 55), # altgr
    '97': (832, 421, 85, 55), # ctrlright
}

while True:
   r,w,x = select([dev], [], [])
   for event in dev.read():
       if event.type == 1 and (event.value == 1L or event.value == 0L):
           if event.value == 0L:
               keys.update({str(event.code): False})
           elif event.value == 1L:
               keys.update({str(event.code): True})
       screen.blit(keyboard, keyboardrect)
       for key, value in keys.iteritems():
           if value and str(key) in positions:
               box = pygame.Rect(positions.get(str(key)))
               rect = pygame.draw.rect(screen,blue,box,0)
       pygame.display.flip()
