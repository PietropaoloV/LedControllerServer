
class LeagueFlashAnimation: public Animation{
public:
  typedef Animation super;
  LeagueFlashAnimation(Key* key, std::string name,
              std::string filePath, bool cancellable, int sizeX, int sizeY, int duration, int velocity) : super(key, name,
              filePath, cancellable, sizeX, sizeY, duration, velocity){
              //To-Do make it so that it check disk before creating
              //after creating save to folder with size and then use name of the animation 
                createAnimation(sizeX, sizeY, duration, velocity);
              }
   void createAnimation(int sizeX, int sizeY, int duration, int velocity){
    for (int i = 0; i< duration; i++){
    
          Frame *frame = new Frame(1);
          frame->addPixel(new Pixel(255,255,255,100,0,(int)i/velocity));
          super::addFrame(frame);
  }
}

};

