# whiptail.py - Use whiptail to display dialog boxes from shell scripts
# Copyright (C) 2013 Marwan Alsabbagh
# license: BSD, see LICENSE for more details.

__version__ = '0.1'

import sys
import shlex
from utile import save_args, flatten
from subprocess import Popen, PIPE
from collections import namedtuple

Response = namedtuple('Response', 'returncode value')


class Whiptail(object):
    def __init__(self, title='', backtitle='', height=10, width=50, auto_exit=True):
        save_args(self, vars())

    def run(self, control, msg, extra=(), exit_on=(1, 255)):
        cmd = ['whiptail', '--title', self.title, '--backtitle', self.backtitle,
               '--' + control, msg, str(self.height), str(self.width)] + list(extra)
        p = Popen(cmd, stderr=PIPE)
        out, err = p.communicate()
        if self.auto_exit and p.returncode in exit_on:
            print 'User cancelled operation.'
            sys.exit(p.returncode)
        return Response(p.returncode, err)

    def prompt(self, msg, default='', password=False):
        control = 'passwordbox' if password else 'inputbox'
        return self.run(control, msg, [default]).value

    def confirm(self, msg, default='yes'):
        defaultno = '--defaultno' if default == 'no' else ''
        return self.run('yesno', msg, [defaultno], [255]).returncode == 0

    def alert(self, msg):
        self.run('msgbox', msg)

    def view_file(self, path):
        self.run('textbox', path, ['--scrolltext'])

    def calc_height(self, msg):
        height_offset = 8 if msg else 7
        return [str(self.height - height_offset)]

    def menu(self, msg='', items=(), prefix=' - '):
        if isinstance(items[0], basestring):
            items = [(i, '') for i in items]
        else:
            items = [(k, prefix + v) for k, v in items]
        extra = self.calc_height(msg) + flatten(items)
        return self.run('menu', msg, extra).value

    def showlist(self, control, msg, items, prefix):
        if isinstance(items[0], basestring):
            items = [(i, '', 'OFF') for i in items]
        else:
            items = [(k, prefix + v, s) for k, v, s in items]
        extra = self.calc_height(msg) + flatten(items)
        return shlex.split(self.run(control, msg, extra).value)

    def radiolist(self, msg='', items=(), prefix=' - '):
        return self.showlist('radiolist', msg, items, prefix)

    def checklist(self, msg='', items=(), prefix=' - '):
        return self.showlist('checklist', msg, items, prefix)
