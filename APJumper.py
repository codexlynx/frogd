
from lib.config import Parser

import logging

config      = './config.cfg'
logfile     = './APJumper.log'

class APJumper(object):

    def __init__(self):
        logging.basicConfig(filename = log, level = logging.DEBUG,
                            format = '%(asctime)s - %(levelname)s - %(message)s')

        self.config = Parser(config)

    def start(self):
        #print (self.config.getNetworks())
        logging.info('Daemon running...')

def main():
    jumper = APJumper()
    jumper.start()

if __name__ == '__main__':
    main()
