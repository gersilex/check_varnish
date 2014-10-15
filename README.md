check_varnish
=============

nagios plugin for Varnish 4+
Requires Python 3.3+ with nagiosplugin and argparse python modules

Installation
============
- Install pip with your distribution's package manager
- `sudo pip install nagiosplugin`
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
