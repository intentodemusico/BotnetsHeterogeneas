//code write by Moz for YouTube changel logMaker360, 24-11-2016
//code belongs to this video: https://youtu.be/nAUUdbUkJEI

//#include <EEPROM.h>
#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <Wire.h>
//#include <Adafruit_INA219.h>
#include <Time.h> 
 
// Connect to the WiFi
const char* ssid = "AndroidAP";                           //!!!!!!!!!!!!!!!!!!!!!
const char* password = "12345678";                //!!!!!!!!!!!!!!!!!!!!!
const char* mqtt_server = "iot.eclipse.org";                 //!!!!!!!!!!!!!!!!!!!!!
//------

 int target=0;
 int received=-1;
 int lastId=-555;
 int nodeId=-1;
int status = WL_IDLE_STATUS;
WiFiClient espClient;
PubSubClient client(espClient);



 
const byte ledPin = 2; // 
int on_publish (char* topic, byte* payload)
{
  Serial.print("data published");
  }
 boolean on_connectm(char* clientId){
  
 Serial.print("Connected with result code ");
    client.subscribe("botnet/target");
    client.subscribe("botnet/lastId");
    client.unsubscribe("botnet/heartbeat");
}
  boolean on_connectsc(char* clientId){
 Serial.print("Connected with result code ");
 client.subscribe("botnet/heartbeat");
}

void on_messagem(char* topic, byte* payload, unsigned int length){
  received=1;
  for (int i=0;i<length;i++) {
  char receivedChar = (char)payload[i];
  
  Serial.print(topic+' '+receivedChar);
  char* var="botnet/lastId";

  Serial.println(lastId!=String(receivedChar).toInt());

  
  if(String(topic)==String(var) and lastId!=String(receivedChar).toInt())
  {

    lastId=receivedChar;


    Serial.println("New local last id: ");
     Serial.print(lastId);
    
   
  }
  if(String(topic)==String(var))
  {
    target=receivedChar;
    Serial.println("New local target: ");
    Serial.print(target);
  }
    
  }
  }


void on_messagesc(char* topic, byte* payload, unsigned int length){
  received=1;
  
   for (int i=0;i<length;i++) {
  char receivedChar = (char)payload[i];
  Serial.print(topic+' '+receivedChar);
  char* var="botnet/heartbeat";
  if(String(topic)==String(var) and lastId!=String(receivedChar).toInt())
  {
    lastId=receivedChar;
    char * hola=" ";
    sprintf(hola,"New local last id: %i",lastId);
    Serial.print(hola);
  }
  if(String(topic)==String(var) && lastId!=0)
  {
    target=receivedChar;
    attack();
  }
    
  }
  }
boolean isSlave()
{
  return nodeId==1;
  }

boolean isReceived()
{
  return received==1;
  }
void attack()
{
  unsigned long time1 = 0;
  unsigned long tiempo2 = 1000;
  unsigned long tiempo3 = 0;

  time1=millis();
  while(true)
  {
    client.loop();
    if(((millis()-time1)/tiempo2)==0)
    {
      Serial.println("Attacking");
      if(target==0)
      {
        break;
        return;
        }
        time1=millis();
      }
    }
   
  }
void slave()
{
   Serial.print("I'm slave");
 //  client.connect(on_connectsc);
 //------------------------------------------
 // client.connect("ESP8266 Client");
  client.subscribe("botnet/heartbeat");
  //-----------------------------------
    client.setCallback(on_messagesc);
  //  client.publish(on_publish);
  
    client.setServer(mqtt_server, 1883);
    unsigned long  tiempo1 = 0;
    tiempo1=millis();
    delay(1000);
    while(nodeId==1)
    {
      client.loop();
      if((((millis()-tiempo1))/1000%2)==0)
      {
        tiempo1=millis();
        if(not isReceived())
        {
          nodeId-=1;
          master();
          }
        }
      
      
      }
  }
void master()
{
  Serial.println("I'm master");
  const char * clienteId;
 // client.connect(on_connectm);
 //-----------------------------------
 // client.connect("ESP8266 Client");
   client.subscribe("botnet/target");
    client.subscribe("botnet/lastId");
    client.unsubscribe("botnet/heartbeat");
     //-----------------------------------
    client.setCallback(on_messagem);
   // client.publish(on_publish);
    client.setServer(mqtt_server, 1883);
   unsigned long  tiempo1 = 0;
       if(nodeId==-2)
    {
      lastId=-1;
      nodeId=0;
       }
    if(nodeId==-1)
    {
      lastId=0;
      nodeId=0;
       }
      tiempo1=millis();

      
      while(nodeId==0)
      {

        client.loop();
      
        if((((millis()-tiempo1))/1000%1)==0)
        {

          tiempo1=millis();
          //delay(1000);
       
          char* hola=" ";
          Serial.println(target);
          //Serial.println(atoi((const char*)lastId));
          
          sprintf(hola,"%i %i",(int)target,(int)lastId);
          Serial.print("Target y Last id: ");
         Serial.println(hola);
          client.publish("botnet/heartbeat",hola);
    
           //Serial.print("Last id:"+lastId);
          // Serial.print(ret);
          }
          delay(500);
        
        }
      
     
  
  }
void common()
{
  Serial.println("I'm common");
    char * clienteId;
//    client.connect(on_connectsc);
 client.setCallback(on_messagesc);
  client.setServer(mqtt_server, 1883);
 while (!client.connected()) {
 if (client.connect("ESP8266 Client")) {
 
    //------------------------------------------
  client.subscribe("botnet/heartbeat");
  //-----------------------------------
 }
 }
   
//    client.publish(on_publish);
   
     unsigned long  tiempo1 = 0;
    tiempo1=millis();
    delay(1000);
    while(true)
    {
      client.loop();
      if(((millis()-tiempo1)/1000%14)==0)
      {
        delay(1000);
        if(nodeId==-1 && isReceived())
        {
          nodeId=lastId+1;
          Serial.println("common: ");
          Serial.print((const char*)nodeId);
          Serial.println(nodeId);
          client.publish("botnet/lastId",(const char*)nodeId);
          }
        if(not isReceived() and nodeId==-1)
        {
          master();
          }
         if(isReceived())
         {
          received=0;
          
          }
          if(isSlave())
          {
            slave();
            }

         else
         {
          nodeId-=1;
          lastId-=1;
          
          }
        }
      
      }
  
  }

 /*
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
}*/
 
void setup()
{
 Serial.begin(115200);

// status = WiFi.begin(ssid, password);
// if ( status != WL_CONNECTED) { 
//    Serial.println("Couldn't get a wifi connection");
//    // don't do anything else:
//    while(true);
//  } 
 client.setServer(mqtt_server, 1883);
 //client.setCallback(callback);
 
 pinMode(ledPin, OUTPUT);
 digitalWrite(ledPin, HIGH);
 delay(5000);
 digitalWrite(ledPin, LOW);
}
 
void loop()
{
 
 if (!client.connected()) {
  Serial.println("conectando");
  common();
  //reconnect();
  
 }
 Serial.println("salió");
 client.loop();
}
void reconnect() {
 // Loop until we're reconnected
 while (!client.connected()) {
 Serial.print("Attempting MQTT connection...");
 // Attempt to connect
 if (client.connect("ESP8266 Client")) {
  Serial.println("connected");
  // ... and subscribe to topic
  //client.subscribe("ledStatus");
 } else {
  Serial.print("failed, rc=");
  Serial.print(client.state());
  Serial.println(" try again in 5 seconds");
  // Wait 5 seconds before retrying
  delay(5000);
  }
 }
}
