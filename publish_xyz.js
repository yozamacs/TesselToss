(function() {
  var PUBNUB, accel, accellib, tessel, pubChannel, pubBuffer, benchStart, bench;
  benchStart = Date.now();
  bench = function(ev){
    console.log((Date.now() - benchStart) + 'ms: '+ev);
  };

  tessel = require('tessel');
  bench('required tessel');

  accellib = require('accel-mma84');
  bench('required accel');

  accel = accellib.use(tessel.port['A']);
  bench('accel port link');

  PUBNUB = require("pubnub-hackathon").init({
    publish_key: "pub-c-YOUR-PUBNUB-PUBLISH-KEY-HERE",
    subscribe_key: "sub-c-YOUR-PUBNUB-SUBSCRIBE-KEY-HERE"
  });
  pubChannel = 'YOUR-CHANNEL-NAME-HERE'; // change this

  bench('pubnubz');

  pubBuffer = [];

  accel.on('ready', function(version) {
    bench('on ready called');

    accel.removeAllListeners('data');
    bench('data listeners removed');

    accel.setOutputRate(1, function() {
      bench('output rate set');

      accel.on('data', function(xyz) {
        bench('data recieved');

        console.log('xyz:', JSON.stringify(xyz));
        pubBuffer.push(xyz);
        if (pubBuffer.length >= 3){
          PUBNUB.publish({
            channel: pubChannel,
            message: pubBuffer
          });
          bench('published');

          pubBuffer = [];
        }
        else{
          bench('buffered XYZ');
        }
      });
    });
  });
  bench('accell on ready set');

  accel.on('error', function(err) {
    return console.error(err);
  });
  bench('error handler set');

})();