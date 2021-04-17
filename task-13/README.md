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

