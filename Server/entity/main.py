import time
import numpy
import socket as socket
import time
import sys
import MessageSerialization as ms
from Entity import Game
from Entity import LedMatrix
from Entity import Character
from Entity import Pixel
from FlashAnimation import LeagueFlashAnimation
from SmiteAnimation import LeagueSmiteAnimation
from UdyrAnimation import UdyrAnimation 
from Entity import Key
from Entity import Message


# from rpi_ws281x import Color, PixelStrip, ws
LED_COUNT = 250    # Number of LED pixels.
LED_PIN = 18           # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000   # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10           # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255   # Set to 0 for darkest and 255 for brightest
LED_INVERT = False     # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0
FPS = 600
# LED_STRIP = ws.SK6812_STRIP_RGBW
sizeX = 10;
sizeY = 25;
leds = LedMatrix(sizeX, sizeY)

def memory_usage_psutil():
    import psutil
    return psutil.virtual_memory()

def checkDimensions():
    return LED_COUNT != sizeX * sizeY

def createServer(ip, port):
# Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
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
    leds.clearMatrix()
    if (checkDimensions()):
        exit(1)
    leagueFlashAnimation = LeagueFlashAnimation(Key('f', bool(0) ), 30 , FPS, "LeagueFlashAnimation" , "test.csv", bool(1), sizeX, sizeY);
    leagueSmiteAnimation = LeagueSmiteAnimation(Key('d', bool(0) ), 15 , FPS, "LeagueSmiteAnimation " , "test.csv", bool(1), sizeX, sizeY);
    udyrQAnimation = UdyrAnimation(Key('q', bool(0) ), 15 , FPS, "Tiger" , "test.csv", bool(1), sizeX, sizeY,255,0,0,);
    udyrWAnimation = UdyrAnimation(Key('w', bool(0) ), 15 , FPS, "Turtle" , "test.csv", bool(1), sizeX, sizeY,0,255,0);
    udyrEAnimation = UdyrAnimation(Key('e', bool(0) ), 15 , FPS, "Bear" , "test.csv", bool(1), sizeX, sizeY,0,0,255);
    udyrRAnimation = UdyrAnimation(Key('r', bool(0) ), 15 , FPS, "Pheonix" , "test.csv", bool(1), sizeX, sizeY,255,0,255);
    league = Game("League", "./League" );
    udyr = Character("udyr", "./League/Udyr");
    udyr.putAnimation(leagueFlashAnimation);
    udyr.putAnimation(leagueSmiteAnimation);
    udyr.putAnimation(udyrQAnimation);
    udyr.putAnimation(udyrWAnimation);
    udyr.putAnimation(udyrEAnimation);
    udyr.putAnimation(udyrRAnimation);
    league.putCharacter(udyr);
    socket = createServer("127.0.0.1", 10001)
    i = league.selectCharacter("udyr");
    while(True):
        leds.clearMatrix()
        message = None
        ## Eventual Threading
        while (message == None):
            data = listenToClient(socket)
            message = ms.deserialize(data)
        print(message)

        operationBit = int(message.getOptMode())
        game = message.getGameName()
        character = message.getCharacterName()
        key = message.getKey().getKeyChar()
        if (operationBit == 0):
            if (i == 1):
                animation = league.getCurrentCharacter().selectAnimation(key);
                if (animation != None):
                    listOfFrames = animation.keyPressed()
                    for x in range(0,len(listOfFrames)) :
                        currentFrame = listOfFrames[x];
                        print("Current Frame", x)
                        leds.playFrame(currentFrame, 1) 
                    print(memory_usage_psutil())
        # if (operationBit == 1):
        # if (operationBit == 2):
        # if (operationBit == 3):
        
            
       
if __name__ == "__main__":
    main()