#include <chrono>
#include <thread>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <dirent.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <unistd.h>
#include <errno.h>
#include <pthread.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <stdbool.h>
#include "Game.h"
Pixel *pixel = new Pixel (0, 0, 0, 100, 0, 0);
int sizeY = 7;
int sizeX = 7;
std::vector<Pixel*> xVec(sizeX, pixel);
std::vector<std::vector<Pixel*>> leds(sizeY, xVec);
void printUpdateScreen(Frame *currentFrame);
void printUpdatePixel(Pixel *currentPixel);
void printMatrix();
void initMatrix();

int * initServer();
void closeServer(int server_socket, int client_socket);
Key* deserialize(char* bytes);
int main(){
	uint32_t dataLength;
	std::string receivedString;                       
	std::vector<uint8_t> rcvBuf; 
	int* sockets = initServer();
	int client_socket = sockets[0];
	initMatrix();
	LeagueFlashAnimation *lFa = new LeagueFlashAnimation(new Key('q', false), "LeagueFlashAnimation" , "test.csv", true, sizeX, sizeY, 240, 40);
	Game *league = new Game("League", "./League" );
	Character *sion = new Character("Sion", "./League/Sion");
	sion->putAnimation(lFa);
	league->putCharacter(sion);
	int i = league->selectCharacter("Sion");
	
	

		recv(client_socket,&dataLength,sizeof(uint32_t),0); // Receive the message length
		dataLength = ntohl(dataLength ); // Ensure host system byte order
		std::cout<<dataLength;
		   
		rcvBuf.resize(dataLength,0x00); // with the necessary size

		recv(client_socket,&(rcvBuf[0]),dataLength,0); // Receive the string data

		std::cout<<&rcvBuf[0];
		// std::cout<<receivedString;
		// if (key){
		// 	std::cout << buffer;
		// 	std::cout << key->getKeyChar();
	

		// 	if (i == 0){
		// 		Animation* animation = league->getCurrentCharacter()->selectAnimation(key);

		// 		if (animation){
		// 			std::vector<Frame*> listOfFrames = animation->keyPressed();
 	// 				for(unsigned int i=0; i < listOfFrames.size(); i++) {
 	// 					system("clear");
 	// 					Frame *currentFrame = listOfFrames[i];
 	// 					std::cout<< "Frame " << i << ":" << std::endl;
 	// 					printUpdateScreen(currentFrame);
 	// 					//std::this_thread::sleep_for(std::chrono::milliseconds());
		// 				std::cout << std::endl;
		// 			}
		// 		}
		// 		initMatrix();
		// 	}
		// }
		//  memset(buffer, 0, sizeof buffer);


	closeServer(sockets[1], sockets[0]);
		return 0;
}
Key* deserialize(char* bytes){
	Key *key = NULL;
	std::cout<<bytes;
	if (sizeof(bytes)/sizeof(bytes[0]) >= 3){
		if (*bytes == '@'){
			key = new Key(*(bytes+1),(*(bytes+2) == '0'));
		}
	}
	return key;
}
void closeServer(int server_socket, int client_socket){
	close( client_socket);
	close( server_socket);
}
int * initServer(){
	int * sockets = (int*) malloc(2*sizeof(int));
	int SERVER_PORT = 8876;
	int server_socket = socket(AF_INET, SOCK_STREAM, 0);

	if (server_socket == 0) {
		printf("Error creating socket on server side failed\n");
		exit(EXIT_FAILURE);
	}

	// socket address used for the server
	struct sockaddr_in address;
	memset(&address, 0, sizeof(address));
	address.sin_family = AF_INET; 
    address.sin_addr.s_addr = INADDR_ANY; 
    address.sin_port = htons( SERVER_PORT ); 
	// Binding
	if (bind(server_socket, (struct sockaddr *)&address,
			sizeof(address)) < 0) {
		printf("Failed to bind socket\n");
		exit(EXIT_FAILURE);
	}
	// Listening waiting time 16
	if (listen(server_socket, 16) < 0) {
		printf("Listening to socket failed\n");
		exit(EXIT_FAILURE);
	}

	int client_socket;
	client_socket = accept(server_socket, NULL, NULL);
	if (client_socket == -1) {
		printf("Problem creating connection to socket %s\n", strerror(errno));
		exit(EXIT_FAILURE);
	}
	sockets[0] = client_socket;
	sockets[1] = server_socket;
	return sockets;
}

void printMatrix(){
	for(unsigned int i=0; i < leds.size(); i++) {
      for (unsigned int j=0; j < leds[i].size(); j++){
        Pixel *currentPixel = leds[i][j] ;  
        int red  = currentPixel->getRed(); 
 		int blue = currentPixel->getBlue();
 		int green = currentPixel->getGreen(); 
        std::cout << "(" << red << "," << green << "," << blue <<") "; 
   }
  std::cout << std::endl;
}
}
void initMatrix(){
	for(unsigned int i=0; i < leds.size(); i++) {
      for (unsigned int j=0; j < leds[i].size(); j++){
         leds[i][j] = new Pixel (0, 0, 0, 100, 0, 0);
     }    
   }
}
void printUpdateScreen(Frame *currentFrame){
	for(unsigned int j=0; j < currentFrame->getPixels().size(); j++) {
 		Pixel *currentPixel = currentFrame->getPixels()[j];
 		int xLoc = currentPixel->getXLoc();
 		int yLoc = currentPixel->getYLoc();
 		int red  = currentPixel->getRed(); 
 		int blue = currentPixel->getBlue();
 		int green = currentPixel->getGreen();
 		std::cout << xLoc << ",";
 		std::cout << yLoc << ",";
 		std::cout << red  << ",";
 		std::cout << green  << ",";
 		std::cout << blue;
 		std::cout << std::endl;
 		printUpdatePixel(currentPixel);

	}
	for(unsigned int i=0; i < leds.size(); i++) {
      for (unsigned int j=0; j < leds[i].size(); j++){
        Pixel *currentPixel = leds[i][j] ;  
        int red  = currentPixel->getRed(); 
 		int blue = currentPixel->getBlue();
 		int green = currentPixel->getGreen(); 
        std::cout << "(" << red << "," << green << "," << blue <<") "; 
   }
   std::cout << std::endl;
}
}
void printUpdatePixel(Pixel *currentPixel){
 		int xLoc = currentPixel->getXLoc();
 		int yLoc = currentPixel->getYLoc();
 		int red  = currentPixel->getRed(); 
 		int blue = currentPixel->getBlue();
 		int green = currentPixel->getGreen();
 		Pixel *ledPixel = leds[yLoc][xLoc];
		ledPixel->setRed(red);
		ledPixel->setBlue(blue);
		ledPixel->setGreen(green);
}