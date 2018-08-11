const electron = window.require('electron');
const fs = electron.remote.require('fs');
const ipcRenderer = electron.ipcRenderer;

// Connect to Python Backend
const zerorpc = electron.remote.require('zerorpc');
let client = new zerorpc.Client();
client.connect('tcp://127.0.0.1:4242');
load_thumbs();

// Test Backend with Echo function
export function fetchHello() {
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

function load_thumbs() {
  /*
    Load thumbs to static resource through python server
  */
  client.invoke('get_thumb', (error, res) => {
    console.log('Images Loaded');
  });
}

export function get_thumb(r) {
  /*
    Dynamically Require Thumbs
  */
  let images = {};
  r.keys().map((item, index) => {
    images[item.replace('./', '')] = r(item);
  });
  return images;
}

function parseArray(array) {
  /*
    Takes an array of JSON objects from the python server
    and parses it for javascript usage
  */
  let data = JSON.parse(array);
  data.forEach((obj, index) => {
    data[index] = JSON.parse(obj);
  });
  return data;
}

// Fetch Sessions
export function fetch_sessions() {
  let $req = new Promise((resolve, reject) => {
    client.invoke('fetch_sessions', (error, res, more) => {
      if (error) {
        reject(error);
      } else {
        let data = parseArray(res);
        console.log('Accepted', data);
        resolve(data);
      }
    });
  });
  return $req;
}

function fetchPaths() {
  /*
    Debug:
    Check Paths
  */
  let $req = new Promise((resolve, reject) => {
    client.invoke('check_dir', (error, res, more) => {
      if (error) {
        reject(error);
      } else {
        let data = res;
        console.log('Path Check: ', data);
        resolve(data);
      }
    });
  });
  return $req;
}
