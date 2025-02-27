#include <Servo.h>

Servo lightSwitchServo;
int servoPin = 9;  
int onPosition = 90;  
int offPosition = 0;  

void setup() {
    Serial.begin(9600);
    lightSwitchServo.attach(servoPin);
    Serial.println("Arduino ready");
    lightSwitchServo.write(60);
}

void loop() {
    if (Serial.available() > 0) {  // Check if data is available
        String command = Serial.readStringUntil('\n');  
        command.trim();  

        Serial.print("Received command: "); 
        Serial.println(command);  

        if (command == "ON") {
            Serial.println("Turning light ON...");
            lightSwitchServo.write(150);  
            delay(500);  
           
        } 
        else if (command == "OFF") {
            Serial.println("Turning light OFF...");
            lightSwitchServo.write(10);  
            delay(500);
              
        } 
        else if (command == "NEUTRAL"){
            Serial.println("Neutral state, stopping servo.");
           
            delay(500);
        }
        else if (command == "EXIT") {
            Serial.println("Exiting, resetting servo...");
            lightSwitchServo.write(90);  // Stops servo
            delay(500);
        } 
        else {
            Serial.println("Invalid command received.");
        }
    }
}
