var scriptNode = document.createElement("script")
scriptNode.type = "text/javascript"

scriptNode.src = '//cdnjs.cloudflare.com/ajax/libs/socket.io/1.3.6/socket.io.min.js'

scriptNode.onload = function(){
  var socket = io.connect('http://localhost:5000');
    socket.on('connect', function() {
        socket.emit('my event', {data: 'I\'m connected!'});
    });
}

document.body.appendChild(scriptNode)
