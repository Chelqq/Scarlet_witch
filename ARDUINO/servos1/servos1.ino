#include <Servo.h>

Servo servol;

int PINSERVO = 12;
int PULSOMIN = 1000;
int PULSOMAX = 2000;

void setup () {
  servol.attach (PINSERVO, PULSOMIN, PULSOMAX);
}

void loop() {
  servol.write(0);
  delay(5000);
  servol.write(180);
  delay(5000);
}