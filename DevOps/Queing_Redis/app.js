var redis = require('redis');
var express = require('express');
var client = redis.createClient(); //creates a new client 

var port = 6379;
var host = "localhost";
var client = redis.createClient(port, host);

client.on('connect', function() {
    console.log('client is connected to' +host +'@ port: ' +  port);
});

client.set('name', 'AKOND', function(err, reply) {
  console.log(reply);
});

/*name is the key, AKOND is the value*/

client.get('name', function(err, reply) {
    console.log(reply);
});

client.exists('name', function(err, reply) {
    if (reply === 1) {
        console.log('The key name exists');
    } else {
        console.log('They key name doesn\'t exist');
    }
});


client.set('expire_key', 'this message will self-destruct in 10 seconds');
client.expire('expire_key', 10);
client.get('expire_key', function(err, reply) {
    console.log(reply);
});

/*

var app = express();
var server = app.listen(3000, function () {

  var host = server.address().address
  var port = server.address().port

  console.log('Example app listening at http://%s:%s', host, port)
})


app.get('/', function(req, res) {
  res.send('hello world from app.js !')
})

*/