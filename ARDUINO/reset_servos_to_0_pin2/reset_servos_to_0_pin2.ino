#include <Servo.h>
Servo miServo;  // Crear un objeto de la clase Servo para controlar el servomotor

void setup() {
  // put your setup code here, to run once:
  miServo.attach(7);  // El pin al que está conectado el servo (cámbialo si es necesario)
  
}

void loop() {
  miServo.write(0);
  delay(1000);  
  miServo.write(180);
  delay(1000);
}
