#include <LiquidCrystal.h>
#include <SoftwareSerial.h>

const int TX = 2;
const int RX = 3;
const int LED = 10;

SoftwareSerial BTSerial(TX,RX);
LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

void setup() {
  Serial.begin(9600);
  BTSerial.begin(9600);
  pinMode(LED, OUTPUT);
  lcd.begin(16, 2);
  lcd.setCursor(0,0);
  lcd.print("<LED>");
}

void loop() {
  // Read from the Serial Monitor and send to the Bluetooth module
  if (Serial.available())
    BTSerial.write(Serial.read());   

  // Read from the Bluetooth module and send to the Arduino Serial Monitor
  if (BTSerial.available())
  {
    char c = BTSerial.read();
    Serial.write(c);
    lcd.setCursor(0, 1);
    
    if(c == '1')
    {
      digitalWrite(LED, HIGH);
      lcd.print("     "); 
      lcd.setCursor(0, 1);
      lcd.print("On");
    }

    else if(c == '0')
    {
      digitalWrite(LED, LOW);
      lcd.print("OFF");
    }
  }
}