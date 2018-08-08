const electron = window.require('electron');
const fs = electron.remote.require('fs');
const ipcRenderer = electron.ipcRenderer;

// Connect to Python Backend
const zerorpc = electron.remote.require('zerorpc');
let client = new zerorpc.Client();
client.connect('tcp://127.0.0.1:4242');

// Test Backend with Echo function
export function fetchHello() {
  let resp;
  let $req = new Promise((resolve, reject) => {
    client.invoke('echo', 'ready', (error, res) => {
      if (error || res !== 'ready') {
        console.log('Python backend connection failed.');
        console.log('Error: ', error);
        reject(error);
      } else {
        resolve(res);
      }
    });
  });
  return $req;
}
