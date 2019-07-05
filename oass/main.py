from lib.functions import *
from owasp.owasp import *
import lib.globals
import sys

def main():
    args = parse_args()
    lib.globals.initialize()
    lib.globals.TARGET = args.domain
    lib.globals.TESTS = args.test

    if(not isValidDomain()):
        error(lib.globals.TARGET + " is not a valid domain." + "\n")
        sys.exit()
    else:
        owasp()