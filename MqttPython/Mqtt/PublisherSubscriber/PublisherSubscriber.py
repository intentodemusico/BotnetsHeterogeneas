import paho.mqtt.client as mqtt
import time
broker = "iot.eclipse.org"
port = 1883
global received
global nodeId
global lastId
received=-1

nodeId=-1

heartbeat="Node "+str(nodeId)+" alive"

#Establishing new last id and setting it to node
def setNodeId(newLastId):
    global nodeId
    nodeId=newLastId
    ret= client.publish("botnet/lastId",newLastId)
    
def on_publish(client,userdata,result): 
    print("data published \n")
    pass

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")
    client.subscribe("botnet/target")
    client.subscribe("botnet/heartbeatId")
    cliente.subscribe("botnet/lastId")
    
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global received
    global lastId
    print(msg.topic+" "+str(msg.payload))
    print(" ")
    received=1
    if(msg.topic="botnet/lastId"):
        lastId=int(msg.payload)
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.connect(broker,port)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.

#Runs until it receives a message

startTime=time.time()
while(True):
    client.loop(.1)
    if(int((time.time()-startTime)%60%14)==0):
        time.sleep(1)## 15 seconds elapsed
        #print("15 seconds elapsed")
        if(received==0):
            print("No alive nodes, i'll be the master one")
            client.loop_stop()
            break
        else:
            received=0
            if(nodeId==-1):
                setNodeId(lastId+1)
                
if(nodeId==1):
    nodeId=0
    startTime=time.time()
    while(nodeId==0):
        if(int((time.time()-startTime)%60%9)==0):
            time.sleep(1)
            ret= client.publish("botnet/heartbeatId",heartbeat)
            print(ret)
