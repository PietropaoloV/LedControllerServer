#include <iostream>
#include <string.h>
#include <chrono>
#include <thread>
#include "Game.h"
#include "./AnimationsRaw/LeagueFlashAnimation.h"

Pixel *pixel = new Pixel (0, 0, 0, 100, 0, 0);
int sizeY = 7;
int sizeX = 7;
std::vector<Pixel*> xVec(sizeX, pixel);
std::vector<std::vector<Pixel*>> leds(sizeY, xVec);
void printUpdateScreen(Frame *currentFrame);
void printUpdatePixel(Pixel *currentPixel);
void printMatrix();
void initMatrix();

int main() {
	initMatrix();
	LeagueFlashAnimation *lFa = new LeagueFlashAnimation('q', "LeagueFlashAnimation" , "test.csv", true, sizeX, sizeY, 240, 40);
	Game *league = new Game("League", "./League" );
	Character *sion = new Character("Sion", "./League/Sion");
	sion->putAnimation(lFa);
	league->putCharacter(sion);
	int i = league->selectCharacter("Sion");
	
	while(true){
	char c;
	std::cin>>c;

	if (i == 0){
		Animation* animation = league->getCurrentCharacter()->selectAnimation(c);

		if (animation){
			std::vector<Frame*> listOfFrames = animation->keyPressed();
 			for(unsigned int i=0; i < listOfFrames.size(); i++) {
 				system("clear");
 				Frame *currentFrame = listOfFrames[i];
 				std::cout<< "Frame " << i << ":" << std::endl;
 				printUpdateScreen(currentFrame);
 				std::this_thread::sleep_for(std::chrono::milliseconds(250));
				std::cout << std::endl;
			}
		}
	}

}
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
// int SERVER_PORT = 8876;
	// int server_socket = socket(AF_INET, SOCK_STREAM, 0);

	// if (server_socket == 0) {
	// 	printf("Error creating socket on server side faild\n");
	// 	exit(EXIT_FAILURE);
	// }

	// // socket address used for the server
	// struct sockaddr_in server_address;
	// memset(&server_address, 0, sizeof(server_address));
	// server_address.sin_family = AF_INET;
	// server_address.sin_port = htons(SERVER_PORT);
	// server_address.sin_addr.s_addr = htonl(INADDR_ANY);

	// // Binding
	// if (bind(server_socket, (struct sockaddr*) server_address,
	// 		sizeof(server_address)) < 0) {
	// 	printf("Failed to bind socket\n");
	// 	exit(EXIT_FAILURE);
	// }

	// // Listening waiting time 16
	// if (listen(server_socket, 16) < 0) {
	// 	printf("Listening to socket failed\n");
	// 	exit(EXIT_FAILURE);
	// }

	// int client_socket;
	// client_socket = accept(server_socket, NULL, NULL);
	// if (client_socket == -1) {
	// 	printf("Problem creating connection to socket %s\n", strerror(errno));
	// 	exit(EXIT_FAILURE);
	// }

	// int exit = 0;
	// char buffer[8];
	// while (strcmp(exit == 0)) {
	// 	int readvalue = recv(client_socket, buffer, 7)
	// 	buffer[7] = '/0';
	// }
		


	// 	close( client_socket);
	// 	close( server_socket);
	// 	return 0;