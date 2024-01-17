#include <Servo.h>
//usa ARDUI UNOOOO

Servo miServo;  // Crear un objeto de la clase Servo para controlar el servomotor
Servo miServo2;  // Crear un objeto de la clase Servo para controlar el servomotor
Servo miServo3;
Servo miServo4;
Servo miServo5;
Servo miServo6;
int tiempoEspera = 2000;  // Tiempo de espera entre movimientos en milisegundos (en este caso, 2 segundos)

void setup() {
  miServo.attach(2);  // El pin al que está conectado el servo (cámbialo si es necesario)
  miServo2.attach(3);
  miServo3.attach(4);
  miServo4.attach(5);
  miServo5.attach(6);
  miServo6.attach(7);
}

void loop() {
    miServo.write(0);  // Establecer la posición del servo
    miServo2.write(0);
    miServo3.write(0);
    miServo4.write(0);
    miServo5.write(0);
    miServo6.write(0);
    delay(1000);

    miServo.write(90);  // Establecer la posición del servo
    miServo2.write(90);
    miServo3.write(90);
    miServo4.write(90);
    miServo5.write(90);
    miServo6.write(90);
    delay(1000);

    miServo.write(180);  // Establecer la posición del servo
    miServo2.write(180);
    miServo3.write(180);
    miServo4.write(180);
    miServo5.write(180);
    miServo6.write(180);
    delay(1000);

  // Mover el servo de 0° a 180°
  /*
  for (int angulo = 0; angulo <= 180; angulo++) {
    miServo.write(angulo);  // Establecer la posición del servo
    miServo2.write(angulo);
    miServo3.write(angulo);
    miServo4.write(angulo);
    miServo5.write(angulo);
    miServo6.write(angulo);
    delay(15);  // Pequeño retardo para dar tiempo al servo de llegar a la posición
  }

  delay(tiempoEspera);  // Esperar el tiempo especificado

  // Mover el servo de 180° a 0°
  for (int angulo = 180; angulo >= 0; angulo--) {
    miServo.write(angulo);
    miServo2.write(angulo);
    miServo3.write(angulo);
    miServo4.write(angulo);
    miServo5.write(angulo);
    miServo6.write(angulo);
    delay(15);
  }

  delay(tiempoEspera);  // Esperar el tiempo especificado
  */
}

