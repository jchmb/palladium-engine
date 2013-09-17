'''
@class Entity
@abstract
'''
class Entity:
	'''
	Constructor.

	@param (int, int) position
	@param Sprite sprite

	@var int x
	@var int y
	@var Sprite sprite
	'''
	def __init__(self, (x, y), sprite):
		self.x = x
		self.y = y
		self.sprite = sprite

	'''
	Execute this after the step.
	'''
	def afterStep(self):
		pass

	'''
	Execute this before the step.
	'''
	def beforeStep(self):
		pass

	'''
	Draw this Entity on the screen.

	@param Surface screen
	'''
	def onDraw(self, screen):
		self.sprite.onDraw(screen, (self.x, self.y))

	'''
	Set the Sprite of this Entity.

	@param Sprite sprite
	'''
	def setSprite(self, sprite):
		self.sprite = sprite

	'''
	Execute a single step for this Entity.
	'''
	def onStep(self):
		self.sprite.onStep()