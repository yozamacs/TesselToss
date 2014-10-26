import pygal

from Pubnub import Pubnub
pubnub = Pubnub(publish_key="pub-c-YOUR-PUBNUB-PUBLISH-KEY-HERE", subscribe_key="sub-c-YOUR-PUBNUB-SUBSCRIBE-KEY-HERE", ssl_on=False)
channel = 'lollipop'
graphData = []

def callback(message, channel):
    print(message)
    for item in message:
    	graphData.append(item)

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

import time
time.sleep(15)
pubnub.unsubscribe(channel=channel)
chartData = []
chartDataY = []
print "graph data:"
print graphData
time=0
for item in graphData:
	chartData.append((time,item[0]))
	chartDataY.append((time,item[1]))
	time+=1

print "chart data: "
print chartData
print chartDataY                                           
xy_chart = pygal.XY(stroke=True)
xy_chart.title = 'X and Y vs Time'                                        
xy_chart.add('X', chartData) 
xy_chart.add('Y', chartDataY)
xy_chart.render_to_file('XY_chart.svg')  
print "I'm done!" 
quit()                   