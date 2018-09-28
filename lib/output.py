#!/usr/bin/python3

from lib.colors import Colors
from lib.time import t

def error(s):
    print(Colors.BOLD + Colors.RED + t() + " " + s + Colors.DEFAULT)