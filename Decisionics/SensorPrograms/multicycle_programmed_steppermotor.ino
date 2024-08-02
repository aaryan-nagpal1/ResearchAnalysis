const int stepPin = 5; 
const int dirPin = 2; 
const int enPin = 8;
const unsigned long RunTime_phase1 = 600000; // run time phase motor 1 in ms (total : 10 minutes)
const unsigned long RunTime_phase2 = 660000; // run time phase motor 2 in ms (total : 11 minutes)
const unsigned long RunTime_phase3 = 780000; // run time phase motor 3 in ms (total : 13 minutes)
const unsigned long RunTime_phase4 = 1200000; // run time phase motor 4 in ms (total : 20 minutes)
const unsigned long RunTime_phase5 = 1260000; // run time phase motor 5 in ms (total : 21 minutes)
const unsigned long RunTime_phase6 = 1380000; // run time phase motor 6 in ms (total : 23 minutes)
const unsigned long RunTime_phase7 = 1500000; // run time phase motor 7 in ms (total : 25 minutes)
const unsigned long initialDelay = 600000; // initial delay period in ms (10 minutes)
const int numberOfCycles = 3;

void setup() {
  pinMode(stepPin, OUTPUT); 
  pinMode(dirPin, OUTPUT);
  pinMode(enPin, OUTPUT);
  digitalWrite(enPin, LOW); // Enable motor driver
}

void loop() {
  static unsigned long startTime = millis(); // remember when the motor started
  static bool initialDelayCompleted = false;
  static int completedCycles = 0;

  if (!initialDelayCompleted) {
    // Initial delay period of 10 minutes
    if (millis() - startTime >= initialDelay) {
      initialDelayCompleted = true;
      startTime = millis(); // Reset start time after the initial delay
    }
  } else {
    unsigned long elapsedTime = millis() - startTime;

    if (elapsedTime < RunTime_phase1) {
      // Phase 1: 22.5ml to 0ml in 10 mins
      digitalWrite(dirPin, HIGH); // Set direction HIGH = Backward, LOW = Forward
      stepMotor1and7();
    } 
    else if (elapsedTime < RunTime_phase2) {
      // Phase 2: 0ml to 11.25ml in 1 min
      digitalWrite(dirPin, LOW);
      stepMotor2and5();
    }
    else if (elapsedTime < RunTime_phase3) {
      // Phase 3: hold at 11.25ml for 2 mins
      digitalWrite(dirPin, LOW);
      stepMotorZero();
    }   
    else if (elapsedTime < RunTime_phase4) {
      // Phase 4: 11.25ml to 42.75ml in 7 mins
      digitalWrite(enPin, LOW); // Enable motor driver
      digitalWrite(dirPin, LOW); // Keep motor direction
      stepMotor4();
    }
    else if (elapsedTime < RunTime_phase5) {
      // Phase 5: 42.75ml to 31.5ml in 1 min
      digitalWrite(dirPin, HIGH);
      stepMotor2and5();
    }
    else if (elapsedTime < RunTime_phase6) {
      // Phase 6: hold at 31.5ml for 2 mins
      digitalWrite(dirPin, HIGH);
      stepMotorZero();
    }
    else if (elapsedTime < RunTime_phase7) {
      // Phase 7: 31.5ml to 22.5ml in 2 mins
      digitalWrite(enPin, LOW); // Enable motor driver
      digitalWrite(dirPin, HIGH); // Keep motor direction
      stepMotor1and7();
    }  
    else {
      // Completed one cycle
      completedCycles++;
      if (completedCycles >= numberOfCycles) {
        // Stop everything after completing the specified number of cycles
        digitalWrite(enPin, HIGH); // Disable motor driver
        while (true) {} // Stay in a loop, effectively stopping further execution
      } else {
        // Reset the start time for the next cycle
        startTime = millis();
      }
    }
  }
}

void stepMotor1and7() {
  for (int x = 0; x < 500; x++) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(50);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(50);
  }
  delay(11536);
}

void stepMotor2and5() {
  for (int x = 0; x < 500; x++) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(50);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(50);
  }
  delay(2307);
}

void stepMotor4() {
  for (int x = 0; x < 500; x++) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(50);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(50);
  }
  delay(5768);
}

void stepMotorZero(){
  delay(200);
}


