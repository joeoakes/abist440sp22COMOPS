
#include <WiFi.h>
#include <M5Core2.h>
#include <HTTPClient.h>



const char* ssid = "";  // add your wifi config.
const char* password = "";

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  M5.begin();
  WiFi.begin(ssid, password);
  int i = 0;
  while (WiFi.status() != WL_CONNECTED) {
    i++;
    delay(1000);
    Serial.print("connecting...");
    Serial.println(i);
    
  }

  Serial.println("Connected to WiFi");
  Serial.println(WiFi.localIP());
  M5.Lcd.print(WiFi.localIP());

}
void loop() {
  // put your main code here, to run repeatedly:
  M5.update();
  if (M5.BtnA.wasPressed()) {
    if (WiFi.status() == WL_CONNECTED) {
      HTTPClient http;
      http.begin("http://192.168.1.165:5000/logs"); // destination of req
      http.addHeader("Content-Type", "application/json");
      String data = "{\"app\":\"SENT FROM M5\",\"status\":\"test\",\"time\":\"test\",\"duration\":\"test\"}";
      int httpResponseCode = http.POST(data);
  
  
      if (httpResponseCode != 201){
        String response = http.getString();
  
        Serial.println(httpResponseCode);
        Serial.println(response);
      }
      else {
        Serial.print("Error: ");
        Serial.println(httpResponseCode);
      }
      http.end();
    }
    else {
      Serial.println("error with connection");
    }
  }


}
