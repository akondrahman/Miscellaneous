var redis = require('redis')
var multer  = require('multer')
var express = require('express')
var fs      = require('fs')
var app = express();
var httpProxy = require('http-proxy');
var uploadDone = false ;
var http = require('http');

var stack = [] ;
var port1 = 3001 ;
var port2 = 3002 ;
var originalPort = 3000;
var visitedUrls="";




///////////// WEB ROUTES

// Add hook to make it easier to get all visited URLS.
var app = express();

app.get('/', function (req, res) {
  res.send('Hello World! <br /> This is the index page');
});



var server1 = app.listen(port1, function () {

    var host1 = server1.address().address ;
    var port1 = server1.address().port ; 

    console.log('Echoing from http://%s:%s', host1, port1) ;
});

var server2 = app.listen(port2, function () {

    var host2 = server2.address().address ;
    var port2 = server2.address().port ; 

    console.log('Echoing from http://%s:%s', host2, port2) ;
});





app.use(function(req, res, next) 
{
	console.log(req.method, req.url);
    next(); // Passing the request to the next handler in the stack.
});



var addresses = [
  {
    host: 'localhost',
    port: 3001
  },
  {
    host: 'localhost',
    port: 3002
  }
];
var proxy = httpProxy.createServer();

http.createServer(function (req, res) {
  var target = { target: addresses.shift() };

  console.log('balancing request to: ', target);
  proxy.web(req, res, target);

  addresses.push(target.target);
}).listen(originalPort);



// REDIS
var redisServer = 'localhost';
var redisPort = 6379;
var client = redis.createClient( redisPort, redisServer, {});





app.all('/set', function(req, res) {

        client.set('expire_key', 'This Message Will Self-destruct in 10 Seconds', function(err, reply) {
        console.log(reply);
        client.expire('expire_key', 120);
        res.send('A key that expires after 10 seconds is set ... <br /> Status: ' + reply );
    });


});


app.get('/get', function(req, res) {

    client.get('expire_key', function(err, reply) {
        console.log(reply);
        res.send('hello world  ! <br /> It is reply time now: ' + reply ); 
    });

    
});

app.use(function(req, res, next){

    console.log('What does request have ' + req['url']);
    //console.log(Object.getOwnPropertyNames(req).sort());
    client.lpush("vistedUrl", req['url'], function(err, reply){ 
        //console.log(reply); 
    });
    next();

});

app.get('/recent', function(req, res) {

    var messageList = client.lrange("vistedUrl", 0, 5, function(err, messages){
        console.log(messages);
        res.send('Visited websites <br />' + messages  );
        
        
    });

});


app.use(multer({ dest: './uploads/',
 rename: function (fieldname, filename) {
    return filename+Date.now();
  },
onFileUploadStart: function (file) {
  console.log(file.originalname + ' is starting ...')
},
onFileUploadComplete: function (file) {
  console.log(file.fieldname + ' uploaded to  ' + file.path)
  uploadDone=true;
    
  stack.push(file);
  console.log("The stack is " +  stack ) ;
    
}
}));

app.post('/photo',function(req,res){
  if(uploadDone==true){
    console.log(req.files);
    res.end("File uploaded.");
  }
});

app.get('/upload',function(req,res){
      res.sendfile("upload.html");
});

// static upload ...  needed 
app.use("/uploads", express.static(__dirname + '/uploads'));



app.get('/meow', function(req, res) {
 	{
 		//if (err) throw err
        console.log(req.files);
 		res.writeHead(200, {'content-type':'text/html'});
        
        var getFile =    stack.pop() ;
        var pathOfFile = getFile.path ;
        console.log('Original name of the file ' + getFile.originalname);
        console.log('Path of the file ' + pathOfFile);
        console.log('Current name of the file ' + getFile.name);
        res.write("<strong>Here is the recent image for you : </strong>");
        res.write("<br />");        
        res.write("<h1><image src='./"+ pathOfFile +"'></image></h1>");
        
    	res.end();
 	}
 });


