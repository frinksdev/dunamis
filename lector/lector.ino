#define lm35 0
int ASignal = A1;

char set;

void setup()
{
  Serial.begin(9600);
};

void loop()
{
  bombo();
  if (Serial.available() > 0)
  {
    set = Serial.read();
    if (set=='A')
    {
      temp();
    }
    if(set=='B')
    {
      humd();
    }
    if (set=='I')
    {
      bomba();
    }
    if (set=='O')
    {
      bombo();
    }
  }
}


void temp()
{
  float temp = (5.0 * analogRead(lm35)*100.0)/1023.0;
  Serial.println(temp);
}

void humd()
{
  int sensorValue = analogRead(ASignal);
  Serial.println(sensorValue);
}

void bomba()
{
  digitalWrite(13,HIGH);
}

void bombo()
{
  digitalWrite(13,LOW);
}
