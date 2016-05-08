
from lib.config import Parser
from lib.algorithms import Algorithms

import logging
import json

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

    def oneInterface(self):
        pass

    def networkDispatcher(self):
        mode = self.config.getGlobal('mode')
        if mode == 'one-interface':
            self.oneInterface()
        elif mode == 'two-interface':
            pass

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
