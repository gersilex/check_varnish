#!/usr/bin/env python2
#
# Nagios Plugin for Varnish 4
# ---------------------------
#
#  Copyright (c) 2014 Leroy Foerster <lfoerster@goodgamestudios.com>
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

"""Check Varnish 4 status using the varnishstat utility.
Current version checks only one metric with optional warning and critical ranges."""

__author__ = 'lfoerster@goodgamestudios.com'
__version__ = "1.1"

import sys
import argparse
import subprocess
import nagiosplugin


@nagiosplugin.guarded
class Varnish(nagiosplugin.Resource):
    def __init__(self, metric):
        self.metric = metric

    def probe(self):
        command = runcommand(options.path + " -1")
        command = str(command)
        lines = command.splitlines()

        for line in lines:
            if self.metric in str(line).split():
                words = line.split()
                return nagiosplugin.Metric(name=words[0], value=int(words[1]), context="Varnish")


def runcommand(command):
    process = subprocess.Popen(command.split(" "), stdout=subprocess.PIPE)
    output, unused_err = process.communicate()
    return output

o = argparse.ArgumentParser(description=__doc__)

o.add_argument('-m', '--metric', help="name of the metric to check", default="MAIN.uptime")
o.add_argument('-p', '--path', default='/usr/bin/varnishstat', help="path to varnishstat binary")
o.add_argument('-w', '--warning', metavar='RANGE', help="(supports nagios-style ranges)")
o.add_argument('-c', '--critical', metavar='RANGE', help="(supports nagios-style ranges)")
o.add_argument('-l', '--list', help="list all known metrics", action="store_true")
o.add_argument('-V', '--version', action="version", version=__version__)
options = o.parse_args()

if options.list:
    print(str(runcommand(options.path + " -1")))
    sys.exit(3)

nagiosplugin.Check(Varnish(str(options.metric)),
                   nagiosplugin.ScalarContext("Varnish", options.warning, options.critical)).main()

