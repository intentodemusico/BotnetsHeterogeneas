import paho.mqtt.publish as publish
import time
while 1==1:
   print("Sending 1...")
   publish.single("ledStatus", "1", hostname="iot.eclipse.org")
   time.sleep(6)
   print("Sending 0...")
   publish.single("ledStatus", "0", hostname="iot.eclipse.org")
   time.sleep(3)
