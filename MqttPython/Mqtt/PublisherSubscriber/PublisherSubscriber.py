import paho.mqtt.client as mqtt
import time
broker = "iot.eclipse.org"
port = 1883
global received
global nodeId
global lastId
received=-1
lastId=-555
nodeId=-1
restas=0

heartbeat="Node "+str(nodeId)+" alive"

#Establishing new last id and setting it to node
def setNodeId(newLastId):
    global nodeId
    nodeId=newLastId
    print("Node id:",newLastId)
    ret= client.publish("botnet/lastId",nodeId)
    
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
    client.subscribe("botnet/lastId")
    
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global received
    global lastId
    print(msg.topic+" "+str(msg.payload))
    print(" ")
    received=1
    if(msg.topic=="botnet/lastId" and lastId!=int(msg.payload)):
        lastId=int(msg.payload)
        print("New local last id:",lastId)
        
    
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

#
startTime=time.time()
while(True):
    client.loop(.1)
    #print("Mi id",nodeId)
    if(int((time.time()-startTime)%60%16)==0):
        time.sleep(1)## 15 seconds elapsed
        #print("15 seconds elapsed")

        
        # if(nodeId==-1 and received==1):   
        #     setNodeId(lastId+1)
        # if(received==0):
        #     print("No alive nodes, i'll be the master one")
        #     #client.loop_stop()
        #     break
        # else:
        #     received=0

        if(received==1):
            print("Id",nodeId,"lastId",lastId)
            if(nodeId<=-1):  
                setNodeId(lastId+1)
        elif(nodeId<=1 and received==0): #Fixiable
            print("No alive nodes, i'll be the master one")
            #client.loop_stop()
            break
        else:
            nodeId-=1
            lastId-=1
            restas+=1
            print("NodeId--",nodeId,"restas",restas)
        received=0
        #Control de errores?
        if(nodeId>lastId):
            nodeId-=1#?

#Node take leadership of the botnet                
if(nodeId<=-1):
    lastId=0
else:
    restas+=1
    lastId-=1
nodeId=0
startTime=time.time()

while(nodeId==0):
    client.loop(.1)
    if(int((time.time()-startTime)%60%10)==0):
        time.sleep(1)
        #ret= client.publish("botnet/heartbeatId",heartbeat)
        ret= client.publish("botnet/lastId",lastId)
        print("Last id:",lastId)
        print(ret)
