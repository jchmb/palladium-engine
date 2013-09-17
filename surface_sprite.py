from sprite import Sprite

'''
@class SurfaceSprite
@extends Sprite
'''
class SurfaceSprite(Sprite):
	'''
	Constructor.

	@param Surface surface

	@var Surface surface
	'''
	def __init__(self, surface):
		self.surface = surface

	'''
	Draw this Sprite on the screen.

	@param Surface screen
	@param (int, int) position
	'''
	def draw(self, screen, position):
		screen.blit(self.surface, position)

	'''
	Execute a single step.
	'''
	def step(self):
		pass