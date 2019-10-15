from .config import ConfigService
from importlib import machinery
import os


class Frogd:

    def __init__(self, config):
        self.config = ConfigService(config)
        self.networks = self.config.networks_list()

    @staticmethod
    def interpolate(string, values):
        for value in values.keys():
            string = string.replace('${%s}' % value, values[value])
        return string

    def exec(self, command):
        print(command)
        if not self.config.dry:
            os.system(command)

    def connect(self, network):
        self.exec(self.interpolate(self.config.wireless_connect(), {
            'interface': self.config.interface(),
            'essid': network['essid'],
            'password': network['password']
        }))

        self.exec(self.interpolate(self.config.dhcp_request(), {
            'interface': self.config.interface()
        }))

    def start(self):
        context = {'networks': self.networks, 'current': False}
        rule_loader = machinery.SourceFileLoader('.', self.config.rule)
        rule_module = rule_loader.load_module()

        while True:
            network = rule_module.rule(context)
            self.connect(network)
            context['current'] = network
