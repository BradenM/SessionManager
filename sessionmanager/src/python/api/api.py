from __future__ import print_function
import sys
import zerorpc
import json
from io import StringIO
import requests
import sys
import os
from pathlib import Path
from manage.session import Session
from data import data
from definitions import DATABASE, ROOT_DIR
from shutil import copy
import gevent


class Api(object):
    def __init__(self, *args, **kwargs):
        self._create_progress = 0
        self.copied = []

    def echo(self, text):
        """echo any text"""
        return text

    def check_dir(self):
        os_cur = os.getcwd()
        sys_cur = sys.path
        reply = f"""
        Current Path: {os_cur},
        Sys Current: {sys_cur},
        Database: {DATABASE},
        ROOT_DIR: {ROOT_DIR},
        Session Info: {data.db.info}
        """
        return reply

    def get_thumb(self):
        web_img = Path.cwd() / 'src' / 'imgs' / 'thumb'
        for s in Session.all():
            tmb = Path(s.images[0].thumb)
            if not tmb.name in web_img.glob('*.jpg'):
                copy(str(tmb), str(web_img / tmb.name))
        return [str(x) for x in web_img.glob('*.jpg')]

    def fetch_sessions(self):
        sessions = Session.all()
        reply = []
        for s in sessions:
            reply.append(json.dumps(s.to_dict()))
        return json.dumps(reply)

    def create(self, json_request, callback):
        request = json.loads(json_request)
        s = Session(request['name'], request['raw_path'])
        s.copy_callback = callback
        s.create()
        gevent.sleep(0)

    def copy_callback(self, data=None, complete=False):
        if complete:
            self._create_progress = 100
            gevent.sleep(0)
            return self._create_progress
        if data is not None:
            self.copied.append(data[0])
            percent = (len(self.copied) / data[1])*100
            self._create_progress = int(percent)
            gevent.sleep(0)
        return self._create_progress

    def create_session(self, json_request):
        gevent.joinall([
            gevent.spawn(self.create(json_request, self.copy_callback))
        ])
        return 'Temp session created return'


def parse_port():
    port = 4242
    try:
        port = int(sys.argv[1])
    except Exception as e:
        pass
    return '{}'.format(port)


def start():
    addr = 'tcp://127.0.0.1:' + parse_port()
    s = zerorpc.Server(Api())
    s.bind(addr)
    print('start running on {}'.format(addr))
    gevent.spawn(s.run())
