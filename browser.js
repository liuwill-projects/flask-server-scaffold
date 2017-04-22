// socket.io demo
var scriptNode = document.createElement("script")
scriptNode.type = "text/javascript"

scriptNode.src = '//cdnjs.cloudflare.com/ajax/libs/socket.io/1.3.6/socket.io.min.js'

scriptNode.onload = function(){
  var socket = io.connect('http://localhost:5000/chat');
  socket.on('connect', function() {
      socket.emit('my event', {data: 'I\'m connected!'});
  });

  socket.on('my response', function(msg) {
      console.log('<p>Received: ' + msg.data + '</p>');
  });

  window.mySocket = socket
}

document.body.appendChild(scriptNode)

// websocket demo
const ws = new WebSocket('ws://localhost:8080/chat');

ws.on('open', function open() {
  ws.send('my event');
});

ws.on('my response', function incoming(data, flags) {
  console.log('<p>Received: ' + data + '</p>');
  // flags.binary will be set if a binary data is received.
  // flags.masked will be set if the data was masked.
});
