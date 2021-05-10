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


cant_agua = 100
cont = 0

def sendReport():
    global cant_agua, cont
    sale_agua = int(np.random.normal(0.10*cant_agua, 0.05*cant_agua))
    entra_agua = 0
    print(cont)
    cont += 1
    if cont == 3:
        entra_agua = int(np.random.normal(20, 5))
        cont = 0
    
    cant_agua = cant_agua + entra_agua - sale_agua

    if cant_agua > 100:
        cant_agua = 100
    if cant_agua < 0:
        cant_agua = 0

    if cant_agua > 50:   
        payload = {
            "cant_agua": cant_agua,
            "mitad_tanque": False,
            "tanque_vacio": False
        }
    elif cant_agua <= 0:
        payload = {
            "cant_agua": cant_agua,
            "mitad_tanque": True,
            "tanque_vacio":True
        }

    else:
        payload = {
            "cant_agua": cant_agua,
            "mitad_tanque": True,
            "tanque_vacio": False
        }
    print(payload)
    client.publish('casa/bano/tanque',json.dumps(payload),qos=0)
    Timer(10, sendReport).start()


print("Hello World")
client = paho.mqtt.client.Client("Tanque", False)
client.qos = 0
client.connect(host='localhost')
sendReport()

sys.exit(0)