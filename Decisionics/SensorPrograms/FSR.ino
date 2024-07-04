const int fsrPin1 = A0;          // Analog input pin for the first FSR
const int fsrPin2 = A1;          // Analog input pin for the second FSR
const int fsrPin3 = A2;          // Analog input pin for the third FSR
const int serialBaudRate = 9600;

// Calibration values for FSR1 - replace these with your own calibrated values
const float analogMin1 = 0;     // Minimum analog reading for FSR1 (corresponding to 0 Newtons)
const float analogMax1 = 1023;  // Maximum analog reading for FSR1 (corresponding to the maximum force applied)
const float forceMin1 = 0;      // Minimum force in Newtons for FSR1
const float forceMax1 = 5;     // Maximum force in Newtons for FSR1 (adjust this based on your calibration)

// Calibration values for FSR2 - replace these with your own calibrated values
const float analogMin2 = 0;     // Minimum analog reading for FSR2 (corresponding to 0 Newtons)
const float analogMax2 = 1023;  // Maximum analog reading for FSR2 (corresponding to the maximum force applied)
const float forceMin2 = 0;      // Minimum force in Newtons for FSR2
const float forceMax2 = 5;     // Maximum force in Newtons for FSR2 (adjust this based on your calibration)

// Calibration values for FSR3 - replace these with your own calibrated values
const float analogMin3 = 0;     // Minimum analog reading for FSR3 (corresponding to 0 Newtons)
const float analogMax3 = 1023;  // Maximum analog reading for FSR3 (corresponding to the maximum force applied)
const float forceMin3 = 0;      // Minimum force in Newtons for FSR3
const float forceMax3 = 5;     // Maximum force in Newtons for FSR3 (adjust this based on your calibration)

void setup() {
  Serial.begin(serialBaudRate); // Initialize serial communication
  Serial.println("Time (ms), FSR1 Force (N), FSR2 Force (N), FSR3 Force (N)"); // Print the header for Serial Plotter
}

void loop() {
  float cf = 1.15;
  float cf2 = 0.99;
  unsigned long startTime = millis(); // Get the current time in milliseconds
  
  int fsrValue1 = analogRead(fsrPin1); // Read the analog value from FSR1
  int fsrValue2 = analogRead(fsrPin2); // Read the analog value from FSR2
  int fsrValue3 = analogRead(fsrPin3); // Read the analog value from FSR3

  // Map the analog value to a force range in Newtons based on the calibration values for FSR1
  float force1 = mapfloat(fsrValue1, analogMin1, analogMax1, forceMin1, forceMax1);

  // Map the analog value to a force range in Newtons based on the calibration values for FSR2
  float force2 = mapfloat(fsrValue2, analogMin2, analogMax2, forceMin2, forceMax2);

  // Map the analog value to a force range in Newtons based on the calibration values for FSR3
  float force3 = mapfloat(fsrValue3, analogMin3, analogMax3, forceMin3, forceMax3);

  Serial.print(startTime); // Print the current time in milliseconds
  Serial.print(", ");
  Serial.print(force1*cf); // Print FSR1 force reading in Newtons
  Serial.print(", ");
  Serial.print(force2*cf2); // Print FSR2 force reading in Newtons
  Serial.print(", ");
  Serial.println(force3*cf); // Print FSR3 force reading in Newtons

  delay(100); // Adjust the delay as needed to control the update frequency of the readings
}

// Function to map float values
float mapfloat(float x, float in_min, float in_max, float out_min, float out_max) {
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}