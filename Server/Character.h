#include <string>
#include "Animation.h"
#include <iostream> 
#include <iterator> 
#include <map>
class Character{
	std::string name;
	std::map<char, Animation*> map;
	std::string animationFolder;
	public:
		Character(std::string name, std::string animationFolder ){
			this -> animationFolder = animationFolder;
			this -> name = name;	
		}
	Animation* selectAnimation(char key){
		std::map<char, Animation*>::iterator it;
		it = map.find(key);
  			if (it == map.end()){
    			return NULL;
  			}
    		else{
    			return map.find(key)->second;
    		}
	}
	std::string getName(){return name;}
	void putAnimation(Animation *animation){map.insert(std::pair<char, Animation*>(animation->getKey(), animation));}
	int loadAnimationsFromMemory(){return 1;}
	int saveAnimationsToMemory(){return 1;}

	private:
	
};