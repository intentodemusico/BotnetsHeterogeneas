

#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>
 
void setup() {
 
  Serial.begin(115200);                                  //Serial connection
  WiFi.begin("TBGA-523188", "T1098799484");   //WiFi connection

  while (WiFi.status() != WL_CONNECTED) {  //Wait for the WiFI connection completion
 
    delay(500);
    Serial.println("Waiting for connection");
 
  }
  Serial.println("funciono");
 
}
 
void loop() {
  Serial.println("entro");
 if(WiFi.status()== WL_CONNECTED){   //Check WiFi connection status
 Serial.println("entro1");
   HTTPClient http;    //Declare object of class HTTPClient
 
   http.begin("http://jsonplaceholder.typicode.com/users/");      //Specify request destination
   http.addHeader("Content-Type", "text/plain");  //Specify content-type header
 
   int httpCode = http.POST("Message from ESP8266");   //Send the request
   String payload = http.getString();                  //Get the response payload
 
   Serial.println(httpCode);   //Print HTTP return code
   Serial.println(payload);    //Print request response payload
 
   http.end();  //Close connection
 
 }else{
 
    Serial.println("Error in WiFi connection");   
 
 }
 
  delay(3000);  //Send a request every 3 seconds
 
}
