import pygame, sys

'''
@class App
@abstract
'''
class App:
	'''
	Constructor.

	@param (int, int) size

	@var (int, int) size
	@var Surface screen
	@var Controller controller
	'''
	def __init__(self, size):
		pygame.init()
		self.size = size
		self.screen = pygame.display.set_mode(size)
		self.controller = None

	'''
	Draw the contents of the app on the screen.
	'''
	def draw(self):
		self.controller.draw(self.screen)

	'''
	Set the controller of this app. 

	@param Controller controller
	'''
	def setController(self, controller):
		self.controller = controller
		controller.app = self

	'''
	Execute a single step.
	'''
	def step(self):
		events = pygame.event.get()
		for event in events:
			self.triggerEvent(event)
		self.controller.step()
		self.draw()
		pygame.display.flip()

	'''
	Trigger an event.

	@param Event event
	'''
	def triggerEvent(self, event):
		if event.type == pygame.QUIT:
			sys.exit()
		else:
			self.controller.triggerEvent(event)