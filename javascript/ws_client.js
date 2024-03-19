const WebSocket = require('ws');

const ws = new WebSocket('ws://10.10.4.133:8080');

ws.on('open', function open() {
  console.log('Connected to the WebSocket server');
  ws.send('Hello, server!');
});

ws.on('message', function incoming(data) {
  console.log('Received: %s', data);
});

ws.on('close', function close() {
  console.log('Disconnected from the WebSocket server');
});
