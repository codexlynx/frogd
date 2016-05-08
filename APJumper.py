
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
        self.config = Parser(config)

    def processParameters(self):
        param = self.config.getGlobal('parameters')
        param = param.replace('${id}', str(self.id))
        return json.loads(param)

    def loadNetworks(self):
        self.json = self.config.getNetworks()
        self.max = str(self.json).count("'essid'") - 1

    def checkConnection(self):
        cmd = 'ping -c %d %s > /dev/null 2>&1' % (self.checkPkt, self.checkServer)
        print (cmd)
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
        if dhcp != 'false':
            self.dhcp(interface, dhcp)

        callback = self.config.getGlobal('callback')
        if callback != 'false':
            print (callback)
            #os.system(callback)

        check = self.config.getGlobal('check')
        if check == 'true':
            status = self.checkConnection()
        else:
            status = True
            
        return status

    def networkDispatcher(self):
        mode = self.config.getGlobal('mode')
        if mode == 'one-interface':
            inter = self.oneInterface()
        elif mode == 'two-interface':
            pass
        status = self.postConnect(inter)
        return status

    def nextNetwork(self, mode):
        engine = self.config.getGlobal('algorithm')
        engine = getattr(Algorithms, engine)
        kwargs = self.processParameters()
        self.id = engine(self, mode, **kwargs)

    def start(self):
        logging.info('APJumper daemon running')
        while True:
            logging.info('Loading networks')
            self.loadNetworks()
            logging.info('Connecting to the new network')
            status = self.networkDispatcher()
            logging.info('Jumping to the next network')
            self.nextNetwork(status)

def main():
    jumper = APJumper(config, logfile)
    jumper.start()

if __name__ == '__main__':
    main()
