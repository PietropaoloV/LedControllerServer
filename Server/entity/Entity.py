from colr import color
import os
class Pixel:
	def __init__(self, red, green, blue, brightness, xLoc, yLoc):
		self.red = red;
		self.blue = blue;
		self.green = green;
		self.brightness = brightness;
		self.xLoc = xLoc;
		self.yLoc = yLoc;

	def getRed(self):
		return self.red
	def getBlue(self):
		return self.blue
	def  getGreen(self):
		return self.green
	def  getBrightness(self):
		return self.brightness
	def  getXLoc(self):
		return self.xLoc
	def  getYLoc(self):
		return self.yLoc

	def getLinearLoc(self):
		return (self.yLoc * 10) + self.xLoc

	def setXloc(self, xloc):
		self.xLoc = xloc

	def setYloc(self, yloc):
		self.yLoc = yloc

	def setRed(self, red):
		self.red = red

	def setBlue(self, blue):
		self.blue = blue

	def setGreen(self, green):
		self.green = green

	def setBrightness(self, brightness):
		self.brightness = brightness
  
class Frame:

	def __init__(self):
		self.pixelList = []
		pass

	def getSize(self):
		return len(self.pixelList)

	def getPixels(self):
		return self.pixelList

	def addPixel(self, pixel):
		self.pixelList.append(pixel)

class Animation:
	
	def __init__(self, key, duration, velocity, name, filePath, isCancellable, sizeX, sizeY):
		self.name = name
		self.isCancellable = isCancellable
		self.filePath = filePath
		self.key = key
		self.duration = duration
		self.velocity = velocity
		self.sizeY = sizeY
		self.sizeX = sizeX
		self.frames = []

	def getKey(self):
		return self.key

	def getName(self):
		return self.name

	def frameSize(self):
		return len(self.frames)

	def isCancellable(self):
		return self.isCancellable

	def keyPressed(self):
		return self.frames

	def addFrame(self, frame):
		self.frames.append(frame)

	def createAnimation(self, sizeX, sizeY):
		raise NotImplementedError()

	def __loadFramesFromDisk():
		return 1

	def __saveFramesToDisk():
		return 1

class Character:
	

	def __init__(self, name, animationFolder):
		self.name = name
		self.animationFolder = animationFolder
		self.mapOfAni = dict()

	def selectAnimation(self, key):
		return self.mapOfAni.get(key)

	def getName(self):
		return self.name

	def putAnimation(self, animation):
		animationName = animation.getKey().getKeyChar();
		self.mapOfAni[animationName] = animation

	def loadAnimationsFromMemory():
		return 1

	def saveAnimationsToMemory():
		return 1


class Game:
	def __init__(self, name, characterFolder):
		self.name = name
		self.charcterFolder = characterFolder
		self.characterMap = dict()
		self.currentCharacter = None

	def selectCharacter(self, charName):
		self.currentCharacter = self.characterMap.get(charName)
		if self.currentCharacter != None:
			return 1
		else:
			return -1

	def putCharacter(self, character):
		characterName = character.getName()
		self.characterMap[characterName] = character

	def getCurrentCharacter(self):
		return self.currentCharacter

	def loadCharactersFromDisk():
		return 1
		
	def saveCharactersToDisk():
		return 1 

class Key:
	def __init__(self, key, isDown):
		self.key = key
		self.isDown = isDown

	def getKeyChar(self):
		return self.key

	def isPressed(self):
		return self.isDown


class Message:
	def __init__(self, key, character, game, operationMode):
		self.key = key;
		self.character = character;
		self.game = game;
		self.operationMode = operationMode;
	
	def getKey(self):
		return self.key
	def getCharacterName(self):
		return self.character
	def getGameName(self):
		return self.game
	def getOptMode(self):
		return self.operationMode

class LedMatrix:
	def __init__(self, sizeX, sizeY):
		self.sizeX = sizeX
		self.sizeY = sizeY
		self.matrix = []
		for x in range(0, sizeX):
			yList = []
			for y in range(0,  sizeY):
				yList.append(Pixel(0, 0, 0, 100, 0, 0))
			self.matrix.append(yList)

	def getMatrix(self):
		return self.matrix

	def getSizeX(self):
		return self.sizeX

	def getSizeY(self):
		return self.sizeY

	def printMatrix(self):
		for x in range(0, len(self.matrix)):
			for y in range(0,  len(self.matrix[x])):
				pixel = self.matrix[x][y]
				red  = pixel.getRed() 
				blue = pixel.getBlue()
				green = pixel.getGreen() 
				string = "(" + str(red) + "," + str(green) + "," + str(blue) +")"
				print(color("         ", fore=(0 , 0, 0), back=(red , green, blue)),end = ' , ')
			print("\n")
		os.system('cls' if os.name == 'nt' else 'clear')
	def playFrame(self, currentFrame, print = 0):
		for x in range(0, len(currentFrame.getPixels())):
			currentPixel = currentFrame.getPixels()[x]
			self.updatePixel(currentPixel)
		if (print == 1):
			self.printMatrix()
	

	def border(self, check , bound):
		if (check < 0):
			return 0;
		if (check > bound):
			return bound-1
		return check

	def updatePixel(self, currentPixel):
		xLoc = currentPixel.getXLoc()
		yLoc = currentPixel.getYLoc()
		red  = currentPixel.getRed() 
		blue = currentPixel.getBlue()
		green = currentPixel.getGreen()
		xLoc = self.border(xLoc, len(self.matrix))
		yLoc = self.border(yLoc, len(self.matrix[0]))
		ledPixel = self.matrix[xLoc][yLoc]
		ledPixel.setRed(red)
		ledPixel.setBlue(blue)
		ledPixel.setGreen(green)
		
	def clearMatrix(self):
		for x in range(0, len(self.matrix)):
			for y in range(0,  len(self.matrix[x])):
				ledPixel = self.matrix[x][y]
				ledPixel.setRed(0)
				ledPixel.setBlue(0)
				ledPixel.setGreen(0)

