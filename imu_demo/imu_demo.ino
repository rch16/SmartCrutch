#include <Wire.h>
 
#define MPU9250_ADDRESS 0x68
#define MAG_ADDRESS 0x0C
 
#define GYRO_FULL_SCALE_250_DPS 0x00 
#define GYRO_FULL_SCALE_500_DPS 0x08
#define GYRO_FULL_SCALE_1000_DPS 0x10
#define GYRO_FULL_SCALE_2000_DPS 0x18
 
#define ACC_FULL_SCALE_2_G 0x00 
#define ACC_FULL_SCALE_4_G 0x08
#define ACC_FULL_SCALE_8_G 0x10
#define ACC_FULL_SCALE_16_G 0x18
 
// This function read Nbytes bytes from I2C device at address Address. 
// Put read bytes starting at register Register in the Data array. 
void I2Cread(uint8_t Address, uint8_t Register, uint8_t Nbytes, uint8_t* Data)
{
// Set register address
Wire.beginTransmission(Address);
Wire.write(Register);
Wire.endTransmission();
 
// Read Nbytes
Wire.requestFrom(Address, Nbytes);
uint8_t index=0;
while (Wire.available())
Data[index++]=Wire.read();
}

// Write a byte (Data) in device (Address) at register (Register)
void I2CwriteByte(uint8_t Address, uint8_t Register, uint8_t Data)
{
// Set register address
Wire.beginTransmission(Address);
Wire.write(Register);
Wire.write(Data);
Wire.endTransmission();
}
 
// Initial time
long oldTime;
long newTime;
long startTime;

 
// Initializations
void setup()
{
// Arduino initializations
Wire.begin();
Serial.begin(9600);
 
// Set accelerometers low pass filter at 5Hz
I2CwriteByte(MPU9250_ADDRESS,29,0x06);
// Set gyroscope low pass filter at 5Hz
I2CwriteByte(MPU9250_ADDRESS,26,0x06);
 
 
// Configure gyroscope range
I2CwriteByte(MPU9250_ADDRESS,27,GYRO_FULL_SCALE_1000_DPS);
// Configure accelerometers range
I2CwriteByte(MPU9250_ADDRESS,28,ACC_FULL_SCALE_4_G);
// Set by pass mode for the magnetometers
I2CwriteByte(MPU9250_ADDRESS,0x37,0x02);
 
// Request continuous magnetometer measurements in 16 bits
I2CwriteByte(MAG_ADDRESS,0x0A,0x16);
 
pinMode(13, OUTPUT);
 
 
// Store initial time
oldTime = millis();
startTime = millis();
}
 
// Counter
long int cpt=0;
 

 
// Main loop, read and display data
void loop()
{
  //wait for a bit, 500ms
  newTime = millis();
  while((newTime - oldTime) < 500){
    newTime = millis();
    delay(10);  
  }
  oldTime = millis();
 
 
uint8_t chip_buffer[14];
I2Cread(MPU9250_ADDRESS,0x3B,14,chip_buffer);
 
// Create 16 bits values from 8 bits data
 
// Accelerometer
int16_t ax=-(chip_buffer[0]<<8 | chip_buffer[1]);
int16_t ay=-(chip_buffer[2]<<8 | chip_buffer[3]);
int16_t az=chip_buffer[4]<<8 | chip_buffer[5];
 
// Gyroscope
int16_t gx=-(chip_buffer[8]<<8 | chip_buffer[9]);
int16_t gy=-(chip_buffer[10]<<8 | chip_buffer[11]);
int16_t gz=chip_buffer[12]<<8 | chip_buffer[13];
 
// Display values
 
// Accelerometer
Serial.print("X: ");
Serial.println(ax,DEC);

Serial.print("Y: ");
Serial.println(ay,DEC);

Serial.print("Z: ");
Serial.println(az,DEC);
 
// Gyroscope
Serial.print (gx,DEC);
Serial.print ("\t");
Serial.print (gy,DEC);
Serial.print ("\t");
Serial.print (gz,DEC);
Serial.print ("\t");

}
