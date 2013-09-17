'''
@class Controller
@abstract
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
	def onDraw(self, screen):
		pass
		
	'''
	Execute a single step.
	'''
	def onStep(self):
		pass

	'''
	Trigger an event.

	@param Event event
	'''
	def onEvent(self, event):
		pass