#!/usr/bin/python3

from lib.functions import *
import lib.globals
import requests
import sys
import re
import os

def crypst001():
    information("CRYPST-001 Testing for Weak SSL/TLS Ciphers, Insufficient Transport Layer Protection")
    print("\n")
    default("Lanzando TestSSL")
    c = "testssl " + "https://" + lib.globals.TARGET
    try:
        os.system(c)
    except:
        error("Error lanzando")
