#include "HX711.h"

#define LOAD_DOUT_PIN 12
#define LOAD_CLK_PIN 14

// initialise hx711
HX711 scale(LOAD_DOUT_PIN, LOAD_CLK_PIN);

// Loadcell reading
long zeroFactor; // baseline
float pressure;
float units;
float ounces;
float calibrationFactor = 70;

void setup() {
  Serial.begin(9600);
  Serial.println("HX711 calibration sketch");
  Serial.println("Remove all weight from scale");
  Serial.println("After readings begin, place known weight on scale");
  Serial.println("Press + or a to increase calibration factor");
  Serial.println("Press - or z to decrease calibration factor");

  scale.set_scale();
  scale.tare();  //Reset the scale to 0

  zeroFactor = scale.read_average(); //Get a baseline reading
  Serial.print("Zero factor: "); //This can be used to remove the need to tare the scale. Useful in permanent scale projects.
  Serial.println(zeroFactor);
}

void loop() {

  scale.set_scale(calibrationFactor); //Adjust to this calibration factor

  units = scale.get_units(), 10;

  ounces = units * 0.035274;
  Serial.print("Reading: ");
  Serial.print(abs(units));
  Serial.print("     Calibration Factor: ");
  Serial.println(calibrationFactor);

  if(Serial.available())
  {
    char temp = Serial.read();
    if(temp == '+' || temp == 'a')
      calibrationFactor += 1;
    else if(temp == '-' || temp == 'z')
      calibrationFactor -= 1;
  }
}
