const int led=10;
const int ldr=A0;

void setup()
{
  pinMode(led,OUTPUT);
  pinMode(ldr,INPUT);
}

void loop()
{
  int l=analogRead(ldr);
  if(l<=300)
  {
    digitalWrite(led,HIGH);
  }else
  {
    digitalWrite(led,LOW);
  }
  delay(1000);
}
