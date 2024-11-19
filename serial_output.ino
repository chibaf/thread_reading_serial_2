const int na=100;
float a[na],b[na];

void setup() {
  // initialize serial comms
  Serial.begin(19200);
}

  int i=0;
  float pi=3.1415;

//// print signals
void loop() {
  i=i+1;
  i=i % 100;
  Serial.println(sin(2.0*i*0.01*pi));
  delay(10);
}
