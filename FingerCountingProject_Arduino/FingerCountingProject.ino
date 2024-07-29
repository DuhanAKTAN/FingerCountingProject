void setup() {
  Serial.begin(9600);
  for(int i = 2; i < 7; i++) {
    pinMode(i, OUTPUT);
  }
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    int count = data.toInt();

    switch (count) {
      case 0:
        for(int i = 2; i < 7; i++) {
          digitalWrite(i, LOW);
        }
        break;
      case 1:
        digitalWrite(2, HIGH);
        for(int i = 3; i < 7; i++) {
          digitalWrite(i, LOW);
        }
        break;
      case 2:
        digitalWrite(2, HIGH);
        digitalWrite(3, HIGH);
        for(int i = 4; i < 7; i++) {
          digitalWrite(i, LOW);
        }
        break;
      case 3:
        digitalWrite(2, HIGH);
        digitalWrite(3, HIGH);
        digitalWrite(4, HIGH);
        for(int i = 5; i < 7; i++) {
          digitalWrite(i, LOW);
        }
        break;
      case 4:
        digitalWrite(2, HIGH);
        digitalWrite(3, HIGH);
        digitalWrite(4, HIGH);
        digitalWrite(5, HIGH);
        digitalWrite(6, LOW);
        break;
      case 5:
        for(int i = 2; i < 7; i++) {
          digitalWrite(i, HIGH);
        }
        break;
      default:
        for(int i = 2; i < 7; i++) {
          digitalWrite(i, LOW);
        }
        break;
    }          
  }
}
