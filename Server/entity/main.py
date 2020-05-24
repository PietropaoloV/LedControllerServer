


import os
import time
import numpy
import socket as socket
import time
import sys
from Entity import Game
from Entity import Character
from Entity import Pixel
from Entity import LeagueFlashAnimation
from Entity import Key
from Entity import Message
# from rpi_ws281x import Color, PixelStrip, ws
LED_COUNT = 40         # Number of LED pixels.
LED_PIN = 18           # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000   # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10           # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255   # Set to 0 for darkest and 255 for brightest
LED_INVERT = False     # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0
# LED_STRIP = ws.SK6812_STRIP_RGBW
sizeX = 40;
sizeY = 1;
leds = numpy.full((sizeX, sizeY), Pixel(0, 0, 0, 100, 0, 0))

# strip = Adafruit_NeoPixel(
#         LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
# strip.begin()


def checkDimensions():
    return LED_COUNT != sizeX*sizeY



def initMatrix():
    for x in xrange(0, len(leds)):
        for y in xrange(0,  len(leds[x])):
            leds[x][y] = Pixel(0, 0, 0, 100, 0, 0)

def deserialize(bytes):
    messageArgs = bytes[0].split(",")
    return Message(Key(messageArgs[3],messageArgs[4].lower() == "true" ), messageArgs[2], messageArgs[1], messageArgs[0])


def printMatrix():
    for x in xrange(0, len(leds)):
        for y in xrange(0,  len(leds[x])):
            pixel = leds[x][y]
            red  = pixel.getRed() 
            blue = pixel.getBlue()
            green = pixel.getGreen() 

            print( red ,  green ,  blue ),
        print("\n")

def printUpdatePixel(currentPixel):
    xLoc = currentPixel.getXLoc()
    yLoc = currentPixel.getYLoc()
    red  = currentPixel.getRed() 
    blue = currentPixel.getBlue()
    green = currentPixel.getGreen()
    ledPixel = leds[yLoc][xLoc]
    ledPixel.setRed(red)
    ledPixel.setBlue(blue)
    ledPixel.setGreen(green)

def printUpdateScreen(currentFrame):
    for x in xrange(0, len(currentFrame.getPixels())):
        currentPixel = currentFrame.getPixels()[x]
        xLoc = currentPixel.getXLoc()
        yLoc = currentPixel.getYLoc()
        red  = currentPixel.getRed() 
        blue = currentPixel.getBlue()
        green = currentPixel.getGreen()
        #print(xLoc ,yLoc , red ,green ,blue, " "),
        printUpdatePixel(currentPixel)
    print("\n")
    printMatrix()


def UpdatePixel(currentPixel):
    red  = currentPixel.getRed() 
    blue = currentPixel.getBlue()
    green = currentPixel.getGreen()
    #strip.setPixelColor(currentPixel.getLinearLoc(), Color(red, green, blue))

def UpdateScreen(currentFrame):
    for x in xrange(0, len(currentFrame.getPixels())):
        currentPixel = currentFrame.getPixels()[x]
        UpdatePixel(currentPixel)

def createServer(ip, port):
# Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
    server_address = (ip, port)
    print >>sys.stderr, 'starting up on %s port %s' % server_address
    sock.bind(server_address)
    return sock

def listenToClient(sock):
    data = sock.recvfrom(4)
    dataLength = socket.htonl(len(data))
    data = sock.recvfrom(dataLength)
    print(data)
    return data

def main():
    if (checkDimensions()):
        exit(1)

    initMatrix()
    socket = createServer("127.0.0.1", 10000)
    message = None
    while (message == None):
        data = listenToClient(socket)
        message = deserialize(data)
    key = message.getKey().getKeyChar()
    leagueFlashAnimation = LeagueFlashAnimation(Key('q', bool(0) ), 240, 40, "LeagueFlashAnimation" , "test.csv", bool(1), sizeX, sizeY);
    league = Game("League", "./League" );
    sion = Character("Sion", "./League/Sion");
    sion.putAnimation(leagueFlashAnimation);
    league.putCharacter(sion);
    i = league.selectCharacter("Sion");
    if (i == 1):
        animation = league.getCurrentCharacter().selectAnimation(key);
        if (animation != None):
            listOfFrames = animation.keyPressed();
            for x in xrange(0,len(listOfFrames)):
                currentFrame = listOfFrames[x];
                UpdateScreen(currentFrame);  
                
if __name__ == "__main__":
    main()