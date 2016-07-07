#!/usr/bin/env python

import configparser
import json

class Parser(object):

    def __init__(self, filename):
        self.conf = configparser.ConfigParser()
        self.conf.read(filename)

    def getGlobal(self, key):
        value = self.conf.get('global', key)
        return value

    def getCommad(self, command):
        name = self.conf.get('global', command)
        command = self.conf.get('commands', name)
        return command

    def getInterfaces(self):
        int1 = self.conf.get('interfaces', 'name1')
        int2 = self.conf.get('interfaces', 'name2')
        return int1, int2

    def getNetworks(self):
        source = self.conf.get('networks', 'source')
        if source == 'local':
            jsondata = self.conf.get('networks', 'list')
            jsondata = json.loads(jsondata)
        return jsondata
