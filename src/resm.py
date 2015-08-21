#!/usr/bin/env python
__author__ = 'SuturkinAA'

import os
import sys
from resources import Resources
from config import Config

global res

def setRestPort(resrPort):
    listener = '0.0.0.0:'+str(resrPort)
    if (len(sys.argv)==1):
        sys.argv.append("runserver")
        sys.argv.append(listener)

config = Config();
config.load()

res = Resources(config.resourcesMax);
setRestPort(config.restPort)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rest.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

print ("Started.")
