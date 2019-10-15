## frogd
Daemon for the automatic jumping over 802.11 networks.

[![AUR](https://img.shields.io/aur/license/yaourt.svg)](LICENSE)
![privacy](https://img.shields.io/badge/privacy-tool-red.svg?style=flat)

---

### Usage
```
usage: frogd [-h] [--config PATH] [--rule PATH] [--networks-file PATH]
                     [--dry]

frogd / Daemon CLI.

optional arguments:
  -h, --help            show this help message and exit
  --config PATH         Main configuration file path.
  --rule PATH           Jump rule to use.
  --networks-file PATH  CSV file with the list of networks.
  --dry                 Enable dry run.
```

**Defaults:**
> $ frogd --config /etc/frogd/config.cfg --rule /etc/frogd/rules/by_time.py --networks-file /etc/frogd/networks.csv

### Disclaimer

* __Legal__:
Use it at your own responsibility. Damages or legal problems caused by the tool are the responsibility of the user.

### License

> GPL (GNU General Public License) 3.0

More info: [here](LICENSE)

### About
This tool was created by: __@codexlynx__.

* Twitter: [https://twitter.com/codexlynx](https://twitter.com/codexlynx)
* GitHub: [https://github.com/codexlynx](https://github.com/codexlynx)
