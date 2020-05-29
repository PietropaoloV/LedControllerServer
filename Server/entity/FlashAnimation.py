from __future__ import division
import math
from Entity import Animation, Pixel,Frame

class LeagueFlashAnimation(Animation):
	def __init__(self, key, duration, velocity, name, filePath, isCancellable, sizeX, sizeY):
		Animation.__init__(self, key, duration, velocity, name, filePath, isCancellable, sizeX, sizeY)
		self.createAnimation(sizeX, sizeY)
	def invertIfDecimalFloor(self, number):
		if(number < 1):
			number = 1/number
		return int(math.floor(number))
	def invertIfDecimalCeil(self, number):
		if(number < 1):
			number = 1/number
		return int(math.ceil(number))
	def createAnimation(self, sizeX, sizeY):
		evenConstY = 0
		evenConstX = 0
		if (sizeX % 2 == 0):
			evenConstX = 1
		if (sizeY % 2 == 0):
			evenConstY = 1
		middleX = -(-sizeX//2)
		middleY = -(-sizeY//2)
		frameStepX = -(-self.duration//((middleX + evenConstX)))
		frameStepY = -(-self.duration//((middleY + evenConstY)))
		midDown = middleY-1
		midUp = middleY-1
		firstTimeStep = 0
		print(sizeX, sizeY,middleX, middleY, frameStepX, frameStepY)
		for x in range(self.duration):
			frame = Frame()
			if (x % frameStepY == 0):
				if (firstTimeStep == 0):
					for x in range(sizeX):
						rowMid = Pixel(255,255, 0, 100,  x, middleY-1)
						frame.addPixel(rowMid)
				else:
						midUp+=1
						midDown-=1
						if(midUp > sizeY):
							midUp = sizeY -1
						if(midDown < 0):
							midDown = 0
						for x in range(sizeX):
							rowUp = Pixel(255,255,0,100,  x, midUp)
							rowDown = Pixel(255,255,0,100, x, midDown)
							frame.addPixel(rowUp)
							frame.addPixel(rowDown)
				firstTimeStep = 1

			self.addFrame(frame)