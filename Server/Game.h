#include "Character.h" 
class Game{
	std::string name;
	std::map<std::string, Character*> map;
	std::string characterFolder;
	Character *currentCharacter;
	public:
		Game(std::string name, std::string characterFolder){
			this -> characterFolder = characterFolder;
			this -> name = name;	
		}
	int selectCharacter(std::string charName){
		std::map<std::string, Character*>::iterator it;
		it = map.find(charName);
  			if (it == map.end()){
    			return 1;
  			}
    		else{
    			currentCharacter = map.find(charName)->second;
    			return 0;
    		}
	}
	void putCharacter(Character *character){map.insert(std::pair<std::string, Character*>(character->getName(), character));}
	Character* getCurrentCharacter() {return currentCharacter;}
	int loadCharactersFromDisk(){return 1;}
	int saveCharactersToDisk(){return 1;}

	private:

};