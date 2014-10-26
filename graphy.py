import pygal
import time
from Pubnub import Pubnub

pubnub = Pubnub(publish_key="pub-c-YOUR-PUBNUB-PUBLISH-KEY-HERE", subscribe_key="sub-c-YOUR-PUBNUB-SUBSCRIBE-KEY-HERE", ssl_on=False)
channel = 'YOUR-CHANNEL-NAME-HERE'
rawData = []

def callback(message, channel):
    for item in message:
        rawData.append(item)

def error(message):
    print("ERROR : " + str(message))

def connect(message):
    print("CONNECTED")


def reconnect(message):
    print("RECONNECTED")


def disconnect(message):
    print("DISCONNECTED")

pubnub.subscribe(channel, callback=callback, error=callback,
                 connect=connect, reconnect=reconnect, disconnect=disconnect)  


dataCollectionInterval = 15
time.sleep(dataCollectionInterval)
pubnub.unsubscribe(channel=channel)

print "Raw data:"
print rawData


time=0
chartDataX = []
chartDataY = []

for item in rawData:
    chartDataX.append((time,item[0]))
    chartDataY.append((time,item[1]))
    time+=1

print "chart data: "
print chartDataX
print chartDataY  

xy_chart = pygal.XY(stroke=True)
xy_chart.title = 'X and Y vs Time'                                        
xy_chart.add('X', chartDataX) 
xy_chart.add('Y', chartDataY)
xy_chart.render_to_file('XY_chart.svg')  
print "I'm done!" 
quit()                   