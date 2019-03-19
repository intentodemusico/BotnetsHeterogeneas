import paho.mqtt.client as paho
import random 

broker="iot.eclipse.org"
port=1883

#create function for callback
def on_publish(client,userdata,result): 
    print("data published \n")
    pass

#create client object
client1= paho.Client("potcontroller")

#assign function to callback
client1.on_publish = on_publish

#establish connection
client1.connect(broker,port)

#publish
ret= client1.publish("pot/temperatura",random.randint(10, 40))
print(ret)
