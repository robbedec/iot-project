import time
import psutil

# from allthingstalk import Client, Device, IntegerAsset
from allthingstalk import *

DEVICE_TOKEN = 'maker:4d2yo8gu5UyNjPNyftCm0QQ4td8vMsLZJotOtzuJ'
DEVICE_ID = 'JjQMSfUwiHeW9s47EQ2BwBgr'

class RandomDevice(Device):
    random_number = NumberAsset()

client = Client(DEVICE_TOKEN)
device = RandomDevice(client=client, id=DEVICE_ID)

counter = 1

while True:
    #device.random_number = random.randint(1, 100)

    # CPU percentage
    cpu_percent = psutil.cpu_percent()
    
    # Percentage of used RAM
    ram_percentage = psutil.virtual_memory().percent

    print(f'{counter}: Current RAM usage {ram_percentage}%')

    counter += 1
    time.sleep(5)