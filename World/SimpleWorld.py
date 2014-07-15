from World import World

class SimpleWorld(World):
	'''
	Create a new SimpleWorld instance.

	@var Entity[] entities
	'''
	def __init__(self):
		World.__init__(self)
		self.entities = []

	def addEntity(self, entity):
		self.entities.append(entity)
		entity.world = self

	def removeEntity(self, entity):
		for i in range(len(self.entities)):
			if self.entities[i] == entity:
				self.entities[i].world = None
				del self.entities[i]
				break

	def onStep(self):
		for entity in self.entities:
			entity.onStep()