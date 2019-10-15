from .core import Frogd
import argparse

parser = argparse.ArgumentParser(description='frogd / Daemon CLI.')

parser.add_argument('--config', default='config.cfg.sample', type=str, help='Main configuration file path.',
                    metavar='PATH')

parser.add_argument('--rule', default='rules/by_time.py', type=str, help='Jump rule to use.',
                    metavar='PATH')

parser.add_argument('--networks-file', default='networks.csv.sample', type=str,
                    help='CSV file with the list of networks.', metavar='PATH')

parser.add_argument('--dry', action='store_true', help='Enable dry run.')


def run():
    args = parser.parse_args()
    daemon = Frogd({
        'networks_file_path': args.networks_file,
        'config_path': args.config,
        'rule_path': args.rule,
        'dry_run': args.dry
    })
    daemon.start()
