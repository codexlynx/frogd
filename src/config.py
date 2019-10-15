from json import loads, dumps
import configparser
import csv


class ConfigService:

    def __init__(self, config):
        self.main = configparser.ConfigParser()
        self.main.read(config['config_path'])
        self.networks = open(config['networks_file_path'], 'r')
        self.rule = config['rule_path']
        self.dry = config['dry_run']

    def interface(self):
        return self.main.get('global', 'interface')

    def notifications(self):
        value = self.main.get('global', 'notifications')
        if value == 'true':
            return True
        else:
            return False

    def networks_list(self):
        fieldnames = ('id', 'essid', 'password')
        reader = csv.DictReader(self.networks, fieldnames)
        return loads(dumps([row for row in reader]))[1:]

    def wireless_connect(self):
        key = self.main.get('global', 'command_wireless_connect')
        return self.main.get('commands', key)

    def dhcp_request(self):
        key = self.main.get('global', 'command_dhcp_request')
        return self.main.get('commands', key)
