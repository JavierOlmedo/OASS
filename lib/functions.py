#!/usr/bin/python3

from lib.colors import Colors
import lib.globals
import argparse
import socket
import time
import sys
import re
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

def t():
	current_time = time.localtime()
	ctime = time.strftime('%H:%M:%S', current_time)
	return ("["+ ctime + "]")

def isValidDomain():
    match = re.search("^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$", lib.globals.TARGET)
    if match:
        getIP()
        return True
    else:
        return False

def success(s):
    print(Colors.BOLD + Colors.GREEN + t() + " [+] " + s + Colors.DEFAULT)

def information(s):
    print(Colors.BOLD + Colors.BLUE + t() + " " + s + Colors.DEFAULT)

def warning(s):
    print(Colors.BOLD + Colors.YELLOW + t() + " [!] " + s + Colors.DEFAULT)



def default(s):
    print(Colors.BOLD + t() + " [+] " + s + Colors.DEFAULT)

def parser_error(s):
    banner()
    print(Colors.BOLD + "USAGE: python3 " + sys.argv[0] + " [OPTIONS] (use -h for help)" + Colors.DEFAULT)
    error(s + "\n")
    sys.exit()

def parse_args():
    os.system("clear")
    banner()
    parser = argparse.ArgumentParser(epilog='\tEXAMPLE: \r\npython3 ' + sys.argv[0] + " -d google.com" + "\n")
    parser.error = parser_error
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-d', '--domain', help="Domain name to check OWASP Tests", required=True)
    parser.add_argument('-o', '--output', help='Save the results to text file')
    parser.add_argument('-t', '--test', help='Tests to check info, config, crypst, etc (Default info and crypst)', nargs='+', default=['crypst'])
    #parser.add_argument('-t', '--test', help='Tests to check info, config, crypst, etc (Default info and crypst)', nargs='+', default=['info','crypst'])
    #parser.add_argument('-t', '--threads', help='Number of threads to use for tests (Default 10)', type=int, default=10)
    parser.add_argument('-v', '--verbose', help='Enable verbosity and display results in realtime', nargs='?', default=False)
    
    
    return parser.parse_args()

def getIP():
    try:
        lib.globals.IP = socket.gethostbyname(lib.globals.TARGET)
    except:
        error("IP has not been obtained from " + lib.globals.TARGET + "\n")
        sys.exit()           