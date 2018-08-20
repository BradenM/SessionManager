const electron = window.require('electron');

// Connect to Python Backend
const zerorpc = electron.remote.require('zerorpc');
let client = new zerorpc.Client({ timeout: 90000, heartbeatInterval: 60000 });
client.connect('tcp://127.0.0.1:4242');

export function load_thumbs() {
  /*
    Load thumbs to static resource through python server
  */
  return new Promise(resolve => {
    client.invoke('get_thumb', (error, res) => {
      console.log('Images Loaded');
      console.log('TH Error: ', error);
      console.log(('TH RES:', res));
      resolve(res);
    });
  });
}

export function get_thumb(r) {
  /*
    Dynamically Require Thumbs
  */
  let images = {};
  r.keys().map(item => {
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
    client.invoke('fetch_sessions', (error, res) => {
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

// Create Session
export function create_session(obj) {
  console.log('OBJ: ', obj);
  let request = JSON.stringify(obj);
  let $req = new Promise((resolve, reject) => {
    client.invoke('create_session', request, (error, res, more) => {
      if (error) {
        console.log('INVOKE ERROR');
        reject(error);
      } else {
        resolve(res);
      }
    });
  });
  return $req;
}

export function get_prog(request, callback) {
  client.invoke('session_callback', request, (error, res, more) => {
    if (error) {
      console.log('COPY ERROR', error);
    }
    callback(res);
  });
}
