#include <SoftwareSerial.h>
#include "line_notify.h"

Line_notify lineNotify;


void setup(){
    Serial.begin(115200);

    lineNotify.init("DSL-6740C-849","12345678");
    lineNotify.set_token("lKxdwgslXOi7fIN2tVhNeYG5HIBGvqIQk9G136pA4az");

}

void loop(){
    for(int i=0 ; i<10 ; i++){
        unsigned long startTime = millis();
        lineNotify.send_msg("HELLO" + String(i));
        Serial.println("[DEBUG] send_msg Time : " + String(millis() - startTime));
    }
    while (1){}
    
}
