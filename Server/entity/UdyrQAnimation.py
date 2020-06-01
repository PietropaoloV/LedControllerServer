from __future__ import division
import math
import time
import random
from Entity import Animation, Pixel,Frame

class UdyrAnimation(Animation):
	def __init__(self, key, duration, velocity, name, filePath, isCancellable, sizeX, sizeY, red, green, blue):
		Animation.__init__(self, key, duration, velocity, name, filePath, isCancellable, sizeX, sizeY)
		self.createAnimation(sizeX, sizeY, red, green, blue)
	def checkBoundary(self, pixelLocation, bound):
		if (pixelLocation < 0):
			return 0
		if (pixelLocation >= bound	):
			return bound - 1	
		return pixelLocation

	def	makeBox(self, middleX, middleY, step):
		perimeter = list()
		xLower = self.checkBoundary(middleX-step, self.sizeX)
		xUpper = self.checkBoundary(middleX+step, self.sizeX)
		yLower = self.checkBoundary(middleY-step, self.sizeY)
		yUpper = self.checkBoundary(middleY+step, self.sizeY)
		for x in range(xLower, xUpper):
			for y in range(yLower, yUpper):
				perimeter.append((x,y))
			pass
		return perimeter
					
	def createAnimation(self, sizeX, sizeY, red, green, blue):
		middleX = sizeX//2
		middleY = sizeY//2
		frameStepX = (self.duration//((max(sizeX,sizeY))))
		timeStep = 0
		#print(sizeX, sizeY,middleX, middleY, frameStepX, frameStepY)
		for x in range(self.duration):
			frame = Frame()
			if (x % frameStepX == 0):
				if (timeStep == 0):
						pixel = Pixel(red,  green,	blue, 100, middleX, middleY)
						frame.addPixel(pixel)
					
				else:
					perimeter = self.makeBox(middleX, middleY, timeStep)
					for i in range (len(perimeter)):
						pixelPos = perimeter[i]
						pixel = Pixel(red,  green,	blue, 100,  pixelPos[0]	, pixelPos[1])
						frame.addPixel(pixel)
			
				timeStep += 1

			self.addFrame(frame)