import pygame
from controller import Controller

'''
@class World
@extends Controller
'''
class World(Controller):
	'''
	Constructor.

	@var Entity[] entities
	'''
	def __init__(self):
		Controller.__init__(self)
		self.entities = []

	'''
	Add an entity to this world.

	@param Entity entity
	'''
	def addEntity(self, entity):
		self.entities.append(entity)
		entity.world = self

	'''
	Execute a single step for this world.
	'''
	def step(self):
		for entity in self.entities:
			entity.step()