#include "HX711.h"

#define LOAD_DOUT_PIN 14
#define LOAD_CLK_PIN 12
#define LED_BLUE_PIN 0
#define LED_RED_PIN 2
#define LED_GREEN_PIN 16
#define MOTOR_PIN 15

// initialise hx711
HX711 scale(LOAD_DOUT_PIN, LOAD_CLK_PIN);

// Loadcell reading
long zeroFactor; // baseline
float pressure;
float units;
float ounces;
float calibrationFactor = 70;
float kg_units;

void setup() {
  Serial.begin(9600);
  Serial.println("HX711 calibration sketch");
  Serial.println("Remove all weight from scale");
  Serial.println("After readings begin, place known weight on scale");
  Serial.println("Press + or a to increase calibration factor");
  Serial.println("Press - or z to decrease calibration factor");

  // initialize led pins
  pinMode(LED_RED_PIN, OUTPUT);
  pinMode(LED_GREEN_PIN, OUTPUT);
  pinMode(LED_BLUE_PIN, OUTPUT);
  // start off
  digitalWrite(LED_RED_PIN, LOW);
  digitalWrite(LED_GREEN_PIN, LOW);
  digitalWrite(LED_BLUE_PIN, LOW);

  // initialize motor pin
  pinMode(MOTOR_PIN, OUTPUT);
  // start off
  digitalWrite(MOTOR_PIN, LOW);

  scale.set_scale();
  scale.tare();  //Reset the scale to 0

  zeroFactor = scale.read_average(); //Get a baseline reading
  Serial.print("Zero factor: "); //This can be used to remove the need to tare the scale. Useful in permanent scale projects.
  Serial.println(zeroFactor);
}

void loop() {

  scale.set_scale(calibrationFactor); //Adjust to this calibration factor

  units = scale.get_units(10), 2;

  Serial.println(units);
  
  kg_units = units/1000;
  
  float threshold = 1.5; // threshold for amount of weight placed through crutch
  // allow for 5% variability in the threshold
  float upper_bound = 1.05*threshold;
  float lower_bound = 0.95*threshold;

  if(kg_units > upper_bound){
    // turn on
    digitalWrite(LED_RED_PIN, HIGH);
    digitalWrite(MOTOR_PIN, HIGH);
  }
  else{
    // turn off
    digitalWrite(LED_RED_PIN,LOW);
    digitalWrite(MOTOR_PIN, LOW);
  }
  
  //Serial.print("Reading: ");
  //Serial.println(abs(kg_units));
  //Serial.print("     Calibration Factor: ");
  //Serial.println(calibrationFactor);

//  if(Serial.available())
//  {
//    char temp = Serial.read();
//    if(temp == '+' || temp == 'a')
//      calibrationFactor += 1;
//    else if(temp == '-' || temp == 'z')
//      calibrationFactor -= 1;
//  }
}
