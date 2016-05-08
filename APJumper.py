
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

        self.id = 0 #ID Starting
        self.config = Parser(config)

    def processParameters(self):
        param = self.config.getGlobal('parameters')
        param = param.replace('${id}', str(self.id))
        return json.loads(param)

    def loadNetworks(self):
        self.json = self.config.getNetworks()
        self.max = str(self.json).count("'essid'") - 1

    def checkConnection(self):
        pass

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
        if dhcp != False:
            self.dhcp(interface, dhcp)

        callback = self.config.getGlobal('callback')
        if callback != False:
            print (callback)
            #os.system(callback)
        check = self.config.getGlobal('check')
        if check == True:
            self.checkConnection()

    def networkDispatcher(self):
        mode = self.config.getGlobal('mode')
        if mode == 'one-interface':
            inter = self.oneInterface()
        elif mode == 'two-interface':
            pass
        self.postConnect(inter)

    def nextNetwork(self):
        engine = self.config.getGlobal('algorithm')
        engine = getattr(Algorithms, engine)
        kwargs = self.processParameters()
        self.id = engine(self, **kwargs)

    def start(self):
        logging.info('APJumper daemon running')
        while True:
            logging.info('Loading networks')
            self.loadNetworks()
            logging.info('Connecting to the new network')
            self.networkDispatcher()
            logging.info('Jumping to the next network')
            self.nextNetwork()

def main():
    jumper = APJumper(config, logfile)
    jumper.start()

if __name__ == '__main__':
    main()
