#define BUFF_LENGTH 8
#define BUFF_CHARS 6

byte number = 0;
char serialBuffer[BUFF_LENGTH] = {32,32,32,32,32,32,'\n','\0'};
unsigned char counter = 0;
unsigned char checkTermination(char * serBuff,unsigned char lngth) {
  unsigned char i = (lngth-1);
  unsigned char done = 0;
  while((i > 0))  {
    if(serBuff[i] == '9' || serBuff[i] == '8') {
      if((serBuff[i] & serBuff[i-1] & serBuff[i-2]) == '9'||
          (serBuff[i]   == '8' && 
           serBuff[i-1] == '8' && 
           serBuff[i-2] == '8')) {
        return 1;
      }
      else {
        return 0;
      }  
    }
    i--;
  }
  return 0;
}

void flushBuffer() {
  char resetBuff[BUFF_LENGTH] = {32,32,32,32,32,32,'\n','\0'};
  for(int x = 0;x < BUFF_LENGTH; x++) {
    serialBuffer[x] = resetBuff[x];  
  }
}

void setup() {
  Serial.begin(9600);
}

void loop() {
  if(checkTermination(serialBuffer,BUFF_LENGTH)) {
    Serial.print(serialBuffer);

    //write function to handle data in serialBuffer[] here

    counter = 0;
    flushBuffer();  
  }
  if(counter >= BUFF_CHARS) {
    counter = 0;
    flushBuffer();  
  }
  if(Serial.available()) {
    number = Serial.read();
    serialBuffer[counter] = number;
    counter++;
  }
}
