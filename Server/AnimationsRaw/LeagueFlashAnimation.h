class LeagueFlashAnimation: public Animation{
public:
  typedef Animation super;
  LeagueFlashAnimation(char key, std::string name,
              std::string filePath, bool cancellable, int sizeX, int sizeY) : super(key, name,
              filePath, cancellable, sizeX, sizeY){
              //To-Do make it so that it check disk before creating
              //after creating save to folder with size and then use name of the animation 
                createAnimation(sizeX, sizeY);
              }
   void createAnimation(int sizeX, int sizeY){
   for(int i = 0; i < sizeX; i++){
    for (int j = 0; j < (int)240 / sizeX; ++j){
      Frame *frame = new Frame(1);
      frame->addPixel(new Pixel(255,255,255,100,i,i));
      super::addFrame(frame);
      }
    }
  }

};

