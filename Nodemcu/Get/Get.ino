

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

 if(WiFi.status()== WL_CONNECTED){   //Check WiFi connection status
 Serial.println("gg");
   HTTPClient http;    //Declare object of class HTTPClient
 
   http.begin("http://jsonplaceholder.typicode.com/comments?id=10");      //Specify request destination

 
   int httpCode = http.GET();   //Send the request

// This code is only necessary when you need information about the web, ie the page will respond with the request you made, in this case we will only try to attack it
//------------------------------------------------------------------
   String payload = http.getString();                  //Get the response payload
 
   Serial.println(httpCode);   //Print HTTP return code
   Serial.println(payload);    //Print request response payload
//-------------------------------------------------------------------- 
   http.end();  //Close connection
 
 }else{
 
    Serial.println("Error in WiFi connection");   
 
 }
 
  delay(3000);  //Send a request every 3 seconds
 
}
