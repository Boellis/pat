#pip install phue
#Check Ip address for Hue Bridge: https://www.meethue.com/api/nupnp
from phue import Bridge
myBridge = Bridge('192.168.1.94')

myBridge.connect()


#print(myBridge.get_api())
lights = myBridge.lights

for l in lights:
    #if l.name == "Hue color lamp 1":
    #    l.on = False
    print(l.name)
    l.on = True
