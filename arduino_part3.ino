/*
Arduino reads voltage value
*/

int bottomLeft = 3;     // bottom left potentiometer wiper (middle terminal) connected to analog pin 3
int bottomRight = 4;
int topLeft = 5;
int topCenter = 6;
int topRight = 7;
// outside leads to ground and +5V

int bLval = 0;           // variable to store the value read
int bRval = 0;
int tLval = 0;
int tCval = 0;
int tRval = 0;

int bLvalPrev = -1;           // variable to store the last value read (to detect any changes)
int bRvalPrev = -1;
int tLvalPrev = -1;
int tCvalPrev = -1;
int tRvalPrev = -1;
float voltage = -1;
void setup()
{
  Serial.begin(9600);              //  setup serial
}

void loop()
{
  //Read all input pins
  bLval = analogRead(bottomLeft);     // read the input pin
  bRval = analogRead(bottomRight);
  tLval = analogRead(topLeft);
  tCval = analogRead(topCenter);
  tRval = analogRead(topRight);

  //Check if any change was made to the values: write to serial Voltage + 10*identifier
  //Identifiers:
  //1: change bLval
  //2: change bRval
  //3: change tLval
  //4: change tCval
  //5: change tRval

  voltage=bLval/204.0 + 10;
  Serial.println(voltage);

 
  voltage=bRval/204.0 + 20;
  Serial.println(voltage);

  voltage=tLval/204.0 + 30;
  Serial.println(voltagef);

  voltage=tCval/204.0;
  Serial.println(voltage + 40);
  
  voltage=tRval/204.0;
  Serial.println(voltage + 50);
  

}

