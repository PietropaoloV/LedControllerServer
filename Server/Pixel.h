class Pixel{
  int red; 
  int blue;
  int green;
  int brightness;
  int xLoc;
  int yLoc;
  public:
  Pixel(int red, int blue, int green, int brightness, int xLoc, int yLoc){
    this -> red = red;
    this -> blue = blue;
    this -> green = green;
    this -> brightness = brightness;
    this -> xLoc = xLoc;
    this -> yLoc = yLoc;
    }
  int getRed(){return red;}
  int getBlue(){return blue;}
  int getGreen(){return green;}
  int getBrightness(){return brightness;}
  int getXLoc(){return xLoc;}
  int getYLoc(){return yLoc;}
  void setXloc(int xloc){this -> xLoc = xloc;}
  void setYloc(int yloc){this -> yLoc = yloc;}
  void setRed(int red){this -> red = red;}
  void setBlue(int blue){this -> blue = blue;}
  void setGreen(int green){this -> green = green;}
  void setBrightness(int brightness){this -> brightness = brightness;}
  Pixel copyPixel(Pixel c, int x, int y){
    return Pixel(c.getRed(), c.getBlue(), c.getGreen(), c.getBrightness(), x, y);
  }  
};