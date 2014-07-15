import pygame

'''
@class Keyboard
'''
class Keyboard:
	'''
	Constructor.

	@var boolean[] the keys pressed
	'''
	def __init__(self):
		self.keys = []

	'''
	Execute a single step event.
	'''
	def onStep(self):
		self.keys = pygame.key.get_pressed()

	'''
	Check whether the given key is pressed.

	@param int key
	@return boolean
	'''
	def isPressed(self, key):
		return self.keys[key]