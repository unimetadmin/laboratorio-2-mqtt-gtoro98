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




def sendCant():
    print("Cant Sala")
    cant_personas = int(np.random.uniform(0, 10))
    if cant_personas >= 5:   
        payload = {
            "cant_personas": cant_personas,
            "alerta": True,
        }
    else:
        payload = {
            "cant_personas": cant_personas,
            "alerta": False,
        }
    print(payload)
    client.publish('casa/sala/contador',json.dumps(payload),qos=0)
    Timer(5, sendCant).start()


print("Hello World")
client = paho.mqtt.client.Client("Contador", False)
client.qos = 0
client.connect(host='localhost')
sendCant()

sys.exit(0)