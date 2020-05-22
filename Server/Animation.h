#include "Frame.h"
#include "Key.h"
#include <string>
class Animation{
  /*
    Notes: Each frame will last ~16 milliseconds. The duration of an animation is up to the user.
    Animations will be updated to be saved in disk space to prevent the creation logic of an animation from being called multiple times;
    Animations will be scalable to allow for this each creation method will provide the size of the matrix so scaling can be takin into account;
    Each animation will take in a duration variable that will be used for validation of animation length.

  */
  //TO-DO may need to make custom key type
    Key *key; // Key affected by press
    int duration; //number of ticks an animation lasts
    int velocity; //speed at which animaitions occur
    std::string name; //name of the RenderedAnimation
    std::string filePath; //location of renderedAnimation
    bool cancellable; // Is the RenderedAnimation cancellable
    std::vector<Frame*> frames; // Frames from render file

  public:

    Animation(Key *key, std::string name,
              std::string filePath, bool cancellable, int sizeX, int sizeY, int duration, int velocity){
      this -> name = name;
      this -> cancellable = cancellable;
      this -> filePath = filePath;
      this -> key = key;
      this -> duration = duration;
      this -> velocity = velocity;
      }

    Key* getKey(){return key;}
    std::string getName(){return name;}
    bool isCancellable(){return cancellable;}
    std::vector<Frame*> keyPressed(){return frames;}
    void addFrame(Frame *frame){frames.push_back(frame);}
    virtual void createAnimation(int sizeX, int sizeY, int duration, int velocity) = 0;
    

  private:
    int loadFramesFromDisk(){return 1;}
    int saveFramesToDisk(){return 1;}
};
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