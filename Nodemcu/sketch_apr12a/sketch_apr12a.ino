//code write by Moz for YouTube changel logMaker360, 24-11-2016
//code belongs to this video: https://youtu.be/nAUUdbUkJEI

//#include <EEPROM.h>
#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <Wire.h>
#include <Adafruit_INA219.h>

//Angarita
// Connect to the WiFi
//const char* ssid = "TBGA-523188";                           //!!!!!!!!!!!!!!!!!!!!!
//const char* password = "T1098799484";                //!!!!!!!!!!!!!!!!!!!!!

//Alberto
const char* ssid = "system"; // Rellena con el nombre de tu red WiFi
const char* password = "1nformatica"; // Rellena con la contraseña de tu red WiFi
 
const char* mqtt_server = "iot.eclipse.org";                 //!!!!!!!!!!!!!!!!!!!!!
 
WiFiClient espClient;
PubSubClient client(espClient);
 
const byte ledPin = 2; // 
 
void callback(char* topic, byte* payload, unsigned int length) {
 Serial.print("Message arrived [");
 Serial.print(topic);
 Serial.print("] ");
 for (int i=0;i<length;i++) {
  char receivedChar = (char)payload[i];
  Serial.print(receivedChar);
  if (receivedChar == '1')
  digitalWrite(ledPin, HIGH);
  if (receivedChar == '0')
   digitalWrite(ledPin, LOW);
  }
  Serial.println();
}
 
 
void reconnect() {
 // Loop until we're reconnected
 while (!client.connected()) {
 Serial.print("Attempting MQTT connection...");
 // Attempt to connect
 if (client.connect("ESP8266 Client")) {
  Serial.println("connected");
  // ... and subscribe to topic
  client.subscribe("ledStatus");
 } else {
  Serial.print("failed, rc=");
  Serial.print(client.state());
  Serial.println(" try again in 5 seconds");
  // Wait 5 seconds before retrying
  delay(5000);
  }
 }
}
 
void setup()
{
 Serial.begin(9600);
 
 client.setServer(mqtt_server, 1883);
 client.setCallback(callback);
 
 pinMode(ledPin, OUTPUT);
 digitalWrite(ledPin, HIGH);
 delay(5000);
 digitalWrite(ledPin, LOW);
}
 
void loop()
{
 if (!client.connected()) {
  reconnect();
 }
 client.loop();
}
