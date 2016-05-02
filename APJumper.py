
from lib.config import Parser

config = './config.cfg'

class APJumper(object):

    def __init__(self):
        self.config = Parser(config)

    def start(self):
        print (self.config.getGlobal('mode'))

def main():
    jumper = APJumper()
    jumper.start()

if __name__ == '__main__':
    main()
