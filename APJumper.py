#!/usr/bin/env python

from lib.config import Parser
from lib.algorithms import Algorithms

import logging
import json
import os

config      = './config.cfg'
logfile     = './APJumper.log'

class APJumper(object):

    def __init__(self, config, logfile): #Arguments for using as module
        logging.basicConfig(filename = logfile, level = logging.DEBUG,
                            format = '%(asctime)s - %(levelname)s - %(message)s')
        self.checkServer = '8.8.8.8'
        self.checkPkt = 3
        '''#'''
        self.id = 0 #ID Starting

    def sendEvent(self, text, notify = True, log = True):
        if log == True:
            logging.info(text)

        if notify == True and bool(self.config.getGlobal('notifications')) != False:
            notify = self.config.getCommad('notifications')
            notify = notify.replace('${title}', 'AP-Jumper')
            notify = notify.replace('${text}', text)
            os.system(notify)

    def processParameters(self):
        param = self.config.getGlobal('parameters')
        param = param.replace('${id}', str(self.id))
        return json.loads(param)

    def loadNetworks(self):
        self.json = self.config.getNetworks()
        self.max = str(self.json).count("'essid'") - 1

    def checkConnection(self):
        cmd = 'ping -c %d %s > /dev/null' % (self.checkPkt, self.checkServer)
        rcv = os.system(cmd)
        if rcv == 0:
            return True
        else:
            return False

    def dhcp(self, interface, command):
        dhcp = command.replace('${interface}', interface)
        print (dhcp)
        #os.system(dhcp)

    def connectNetwork(self, interface):
        network = self.config.getNetworks()[str(self.id)]
        command = self.config.getCommad('manager')
        command = command.replace('${interface}', interface)
        command = command.replace('${essid}', network['essid'])
        command = command.replace('${password}', network['password'])
        print (command)
        #os.system(command)

    def oneInterface(self):
        inter1, inter2 = self.config.getInterfaces()
        self.connectNetwork(inter1)
        return inter1

    def postConnect(self, interface):
        dhcp = self.config.getCommad('dhcp')
        if bool(dhcp) != False:
            self.dhcp(interface, dhcp)

        callback = self.config.getGlobal('callback')
        if bool(callback) != False:
            print (callback)
            #os.system(callback)

        check = self.config.getGlobal('check')
        if bool(check) == True:
            status = self.checkConnection()
        else:
            status = True

        return status

    def networkDispatcher(self):
        mode = self.config.getGlobal('mode')
        if mode == 'one-interface':
            inter = self.oneInterface()
        elif mode == 'two-interface':
            pass #@TODO
        status = self.postConnect(inter)
        return status

    def nextNetwork(self, mode):
        engine = self.config.getGlobal('algorithm')
        engine = getattr(Algorithms, engine)
        kwargs = self.processParameters()
        self.id = engine(self, mode, **kwargs)

    def start(self):
        self.config = Parser(config)
        logging.info('APJumper daemon running')
        while True:
            self.sendEvent('Loading networks', False)
            self.loadNetworks()
            self.sendEvent('Connecting to the new network')
            status = self.networkDispatcher()
            self.sendEvent('Jumping to the next network', False)
            self.nextNetwork(status)

def main():
    jumper = APJumper(config, logfile)
    jumper.start()

if __name__ == '__main__':
    main()
