const int stepPin = 5; 
const int dirPin = 2; 
const int enPin = 8;
const unsigned long RunTime_phase = 3600000; // run time phase motor in ms

void setup() {
  pinMode(stepPin, OUTPUT); 
  pinMode(dirPin, OUTPUT);
  pinMode(enPin, OUTPUT);
  digitalWrite(enPin, LOW); // Enable motor driver
}

void loop() {
  static unsigned long startTime = millis(); // remember when the motor started

  unsigned long elapsedTime = millis() - startTime;

  if (elapsedTime < RunTime_phase) {
    // Phase 1: Motor running in one direction
    digitalWrite(dirPin, LOW); // Set direction
    stepMotor();
  } 
  else if (elapsedTime < 2 * RunTime_phase) {
    // Phase 2: Motor stopped
    digitalWrite(enPin, HIGH); // Disable motor driver
    delay(10); // Small delay to ensure motor is stopped
  } 
  else if (elapsedTime < 3 * RunTime_phase) {
    // Phase 3: Motor running in the opposite direction
    digitalWrite(enPin, LOW); // Enable motor driver
    digitalWrite(dirPin, HIGH); // Set opposite direction
    stepMotor();
  } 
  else {
    // Stop everything
    digitalWrite(enPin, HIGH); // Disable motor driver
    while (true) {} // Stay in a loop, effectively stopping further execution
  }
}

void stepMotor() {
  // Function to step the motor
  for (int x = 0; x < 200; x++) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(50);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(50);
  }
  delay(13167); // Delay between steps
}