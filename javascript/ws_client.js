const WebSocket = require('ws');

const ws = new WebSocket('ws://localhost:8080');

const jsonData = {
  // "dmms_m": [
  //     {
  //         "device_id_m": 1,
  //         "t_year_m": 2024,
  //         "t_month_m": 3,
  //         // 其他字段请根据实际情况填写
  //     }
  // ]
  "is_ok": 1
};

ws.on('open', function open() {
  console.log('Connected to the WebSocket server');
  // ws.send('Hello, server!');
  ws.send(JSON.stringify(jsonData));
});

ws.on('message', function incoming(data) {
  console.log('Received: %s', data);
});

ws.on('close', function close() {
  console.log('Disconnected from the WebSocket server');
});
