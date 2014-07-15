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
	@var Keyboard keyboard
	'''
	def __init__(self, size):
		pygame.init()
		self.size = size
		self.screen = pygame.display.set_mode(size)
		self.controller = None

	'''
	Draw the contents of the app on the screen.
	'''
	def onDraw(self):
		self.controller.onDraw(self.screen)

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
	def onStep(self):
		events = pygame.event.get()
		for event in events:
			self.onEvent(event)
		self.controller.onStep()
		self.onDraw()
		pygame.display.flip()

	'''
	Trigger an event.

	@param Event event
	'''
	def onEvent(self, event):
		if event.type == pygame.QUIT:
			sys.exit()
		else:
			self.controller.onEvent(event)