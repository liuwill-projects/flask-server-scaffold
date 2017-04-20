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
}

document.body.appendChild(scriptNode)
