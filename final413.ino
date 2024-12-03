const int led1 = 9;  // Pin for Hydrangea LED
const int led2 = 10; // Pin for Strelizia Reginae LED
const int led3 = 11; // Pin for Sunflower LED
const int led4 = 12; // Pin for Fern LED
const int led5 = 13; // Pin for Orchid LED

void setup() {
    pinMode(led1, OUTPUT);
    pinMode(led2, OUTPUT);
    pinMode(led3, OUTPUT);
    pinMode(led4, OUTPUT);
    pinMode(led5, OUTPUT);
    Serial.begin(9600); // Start serial communication
}

void loop() {
    if (Serial.available()) {
        String command = Serial.readStringUntil('\n');
        
        // Turn all LEDs off initially
        digitalWrite(led1, LOW);
        digitalWrite(led2, LOW);
        digitalWrite(led3, LOW);
        digitalWrite(led4, LOW);
        digitalWrite(led5, LOW);

        if (command == "Hydrangea") {
            digitalWrite(led1, HIGH);
        } else if (command == "Strelizia Reginae") {
            digitalWrite(led2, HIGH);
        } else if (command == "Sunflower") {
            digitalWrite(led3, HIGH);
        } else if (command == "Fern") {
            digitalWrite(led4, HIGH);
        } else if (command == "Orchid") {
            digitalWrite(led5, HIGH);
        }
    }
}
