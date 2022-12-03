
char a;
int LED = 10;

void setup() {
  Serial.begin(9600);
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  if(Serial.available()>0){
    a = Serial.read();
    if(a=='H'){
      Serial.println(a);
      digitalWrite(LED, HIGH); 
    }
    if(a=='L'){
      digitalWrite(LED, LOW); 
      Serial.println(a);
      }
    }
               
}
