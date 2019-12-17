#define MOTOR_PIN 15
 
// the setup routine runs once when you press reset:
void setup()
{
  // initialize motor pin
  pinMode(MOTOR_PIN, OUTPUT);
  // start off
  digitalWrite(MOTOR_PIN, LOW);
}
 
// the loop routine runs over and over again forever:
void loop() {
    digitalWrite(MOTOR_PIN, HIGH); // turn motor on
    delay(5000); // wait for 5s
    digitalWrite(MOTOR_PIN, HIGH); // turn motor off
    delay(5000); // wait for 5s
}
