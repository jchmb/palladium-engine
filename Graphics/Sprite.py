import pygame

'''
@class Sprite
@abstract
'''
class Sprite:
	'''
	Constructor.
	'''
	def __init__(self):
		pass

	'''
	Draw this Sprite.

	@param Surface screen
	'''
	def onDraw(self, screen):
		pass

	'''
	Execute a single step for this Sprite.
	'''
	def onStep(self):
		pass