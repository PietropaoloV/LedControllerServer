#include "Frame.h"
#include <string>
class Animation{
  /*
    Notes: Each frame will last ~16 milliseconds. The duration of an animation is up to the user.
    Animations will be updated to be saved in disk space to prevent the creation logic of an animation from being called multiple times;
    Animations will be scalable to allow for this each creation method will provide the size of the matrix so scaling can be takin into account;
    Each animation will take in a duration variable that will be used for validation of animation length.

  */
  //TO-DO may need to make custom key type
    char key; // Key affected by press
    std::string name; //name of the RenderedAnimation
    std::string filePath; //location of renderedAnimation
    bool cancellable; // Is the RenderedAnimation cancellable
    std::vector<Frame*> frames; // Frames from render file

  public:

    Animation(char key, std::string name,
              std::string filePath, bool cancellable, int sizeX, int sizeY){
      this -> name = name;
      this -> cancellable = cancellable;
      this -> filePath = filePath;
      this -> key = key;
      }

    char getKey(){return key;}
    std::string getName(){return name;}
    bool isCancellable(){return cancellable;}
    std::vector<Frame*> keyPressed(){return frames;}
    void addFrame(Frame *frame){frames.push_back(frame);}
    virtual void createAnimation(int sizeX, int sizeY) = 0;
    

  private:
    int loadFramesFromDisk(){return 1;}
    int saveFramesToDisk(){return 1;}
};
