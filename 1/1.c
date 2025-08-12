const int red=8;
const int yellow=9;
const int green=10;
void setup(){
  pinMode(red,OUTPUT);
   pinMode(yellow,OUTPUT);
   pinMode(green,OUTPUT);
}
void light(int r,int y,int g,int d)
{
  digitalWrite(red,r);
  digitalWrite(yellow,y);
  digitalWrite(green,g);
  delay(d);
}
void loop()
{
  light(HIGH,LOW,LOW,1000);
  light(LOW,HIGH,LOW,1000);
  light(LOW,LOW,HIGH,1000);
  delay(1000);
}
