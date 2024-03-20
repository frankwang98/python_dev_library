const WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 8080 });

const jsonData = {
  "dmms_m": [
      {
          "device_id_m": 1,
          "t_year_m": 2024,
          "t_month_m": 3,
          // 其他字段请根据实际情况填写
      }
  ]
};

wss.on('connection', function connection(ws) {
  console.log('A new client connected');

  ws.on('message', function incoming(message) {
    console.log('Received: %s', message);
  });

  // ws.send('Hello, client!');
  ws.send(JSON.stringify(jsonData));
});
