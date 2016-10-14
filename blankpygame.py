# -*- coding:utf-8 -*-
import pygame, sys
from pygame.locals import *

pygame.init()	#pygame初始化
DISPLAYSURF = pygame.display.set_mode((400, 300))	#返回窗口对象
pygame.display.set_caption('Hello World!')
while True: # main game loop 
	for event in pygame.event.get():	#返回pygame.event.Event对象列表
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
