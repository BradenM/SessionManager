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


class Api(object):
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

    def get_thumb(self, thumb=None):
        web_img = Path.cwd() / 'src' / 'imgs' / 'thumb'
        thumb = Path(thumb)
        match = None
        for s in Session.all():
            tmb = Path(s.images[0].thumb)
            if not tmb.name in web_img.glob('*.jpg'):
                copy(str(tmb), str(web_img / tmb.name))
                if thumb.name == tmb.name:
                    match = '../' + str(Path('src') / 'imgs' / tmb.name)
        if match is not None:
            return match
        else:
            return [str(x) for x in web_img.glob('*.jpg')]

    def fetch_sessions(self):
        sessions = Session.all()
        reply = []
        for s in sessions:
            reply.append(json.dumps(s.to_dict()))
        return json.dumps(reply)


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
    s.run()
