# Object_detection_Ultrasonic_Sensor
#include <FastLED.h>
/* including the required library for running the LEDs*/
#define LED_PIN     2 /*defining pin 2 as LED pin */
#define NUM_LEDS    13 /*setting 13 LED's from the LED strip*/
#define trigPin 13 /*defining pin 13 for Trigger for the ultrasonic sensor*/
#define echoPin 9 /*defining pin 9 for echo for the ultrasonic sensor*/


CRGB leds[NUM_LEDS];
/* declaring an array of CRGB objects for controlling the LED strip */

void setup()
/* setup function runs once at the beginning of the program for and sets all the outputs and input pins*/
 {
  FastLED.addLeds<WS2812, LED_PIN, GRB>(leds, NUM_LEDS);
  /* Initializing the LED strip with FastLED library */
  Serial.begin(9600);
  /* starting the serial communication at a baud rate of 9600 */
  pinMode(trigPin, OUTPUT);
  /*setting trig Pin as an output pin*/
  pinMode(echoPin, INPUT);
  /*setting echo Pin as input pin*/
}

void loop() {
/*loop function runs again and again continously after every execution*/
  digitalWrite(trigPin, LOW);
  /*setting trigPin as LOW(off)*/
  delayMicroseconds(10);
  /*delay for 10 microsecond */

  digitalWrite(trigPin, HIGH);
  /*setting trigPin as High(ON)*/
  delayMicroseconds(20);
  /*delay for 20 microsecond*/
  digitalWrite(trigPin, LOW);
  /*setting trigPin as LOW(off)*/

  long duration = pulseIn(echoPin, HIGH);
  /* measuring the duration of the echo signal using pulseIn() function */
  long distance = duration * 0.034 / 2;
  /*calculating distance using speed formula*/


  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
  /*printing the distance in cm's */
if (distance<10)
/*checking if distance is smaller than 10*/
{
  
  leds[0] = CRGB(255, 0, 0);
  FastLED.show();
  /*turn on led 1 as red*/
  leds[1] = CRGB(255, 0, 0);
  FastLED.show();
 /*turn on led 2 as red*/
  leds[2] = CRGB(255, 0, 0);
  FastLED.show();
 /*turn on led 3 as red*/
  leds[3] = CRGB(255, 0, 0);
  FastLED.show();
/*turn on led 4 as red*/
  leds[4] = CRGB(255, 0, 0);
  FastLED.show();
/*turn on led 5 as red*/
  leds[5] = CRGB(255, 0, 0);
  FastLED.show();
 /*turn on led 6 as red*/
  leds[6] = CRGB(255, 0, 0);
  FastLED.show();
   /*turn on led 7 as red*/
  leds[7] = CRGB(255, 0, 0);
  FastLED.show();
 /*turn on led 8 as red*/
  leds[8] = CRGB(255, 0, 0);
  FastLED.show();
/*turn on led 9 as red*/
  leds[9] = CRGB(255, 0, 0);
  FastLED.show();
 /*turn on led 10 as red*/
  leds[10] = CRGB(255, 0, 0);
  FastLED.show();
 /*turn on led 11 as red*/
  leds[11] = CRGB(255, 0, 0);
  FastLED.show();
/*turn on led 12 as red*/
  leds[12] = CRGB(255, 0, 0);
  FastLED.show();
/*turn on led 13 as red*/
  leds[13 ] = CRGB(255, 0, 0);
  FastLED.show();
/*turn on led 14 as red*/
}
else if (distance>10 && distance<=30)
{
/*if distance is between 10cm and 30cm*/
  leds[0] = CRGB(0, 0, 255);
  FastLED.show();
/*set led 1 as blue*/
  leds[1] = CRGB(0, 0, 255);
  FastLED.show();
/*set led 2 as blue*/
  leds[2] = CRGB(0, 0, 255);
  FastLED.show();
/*set led 3 as blue*/
  leds[3] = CRGB(0, 0, 255);
  FastLED.show();
/*set led 4 as blue*/
  leds[4] = CRGB(0, 0, 255);
  FastLED.show();
/*set led 5 as blue*/
  leds[5] = CRGB(0, 0, 255);
  FastLED.show();
/*set led 6 as blue*/
  leds[6] = CRGB(0, 0, 255);
  FastLED.show();
 /*set led 7 as blue*/ 
   leds[7] = CRGB(0, 0, 255);
  FastLED.show();
/*set led 8 as blue*/
  leds[8] = CRGB(0, 0, 255);
  FastLED.show();
/*set led 9 as blue*/
  leds[9] = CRGB(0, 0, 255);
  FastLED.show();
/*set led 10 as blue*/
  leds[10] = CRGB(0, 0, 255);
  FastLED.show();
/*set led 11 as blue*/
  leds[11] = CRGB(0, 0, 255);
  FastLED.show();
/*set led 12 as blue*/
  leds[12] = CRGB(0, 0, 255);
  FastLED.show();
/*set led 13 as blue*/
  leds[13] = CRGB(0, 0, 255);
  FastLED.show();
/*set led 14 as blue*/
}
else if (distance>=30 && distance<50)
{
/*if distance is smaller than 50cm and higher than 30 then set all lets as green*/
  leds[0] = CRGB(0, 255, 0);
  FastLED.show();
 /*set led 1 as green*/
  leds[1] = CRGB(0, 255, 0);
  FastLED.show();
/*set led 2 as green*/
  leds[2] = CRGB(0, 255, 0);
  FastLED.show();
/*set led 3 as green*/
  leds[3] = CRGB(0, 255,0);
  FastLED.show();
/*set led 4 as green*/
  leds[4] = CRGB(0, 255,0);
  FastLED.show();
/*set led 5 as green*/
  leds[5] = CRGB(0, 255,0);
  FastLED.show();
/*set led 6 as green*/
  leds[6] = CRGB(0, 255,0);
  FastLED.show();
  /*set led 7 as green*/
  leds[7] = CRGB(0, 255, 0);
  FastLED.show();
 /*set led 8 as green*/
  leds[8] = CRGB(0, 255, 0);
  FastLED.show();
/*set led 9 as green*/
  leds[9] = CRGB(0, 255, 0);
  FastLED.show();
/*set led 10 as green*/
  leds[10] = CRGB(0, 255,0);
  FastLED.show();
/*set led 11 as green*/
  leds[11] = CRGB(0, 255,0);
  FastLED.show();
/*set led 12 as green*/
  leds[12] = CRGB(0, 255,0);
  FastLED.show();
/*set led 13 as green*/
  leds[13] = CRGB(0, 255,0);
  FastLED.show();
  /*set led 14 as green*/
}
else if (distance>=50)
{ 
  /*if distance is greater than 50cm then set all lets as yellow*/
  leds[0] = CRGB(160,32,240);
  FastLED.show();
  /*set led 1 as yellow*/
  delay(100);
  /*delay for 100 microseconds*/
  leds[1] = CRGB(160,32,240);
  FastLED.show();
  /*set led 2 as yellow*/
   delay(100);
   /*delay for 100 microseconds*/
  leds[2] = CRGB(160,32,240);
  FastLED.show();
  /*set led 3 as yellow*/
 delay(100);
 /*delay for 100 microseconds*/
  leds[3] = CRGB(160,32,240);
  FastLED.show();
  /*set led 4 as yellow*/
 delay(100);
 /*delay for 100 microseconds*/
  leds[4] = CRGB(160,32,240);
  FastLED.show();
  /*set led 5 as yellow*/
 delay(100);
 /*delay for 100 microseconds*/
  leds[5] = CRGB(160,32,240);
  FastLED.show();
  /*set led 6 as yellow*/
 delay(100);
 /*delay for 100 microseconds*/
  leds[6] = CRGB(160,32,240);
  FastLED.show();
  /*set led 7 as yellow*/
    delay(100);
    /*delay for 100 microseconds*/
  leds[7] = CRGB(160,32,240);
  FastLED.show();
  /*set led 8 as yellow*/
 delay(100);
 /*delay for 100 microseconds*/
  leds[8] = CRGB(160,32,240);
  FastLED.show();
  /*set led 9 as yellow*/
 delay(100);
 /*delay for 100 microseconds*/
  leds[9] = CRGB(160,32,240);
  FastLED.show();
  /*set led 10 as yellow*/
 delay(100);
 /*delay for 100 microseconds*/
  leds[10] = CRGB(160,32,240);
  FastLED.show();
  /*set led 11 as yellow*/
 delay(100);
 /*delay for 100 microseconds*/
  leds[11] = CRGB(160,32,240);
  FastLED.show();
  /*set led 12 as yellow*/
 delay(100);
 /*delay for 100 microseconds*/
  leds[12] = CRGB(160,32,240);
  FastLED.show();
  /*set led 13 as yellow*/
 delay(100);
 /*delay for 100 microseconds*/
  leds[13 ] = CRGB(160,32,240);
  FastLED.show();
  /*set led 14 as yellow*/
  delay(100);
  /*if distance is greater than 50cm then set all lets as purple*/
   leds[0] = CRGB(255,255,0);
  FastLED.show();
  /*set let 1 as purple*/
  delay(100);
  /*delay for 100 microseconds*/
  leds[1] = CRGB(255,255,0);
  FastLED.show();
  /*set led 2 as purple */
   delay(100);
   /*delay for 100 microseconds*/
  leds[2] = CRGB(255,255,0);
  FastLED.show();
  /*set led 3 as purple */
 delay(100);
 /*delay for 100 microseconds*/
  leds[3] = CRGB(255,255,0);
  FastLED.show();
  /*set led 4 as purple */
 delay(100);
 /*delay for 100 microseconds*/
  leds[4] = CRGB(255,255,0);
  FastLED.show();
  /*set led 5 as purple */
 delay(100);
 /*delay for 100 microseconds*/
  leds[5] = CRGB(255,255,0);
  FastLED.show();
  /*set led 6 as purple */
 delay(100);
 /*delay for 100 microseconds*/
  leds[6] = CRGB(255,255,0);
  FastLED.show();
  /*set led 7 as purple */
    delay(100);
    /*delay for 100 microseconds*/
  leds[7] = CRGB(255,255,0);
  FastLED.show();
  /*set led 8 as purple */
 delay(100);
 /*delay for 100 microseconds*/
  leds[8] = CRGB(255,255,0);
  FastLED.show();
  /*set led 9 as purple */
 delay(100);
 /*delay for 100 microseconds*/
  leds[9] = CRGB(255,255,0);
  FastLED.show();
  /*set led 10 as purple */
 delay(100);
 /*delay for 100 microseconds*/
  leds[10] = CRGB(255,255,0);
  FastLED.show();
  /*set led 11 as purple */
 delay(100);
 /*delay for 100 microseconds*/
  leds[11] = CRGB(255,255,0);
  FastLED.show();
  /*set led 12 as purple */
 delay(100);
 /*delay for 100 microseconds*/
  leds[12] = CRGB(255,255,0);
  FastLED.show();
  /*set led 13 as purple */
 delay(100);
 /*delay for 100 microseconds*/
  leds[13 ] = CRGB(255,255,0);
  FastLED.show();
  /*set led 14 as purple*/
}
  
}
