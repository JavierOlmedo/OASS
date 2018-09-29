#!/usr/bin/python3

from lib.banner import banner
from lib.usage import usage
from lib.output import *
from owasp import owasp
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
                owasp.gowasp(target)