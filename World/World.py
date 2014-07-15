import pygame
from Core.Controller import Controller

'''
@class World
@extends Controller
'''
class World(Controller):
	'''
	Constructor.
	'''
	def __init__(self):
		Controller.__init__(self)

	'''
	Add an Entity to this World.

	@param Entity entity
	'''
	def addEntity(self, entity):
		pass

	'''
	Remove an Entity from this World.

	@param Entity entity
	'''
	def removeEntity(self, entity):
		pass

	'''
	Execute a single step for this World.
	'''
	def onStep(self):
		pass