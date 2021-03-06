'''
@class Alarm
'''
class Alarm:
	'''
	Constructor.

	@param int interval number of steps before this Alarm triggers
	@param string event the method to call when this Alarm triggers
	@param boolean repeat

	@var int interval
	@var int ticks
	@var Entity entity
	@var string event
	@var boolean repeat
	@var boolean ticking
	'''
	def __init__(self, interval, event, repeat=False):
		self.interval = interval
		self.ticks = -1
		self.entity = None
		self.event = event
		self.repeat = repeat
		self.ticking = False

	'''
	Execute a single step.
	'''
	def onStep(self):
		if self.ticking:
			if self.ticks > 0:
				self.ticks -= 1
			elif self.ticks == 0:
				getattr(self.entity, method)()
				if self.repeat:
					self.rewind()
				else:
					self.stop()

	'''
	Rewind this Alarm.
	'''
	def rewind(self):
		self.ticks = self.interval

	'''
	Start this Alarm.
	'''
	def start(self):
		self.ticking = True
		
	'''
	Stop this Alarm.
	'''
	def stop(self):
		self.ticking = False