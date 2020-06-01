// Client side C/C++ program to demonstrate Socket programming 
#include <chrono>
#include <thread>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
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
#include <sys/socket.h> 
#include <arpa/inet.h> 
#include <unistd.h> 
#include <string.h> 
#include <sstream> 
#include "Message.h"
#define PORT 10001
   
std::string serialize(Message *m);
int init();
std::string boolToString(bool b)
{
  return b ? "true" : "false";
}
int main(int argc, char const *argv[]) 
{ 
    int socket = init();
    if (socket == -1){
        exit(EXIT_FAILURE);
    }

    //send(sock ,cstr , strlen(cstr) , 0 );
    
    Key *key = new Key('q',true); 
    Message * m = new Message(key, "Test Character", "Test Game", 0 );
    std::string dataToSend = serialize(m);
    std::cout<< dataToSend << std::endl;
    uint32_t dataLength = htonl(sizeof(dataToSend)); // Ensure network byte order 
                                                // when sending the data length
    send(socket, &dataLength ,sizeof(uint32_t ) , 0); // Send the data length
    send(socket,dataToSend.c_str(),dataToSend.size(), 0); 
    return 0; 
} 

std::string serialize(Message *m){
	Key *key = m->getKey();

    char keyPressed = key->getKeyChar();
    std::string isPressed = boolToString(key->isPressed());
    std::string character = m->getCharacter();
    std::string game = m->getGame();
    

    std::string optModeString = std::to_string(m->getOptMode());
    std::stringstream outputStringStream;

    outputStringStream <<optModeString <<  "," << game << "," << character << "," << keyPressed << "," << isPressed;
    return outputStringStream.str();   
}


//To-do Configure IP;
int init(){
  int sock = 0, valread; 
    struct sockaddr_in serv_addr;
    
    sock = socket(AF_INET, SOCK_DGRAM, 0);
    serv_addr.sin_addr.s_addr = inet_addr("192.168.1.17"); 
    serv_addr.sin_port = htons(PORT); 
    serv_addr.sin_family = AF_INET; 
   
    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) 
    { 
        printf("\nConnection Failed \n"); 
        return -1; 
    }
    return sock; 
  }