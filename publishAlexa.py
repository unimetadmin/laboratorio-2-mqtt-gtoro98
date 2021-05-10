import ssl
import sys
import json
import random
import time
import paho.mqtt.client
import paho.mqtt.publish
import numpy as np
import datetime
import requests
from threading import Timer




def sendTemp():
    print("Temp Caracas")
    temp = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Caracas&APPID=4d214b29a2e5ef7a38fe3c6eeb5ed478')
  
    payload = {
        "temp": temp.json()['main']['temp']-273.15,
    }
    print(payload)
    client.publish('casa/sala/alexa',json.dumps(payload),qos=0)
    Timer(5, sendTemp).start()



client = paho.mqtt.client.Client("Alexa", False)
client.qos = 0
client.connect(host='localhost')
sendTemp()

sys.exit(0)