


import os
import time
import numpy
import socket as socket
import time
import sys
from Entity import Game
from Entity import Character
from Entity import Pixel
from FlashAnimation import LeagueFlashAnimation
from Entity import Key
from Entity import Message
from colr import color

# from rpi_ws281x import Color, PixelStrip, ws
LED_COUNT = 121    # Number of LED pixels.
LED_PIN = 18           # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000   # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10           # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255   # Set to 0 for darkest and 255 for brightest
LED_INVERT = False     # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0
FPS = 600
# LED_STRIP = ws.SK6812_STRIP_RGBW
sizeX = 11;
sizeY = 11;
leds = numpy.full((sizeX, sizeY), Pixel(0, 0, 0, 100, 0, 0))
# strip = Adafruit_NeoPixel(
#         LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
# strip.begin()
def memory_usage_psutil():
    import psutil
    return psutil.virtual_memory()

def checkDimensions():
    return LED_COUNT != sizeX*sizeY

def clearMatrix():
    for x in range(0, len(leds)):
        for y in range(0,  len(leds[x])):
            leds[x][y] = Pixel(0, 0, 0, 100, 0, 0)

def deserialize(byteMessage):
    stringMessage = byteMessage[0].decode("utf-8")
    messageArgs = stringMessage.split(",")
    return Message(Key(messageArgs[3],messageArgs[4].lower() == "true" ), messageArgs[2], messageArgs[1], messageArgs[0])


def printMatrix():
    for x in range(0, len(leds)):
        for y in range(0,  len(leds[x])):
            pixel = leds[x][y]
            red  = pixel.getRed() 
            blue = pixel.getBlue()
            green = pixel.getGreen() 
            string = "(" + str(red) + "," + str(green) + "," + str(blue) +")"
            print(color("         ", fore=(0 , 0, 0), back=(red , green, blue)),end = ' , ')
        print("\n")

def border(check , bound):
    if (check < 0):
        return 0;
    if (check > bound):
        return bound-1
    return check

def printUpdatePixel(currentPixel):
    xLoc = currentPixel.getXLoc()
    yLoc = currentPixel.getYLoc()
    red  = currentPixel.getRed() 
    blue = currentPixel.getBlue()
    green = currentPixel.getGreen()
    xLoc = border(xLoc, len(leds))
    yLoc = border(yLoc, len(leds[0]))
    if(xLoc >= len(leds)):
        xLoc = len(leds) - 1
    if(yLoc >= len(leds[0])):
        yLoc = len(leds[0]) -1 

    if(xLoc < 0):
        xLoc = 0
    if(yLoc < 0):
        yLoc = 0


    ledPixel = leds[xLoc][yLoc]
    ledPixel.setRed(red)
    ledPixel.setBlue(blue)
    ledPixel.setGreen(green)


def printUpdateScreen(currentFrame):
    for x in range(0, len(currentFrame.getPixels())):
        currentPixel = currentFrame.getPixels()[x]
        xLoc = currentPixel.getXLoc()
        yLoc = currentPixel.getYLoc()
        red  = currentPixel.getRed() 
        blue = currentPixel.getBlue()
        green = currentPixel.getGreen()
        #print(xLoc ,yLoc , red ,green ,blue, " "),
        printUpdatePixel(currentPixel)
    printMatrix()


def UpdatePixel(currentPixel):
    red  = currentPixel.getRed() 
    blue = currentPixel.getBlue()
    green = currentPixel.getGreen()
    #strip.setPixelColor(currentPixel.getLinearLoc(), Color(red, green, blue))

def UpdateScreen(currentFrame):
    for x in range(0, len(currentFrame.getPixels())):
        currentPixel = currentFrame.getPixels()[x]
        UpdatePixel(currentPixel)

def createServer(ip, port):
# Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
    server_address = (ip, port)
    print (sys.stderr, 'starting up on %s port %s' % server_address)
    sock.bind(server_address)
    return sock

def listenToClient(sock):
    data = sock.recvfrom(4)
    dataLength = socket.htonl(len(data))
    data = sock.recvfrom(dataLength)
    print(data)
    return data

def main():
    clearMatrix()
    if (checkDimensions()):
        exit(1)
    leagueFlashAnimation = LeagueFlashAnimation(Key('q', bool(0) ), 30 , FPS, "LeagueFlashAnimation" , "test.csv", bool(1), sizeX, sizeY);
    league = Game("League", "./League" );
    sion = Character("Sion", "./League/Sion");
    sion.putAnimation(leagueFlashAnimation);
    league.putCharacter(sion);
    socket = createServer("127.0.0.1", 10000)
    i = league.selectCharacter("Sion");
    while(True):
        clearMatrix()
        message = None
        while (message == None):
            data = listenToClient(socket)
            message = deserialize(data)
        key = message.getKey().getKeyChar()
        
        
        if (i == 1):
            animation = league.getCurrentCharacter().selectAnimation(key);
            if (animation != None):
                listOfFrames = animation.keyPressed();
                for x in range(0,len(listOfFrames)):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    currentFrame = listOfFrames[x];
                    #print("Current Frame", x)
                    printUpdateScreen(currentFrame);  
                print(memory_usage_psutil())
if __name__ == "__main__":
    main()