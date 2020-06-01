from __future__ import division
import math
import time
import random
from Entity import Animation, Pixel,Frame

class LeagueSmiteAnimation(Animation):
	def __init__(self, key, duration, velocity, name, filePath, isCancellable, sizeX, sizeY):
		Animation.__init__(self, key, duration, velocity, name, filePath, isCancellable, sizeX, sizeY)
		self.createAnimation(sizeX, sizeY)
	def leftRightMove(self, pixelLocation):
		side = random.randint(2,3);
		if (side % 2 == 0):
				pixelLocation +=1
		else:
				pixelLocation -=1

		if (pixelLocation < 0):
				pixelLocation += 2

		if (pixelLocation >= self.sizeY):
				pixelLocation -= 2
		return pixelLocation

	def createAnimation(self, sizeX, sizeY):
		random.seed(time.time())
		frameStepX = (self.duration//((sizeX)))
		bolts = list()
		if(sizeY > 0):
			for x in range(sizeY//5):
					bolts.append(random.randint(0,sizeY))
		else:
			return
		timeStep = 0
		#print(sizeX, sizeY,middleX, middleY, frameStepX, frameStepY)
		for x in range(self.duration):
			frame = Frame()
			if (x % frameStepX == 0):
				if (timeStep == 0):
					for pos in bolts:
							pixel = Pixel(0,0, 255, 100, timeStep, pos)
							frame.addPixel(pixel)
					
				else:
					for x in range(len(bolts)):
							bolts[x] = self.leftRightMove(bolts[x])
							pixel = Pixel(0,0, 255, 100,  timeStep	, bolts[x])
							frame.addPixel(pixel)
			
				timeStep += 1

			self.addFrame(frame)