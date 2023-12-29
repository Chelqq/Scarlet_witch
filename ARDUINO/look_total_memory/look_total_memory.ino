#include <EEPROM.h>

void setup() {
  Serial.begin(9600);

  Serial.print("Capacidad de memoria: "); 
  Serial.println( EEPROM.length());
  Serial.println(" ");

  Serial.print("Valor almacenado en direccion 0: "); 
  Serial.println( EEPROM.read(0) );  // read(direccion)
  
  Serial.print("Almacenando numero 39 en direccion 0"); 
  EEPROM.write(0, 39); // write(direccion, valor)  
}

void loop(){}