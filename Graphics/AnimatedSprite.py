from SurfaceSprite import SurfaceSprite

'''
@class AnimatedSprite
@extends Surface
'''
class AnimatedSprite(SurfaceSprite):
	'''
	Constructor.

	@param Surface[] surfaces
	@param float surfaceIndex

	@var Surface[] surfaces
	@var float surfaceIndex
	@var float surfaceSpeed
	'''
	def __init__(self, surfaces, surfaceIndex=0):
		if len(surfaces) > (int(surfaceIndex) + 1):
			surface = surfaces[int(surfaceIndex)]
		else:
			surface = None
		SpriteResource.__init__(self, surface)
		self.surfaces = surfaces
		self.surfaceIndex = surfaceIndex
		self.surfaceSpeed = 0.0

	'''
	Reset this AnimatedSprite.
	'''
	def reset(self):
		self.surfaceIndex = 0.0

	'''
	Execute a single step.
	'''
	def onStep(self):
		self.surfaceIndex += self.surfaceSpeed
		if self.surfaceIndex >= len(self.surfaces):
			self.surfaceIndex -= len(self.surfaces)
		self.surface = self.surfaces[int(self.surfaceIndex)]

	'''
	Set the animation speed.

	@param float speed
	'''
	def setAnimationSpeed(self, speed):
		self.surfaceSpeed = speed

		
	'''
	Stop the animation.
	'''
	def stopAnimation(self):
		self.surfaceSpeed = 0.0