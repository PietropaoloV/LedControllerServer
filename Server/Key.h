class Key{
	char key; //key pressed
	bool isDown; //Is the key pushed down (true) or let go (false);

public:
	Key(char key, bool isDown){
		this -> key = key;
		this -> isDown = isDown;
	}

	char getKeyChar(){return key;}
	bool isPressed(){return isDown;}

};
