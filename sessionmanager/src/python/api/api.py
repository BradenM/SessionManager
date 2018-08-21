import gevent
import sys
import zerorpc
import json
from pathlib import Path
from manage.session import Session
from shutil import copy


class Api(object):
    def __init__(self):
        self.progress = {
            'copy': 0,
            'convert': 0
        }
        self.copied = []

    def get_thumb(self):
        web_img = Path.cwd() / 'src' / 'imgs' / 'thumb'
        for session in Session.all():
            tmb = Path(session.images[0].thumb)
            if not tmb.name in web_img.glob('*.jpg'):
                copy(str(tmb), str(web_img / tmb.name))
        return [str(x) for x in web_img.glob('*.jpg')]

    def fetch_sessions(self):
        sessions = Session.all()
        reply = []
        for session in sessions:
            reply.append(json.dumps(session.to_dict()))
        return json.dumps(reply)

    def create(self, json_request, callback):
        request = json.loads(json_request)
        session = Session(request['name'], request['raw_path'])
        session.callback = callback
        session.create()
        gevent.sleep(1)

    def session_callback(self, request, data=None, complete=False):
        prog = self.progress
        if complete:
            print(f'PROGRESS: {self.progress}')
            prog[request] = 0
            self.copied = []
            gevent.sleep(0.05)
            return 0
        if data is not None:
            if isinstance(data[0], list):
                [self.copied.append(i) for i in data[0]]
            else:
                self.copied.append(data[0])
            percent = (len(self.copied) / data[1])*100
            print(f"{request} -- {int(percent)}%")
            prog[request] = int(percent)
            gevent.sleep(0.05)
        return prog[request]

    def create_session(self, json_request):
        prog_reset = self.progress.copy()
        self.create(json_request, self.session_callback)
        self.progress = prog_reset
        print(f'PROGRESS: {self.progress}')
        return 'Temp session created return'


def parse_port():
    port = 4242
    try:
        port = int(sys.argv[1])
    except Exception as e:
        print(e)
        pass
    return '{}'.format(port)


def start():
    addr = 'tcp://127.0.0.1:' + parse_port()
    server = zerorpc.Server(Api(), heartbeat=None)
    server.bind(addr)
    print('start running on {}'.format(addr))
    gevent.spawn(server.run())
