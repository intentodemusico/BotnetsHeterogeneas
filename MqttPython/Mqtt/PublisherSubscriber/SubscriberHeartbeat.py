import paho.mqtt.client as mqtt
import time
broker = "iot.eclipse.org"
port = 1883
global received
received=-1
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")
    client.subscribe("botnet/target")
    client.subscribe("botnet/heartbeatId")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    print(" ")
    global received
    received=1
    client.loop_stop()
    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker,port)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.

#Runs until it receives a message

#client.loop_start()
startTime=time.time()
while(True):
    client.loop(.1)
    if(int((time.time()-startTime)%60%14)==0):
        time.sleep(1)## 15 seconds elapsed
        print("15 seconds elapsed")
        if(received==0):
            print("Vemos, no hay nadie vivo")
            client.loop_stop()
            break
        else:
            received=0
