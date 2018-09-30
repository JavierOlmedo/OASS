#!/usr/bin/python3

from lib.functions import *
from owasp import info
import sys

def main():
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
                success("TARGET " + target + "\n")
                info.main()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        error("User aborted session" + "\n")