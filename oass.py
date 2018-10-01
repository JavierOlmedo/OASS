#!/usr/bin/python3

from lib.functions import *
from owasp import info
import lib.globals
import socket
import sys

def main():
    lib.globals.initialize()
    banner()
    usage()

    if len(sys.argv[1:]) < 1:
        error("No arguments found!! Read how to use this tool and try again" + "\n")
    else:
        if sys.argv[1] != "-u":
            error("Please, read how to use this tool and try again" + "\n")
        else:
            if len(sys.argv[2:]) < 1:
                error("URL not valid" + "\n")
            else:
                target = sys.argv[2]

                if(isValidDomain(target)):
                    lib.globals.TARGET = target
                    try:
                        lib.globals.IP = socket.gethostbyname(target)
                    except:
                        error("No IP from " + lib.globals.TARGET)
                    success("TARGET " + target + " (" + lib.globals.IP + ")" + "\n")
                    
                    info.main()
                else:
                    error(target + " is not a valid domain" + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        error("User aborted session" + "\n")