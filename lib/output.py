#!/usr/bin/python3

from lib.colors import Colors
from lib.time import t

def success(s):
    print(Colors.BOLD + Colors.GREEN + t() + " [+] " + s + Colors.DEFAULT)

def info(s):
    print(Colors.BOLD + Colors.BLUE + t() + " [!] " + s + Colors.DEFAULT)

def warning(s):
    print(Colors.BOLD + Colors.YELLOW + t() + " [!] " + s + Colors.DEFAULT)

def error(s):
    print(Colors.BOLD + Colors.RED + t() + " [-] " + s + Colors.DEFAULT)