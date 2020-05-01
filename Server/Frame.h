#include "Pixel.h"
#include <vector>
class Frame{
  int size; //size of frame 
  std::vector<Pixel*> pixels; // Row Contents
  public:
    Frame(int size){
      this -> size = size;
    }

    Frame(int size, std::vector<Pixel*> pixels){
      this -> size = size;
      this -> pixels = pixels;
     
    } 

    ~Frame();
    int getSize(){return size;}
    std::vector<Pixel*> getPixels(){return pixels;}
    void setPixels(std::vector<Pixel*> pixels){this -> pixels = pixels;}
    void addPixel(Pixel *p){pixels.push_back(p);}
   
  private:

  
};
 Frame::~Frame(){
  for(unsigned int j=0; j < pixels.size(); j++) {
    delete pixels[j];
    
  }

}