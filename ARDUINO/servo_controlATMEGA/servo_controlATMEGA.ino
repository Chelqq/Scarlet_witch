#include <Servo.h>

Servo miServo;  // Crear un objeto de la clase Servo para controlar el servomotor
Servo miServo2;  // Crear un objeto de la clase Servo para controlar el servomotor
int tiempoEspera = 2000;  // Tiempo de espera entre movimientos en milisegundos (en este caso, 2 segundos)

void setup() {
  miServo.attach(8);  // El pin al que está conectado el servo (cámbialo si es necesario)
  miServo2.attach(7);
}

void loop() {
  // Mover el servo de 0° a 180°
  for (int angulo = 0; angulo <= 180; angulo++) {
    miServo.write(angulo);  // Establecer la posición del servo
    miServo2.write(angulo);
    delay(15);  // Pequeño retardo para dar tiempo al servo de llegar a la posición
  }

  delay(tiempoEspera);  // Esperar el tiempo especificado

  // Mover el servo de 180° a 0°
  for (int angulo = 180; angulo >= 0; angulo--) {
    miServo.write(angulo);
    miServo2.write(angulo);
    delay(15);
  }

  delay(tiempoEspera);  // Esperar el tiempo especificado
}

