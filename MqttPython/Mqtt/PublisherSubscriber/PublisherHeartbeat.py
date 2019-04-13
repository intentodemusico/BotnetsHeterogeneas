import paho.mqtt.client as paho
import time

broker="iot.eclipse.org"
port=1883
#target=input("Target: ") #attack direction
#create function for callback
nodeId=-1

heartbeat="Node "+str(nodeId)+" alive"
def on_publish(client,userdata,result): 
    print("data published \n")
    pass

#create client object
client= paho.Client("botnetcontroller")

#assign function to callback
client.on_publish = on_publish

#establish connection
client.connect(broker,port)

#publish

#ret= client1.publish("botnet/target",target)
#print(ret)

startTime=time.time()
while(nodeId==-1):
    if(int((time.time()-startTime)%60%9)==0):
        time.sleep(1)
        ret= client1.publish("botnet/heartbeatId",heartbeat)
        print(ret)
