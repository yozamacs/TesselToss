TesselToss
===========
PubNub + Tessel Hack Day 2014
-----------------------------
[<img src="http://www.pubnub.com/static/images/structure/pubnub.png" alt="PubNub" style="height:50px">](http://pubnub.com)


[<img src="https://s3.amazonaws.com/technicalmachine-assets/technical-io/tessel-logo-horizontal.svg" alt="Tessel" style="height:64px">
](http://tessel.io)

What it is
--------

The TesselToss is a microcontroller-powered ball with an accelerometer inside for easy physics lab experiments. Throw the ball, and the (x,y,z) position data gets published to PubNub. TesselToss subscribes to the PubNub channel and plots the data. Students can access the data to measure gravity, coefficients for projectile motion, among other physical properties.

Winner of the Grand Prize at the Tessel-PubNub Hackathon.  Built by The Tessellation of Smaug.

Usage
------------

### PubNub
Set up a new project and get the API keys, both subscribe and publish. Also pick a channel name to use throughout this project.

More info is available on the PubNub website.  
[Quick Start - PubNub](http://www.pubnub.com/developers/quick-start/)

### Tessel
Install Tessel CLI with npm globally (if not installed):  
`$ npm install tessel -g`

__Once connected to WiFi [(see Tessel docs)](http://start.tessel.io/wifi):__

Use `tessel run publish_xyz.js` to run while connected via USB. Note that the entire directory will be bundled and copied to the runtime filesystem.

`tessel push publish_xyz.js` will save the code to the filesystem and automatically run it in startup, regardless of whether it is plugged into the computer.

`tessel erase` will wipe the filesystem.

### TesselToss

Replace channel name, publish, and suscribe keys with your personal ones. Make sure that Tessel is connected to battery and wifi. Wrap Tessel in paper towels or other material for protection. 

Make sure that channel is connected before throwing the Tessel. Run python program and throw Tessel across a short distance at the same time. You can change the data collection time by changing the dataCollectionInterval in graphy.py. 

After data collection, the program will print "I'm done" to the terminal, and you can see the graph of the X and Y coordinates by opening the XY_chart.svg file in a web browser on your computer.

Installation
------------

Clone this repo using Git:  
`$ git clone https://github.com/yozamacs/TesselToss.git`

License
-------
The MIT License (MIT)

Copyright (c) 2014 Tesselation of Smaug

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
