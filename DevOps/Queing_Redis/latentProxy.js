var util = require('util'),
    colors = require('colors'),
    http = require('http'),
    httpProxy = require('http-proxy');

//
// Http Proxy Server with Latency
//
var proxy = httpProxy.createProxyServer();
http.createServer(function (req, res) {
  setTimeout(function () {
    proxy.web(req, res, {
      target: 'http://localhost:9008'
    });
  }, 500);
}).listen(8008);

//
// Target Http Server
//
http.createServer(function (req, res) {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.write('request successfully proxied to: ' + req.url + '\n' + JSON.stringify(req.headers, true, 2));
  res.end();
}).listen(9008);

util.puts('http proxy server '.blue + 'started '.green.bold + 'on port '.blue + '8008 '.yellow + 'with latency'.magenta.underline);
util.puts('http server '.blue + 'started '.green.bold + 'on port '.blue + '9008 '.yellow);