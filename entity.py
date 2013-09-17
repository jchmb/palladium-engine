'''
@class Entity
@abstract
'''
class Entity:
	'''
	Constructor.

	@param (int, int) position

	@var int x
	@var int y
	'''
	def __init__(self, (x, y)):
		self.x = x
		self.y = y

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
	Draw this entity on the screen.

	@param Surface screen
	'''
	def draw(self, screen):
		pass

	'''
	Execute a single step for this entity.
	'''
	def step(self):
		pass