check_varnish
=============

nagios plugin for Varnish 4+
Requires Python 3.3+ with nagiosplugin and argparse python modules

Installation
============
- Install dependencies:
  - `cd /tmp`
  - `wget https://pypi.python.org/packages/source/n/nagiosplugin/nagiosplugin-1.2.2.tar.gz#md5=c85e1641492d606d929b02aa262bf55d`
  - ``wget https://pypi.python.org/packages/source/a/argparse/argparse-1.2.1.tar.gz#md5=2fbef8cb61e506c706957ab6e135840c`
  - `tar xvzf <package-name.tar.gz>`
  - `cd <package-name>`
  - `python3 setup.py install` in each of the packages. All of them have a `setup.py` included, which takes commands just like `pip` would on Python 2.7
- copy `check_varnish.py` into desired location
- Enjoy!

```
usage: check_varnish.py [-h] [-m METRIC] [-p PATH] [-w RANGE] [-c RANGE] [-l]
                        [-V]

Check Varnish 4 status using the varnishstat utility. Current version checks
only one metric with optional warning and critical ranges.

optional arguments:
  -h, --help            show this help message and exit
  -m METRIC, --metric METRIC
                        name of the metric to check
  -p PATH, --path PATH  path to varnishstat binary
  -w RANGE, --warning RANGE
                        (supports nagios-style ranges)
  -c RANGE, --critical RANGE
                        (supports nagios-style ranges)
  -l, --list            list all known metrics
  -V, --version         show program's version number and exit
```
