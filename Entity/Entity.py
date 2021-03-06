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
	@var Alarm[] alarms
	'''
	def __init__(self, (x, y), sprite):
		self.x = x
		self.y = y
		self.sprite = sprite
		self.alarms = []

	'''
	Add an Alarm.

	@param Alarm alarm
	@param boolean activate
	'''
	def addAlarm(self, alarm, activate=True):
		self.alarms.append(alarm)
		alarm.entity = self
		if activate:
			alarm.rewind()
			alarm.start()

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
	Receive an Event.

	@param Event event
	'''
	def onEvent(self, event):
		pass

	'''
	Set the Sprite of this Entity.

	@param Sprite sprite
	'''
	def setSprite(self, sprite):
		self.sprite = sprite

	'''
	Execute a single step for each Alarm.
	'''
	def onAlarmsStep(self):
		for alarm in self.alarms:
			alarm.onStep()

	'''
	Execute a single step for this Entity.
	'''
	def onStep(self):
		self.onAlarmsStep()
		self.sprite.onStep()