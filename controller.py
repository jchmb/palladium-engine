'''
@class Controller
'''
class Controller:
	'''
	Constructor.

	@var App app
	'''
	def __init__(self):
		self.app = None

	'''
	Draw the contents of this controller on the screen.

	@param Surface screen
	'''
	def draw(self, screen):
		pass
		
	'''
	Execute a single step.
	'''
	def step(self):
		pass

	'''
	Trigger an event.

	@param Event event
	'''
	def triggerEvent(self, event):
		pass