#include "key.h"
#include <string.h> 
class Message{
	Key *key; //Pressed Key
	std::string character; //Selected std::stringacter
	std::string game; //Selected Game
	short operationMode; //0 changeSpecs of board,1 Key press, 2 change std::stringacter, 3 change game

public:
	Message(Key *key, std::string character, std::string game, int operationMode){
		this -> key = key;
		this -> character = character;
		this -> game = game;
		this -> operationMode = operationMode;
	}
	Key * getKey(){return key;}
	std::string getCharacter(){return character;}
	std::string getGame(){return game;}
	int getOptMode(){return operationMode;}
};