# Circuit Design

## Aim
The aim of the task is to design and code a circuit (Aurdino) which should be able to stop the motion of a motor when the detects an obstacle within 100 cm and notify the user about the obstacle.

## Apparatus Used
- Aurdino Uno R3
- DC Motor
- Ultrasonic Distance Sensor
- Resistors
- LED RGB light

## Procedure
- Firstly, I have connected the circuit accordingly and I have used Ultrasonic Distance Sensor to determine the distance from the obstacle.
- Distance is calculated by using the formula **Distance = Velocity * time**.
   - Velocity of sound in air is 340 m/s
   - Here time is time taken by the ultrasonic wave to hit the obstacle and travel back.
   - Distance = 0.034*time/2 cms
- If there is no obstacle in the range of 100 cms from the Ultrasonic distance sensor, then the motor starts rotating and LED will show up **Green** light.
- If there is an obstacle within the range of 100 cms from the Ultrasonic distance sensor, then the motor stops rotating and the LED will show up **RED** light.

# Circuit Simulation
![Screenshot from 2021-04-17 15-59-35](https://user-images.githubusercontent.com/74526207/115114292-20e4f800-9fac-11eb-8845-17a43f73e060.png)


# Code
#define TRIGPIN 5
#define ECHOPIN 6
void setup()
{
  pinMode(12, OUTPUT);
  Serial.begin(9600);
  pinMode(TRIGPIN, OUTPUT);
  pinMode(ECHOPIN, INPUT);
  pinMode(11,OUTPUT);
  pinMode(10,OUTPUT);
}
void loop()
{
  int TimeTaken, distance;
  digitalWrite(TRIGPIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIGPIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGPIN, LOW);
  TimeTaken = pulseIn(ECHOPIN, HIGH);
  distance = (TimeTaken * 0.034)/2;
  Serial.println(distance);
  if(distance>100){
   digitalWrite(11, HIGH);
  digitalWrite(12,HIGH);
  digitalWrite(10,LOW);
  }
  else{digitalWrite(12,LOW);
      digitalWrite(10,HIGH);
      digitalWrite(11,LOW);}
}
