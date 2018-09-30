#!/usr/bin/python3

from lib.colors import Colors
import time
import sys
import os

VERSION = "1.0"



def banner():
    os.system("clear")
    print(Colors.BOLD +
    """
                    ________      _____    _________ _________
                    \_____  \    /  _  \  /   _____//   _____/
                     /   |   \  /  /_\  \ \_____  \ \_____  \ 
                    /    |    \/    |    \/        \/        \\
                    \_______  /\____|__  /_______  /_______  /
                            \/         \/        \/        \/     
                                                              v""" + VERSION + """
                                                                       
                ============ [OWASP Automatic Scan Script] ============
                               Made with ❤️  in Spain                          
                       
                ======= Javier Olmedo - https://hackpuntes.com ========
                [*] Facebook: https://facebook.com/hackpuntes       [*]
                [*] Twitter:  https://twitter.com/jjavierolmedo     [*]
                [*] LinkedIn: https://linkedin.com/in/jjavierolmedo [*]
                [*] GitHub:   https://github.com/JavierOlmedo       [*]
                =======================================================
    """ + Colors.DEFAULT)

def usage():
	print(Colors.BOLD + """
	EXAMPLE:
		-u [REQUIRED] Target URL
		python3 oass.py -u [PATH]
        
		-o [OPTIONAL] Output folder
		python3 oass.py -u [PATH] -o [OUTPUT]
	""" + Colors.DEFAULT)

def t():
	current_time = time.localtime()
	ctime = time.strftime('%H:%M:%S', current_time)
	return "["+ ctime + "]"

def success(s):
    print(Colors.BOLD + Colors.GREEN + t() + " [+] " + s + Colors.DEFAULT)

def info(s):
    print(Colors.BOLD + Colors.BLUE + t() + " [!] " + s + Colors.DEFAULT)

def warning(s):
    print(Colors.BOLD + Colors.YELLOW + t() + " [!] " + s + Colors.DEFAULT)

def error(s):
    print(Colors.BOLD + Colors.RED + t() + " [-] " + s + Colors.DEFAULT)

def default(s):
    print(Colors.BOLD + t() + " [+] " + s + Colors.DEFAULT)