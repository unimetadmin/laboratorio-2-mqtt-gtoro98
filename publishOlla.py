import ssl
import sys
import json
import random
import time
import paho.mqtt.client
import paho.mqtt.publish
import numpy as np
import datetime
from threading import Timer




def sendTemp():
    print("tempOlla")
    temp = int(np.random.uniform(0, 150))
    if temp >= 100:   
        payload = {
            "temp": temp,
            "hirviendo": True,
        }
    else:
        payload = {
            "temp": temp,
            "hirviendo": False,
        }
    print(payload)
    client.publish('casa/cocina/olla',json.dumps(payload),qos=0)
    Timer(1, sendTemp).start()


print("Hello World")
client = paho.mqtt.client.Client("Olla", False)
client.qos = 0
client.connect(host='localhost')
sendTemp()

sys.exit(0)