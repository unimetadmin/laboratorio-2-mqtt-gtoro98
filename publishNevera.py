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
    print("temp")
    temp = int(np.random.normal(10, 2))
    payload = {
        "temp": temp,
    }
    print(payload)
    client.publish('casa/cocina/nevera',json.dumps(payload),qos=0)
    Timer(5, sendTemp).start()

def sendHielo():
    print("hielo")
    hielo = int(np.random.uniform(0, 10))
    payloadHielo = {
        "hielo": hielo,
    }
    print(payloadHielo)
    client.publish('casa/cocina/nevera',json.dumps(payloadHielo),qos=0)
    Timer(10, sendHielo).start()


  

print("Hello World")
client = paho.mqtt.client.Client("Nevera", False)
client.qos = 0
client.connect(host='localhost')
sendHielo()
sendTemp()

sys.exit(0)