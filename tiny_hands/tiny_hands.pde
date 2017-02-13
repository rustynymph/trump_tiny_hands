import oscP5.*;
import netP5.*;

//OSC
OscP5 oscP5;
NetAddress dest;

PImage trump;
PImage right;
PImage left;
int handsize;

void setup(){
  oscP5 = new OscP5(this,12000); //listen for OSC messages on port 12000
  dest = new NetAddress("127.0.0.1",9091);  
  size(600, 400);
  handsize = 100;
  trump = loadImage("trump.png");
  right = loadImage("right.jpg");
  left = loadImage("left.png");
  trump.resize(600, 400);
  right.resize(handsize, handsize);
  left.resize(handsize, handsize);
}

void draw(){
  clear();
  background(255);
  right.resize(handsize, handsize);
  left.resize(handsize, handsize);  
  image(trump, 0, 0);
  image(right, 445, 220);
  image(left, 50, 220);
}

void oscEvent(OscMessage theOscMessage) {
  println(theOscMessage);
  if(theOscMessage.checkAddrPattern("/wek/outputs") == true){
    if(theOscMessage.checkTypetag("f")){
      handsize = int(map(theOscMessage.get(0).floatValue(), 0.0, 1.0, 50, 100));
    }
  }
}