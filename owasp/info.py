#!/usr/bin/python3

from lib.functions import *
import lib.globals
import requests
import sys
import re
import os

def info001():
    info("INFO-001 Conduct search engine discovery/reconnaissance for information leakage")

    def hunterio():
        default("Find emails in Hunter.io")
        emails = []
        url = "https://api.hunter.io/v2/domain-search?domain=" + lib.globals.TARGET +"&api_key=" + lib.globals.HUNTERAPI

        try:
            r = requests.get(url)
            rdata = r.json()
            resultados = rdata['meta']['results']
            if (resultados >= 1):
                emails = rdata['data']['emails']
            else:
                error(str(resultados) + " emails found!!")
            for mail in emails:
                success(mail['value'])
        except:
            error("Error in Hunter.io API")

    def theharvester():
        default("Launch command in TheHarvester")
        c = "theharvester -d " + lib.globals.TARGET + " -b all"
        try:
            os.system(c)
        except:
            error("Error in theHarvester command")

    def sublist3r():
        default("Launch command in Sublist3r")
        c = "cd /root/Herramientas/Sublist3r &&python sublist3r.py -d " + lib.globals.TARGET +""
        try:
            os.system(c)
        except:
            error("Error Sublist3r command")

    hunterio()
    theharvester()
    sublist3r()
    print("\n")

def info002():
    info("INFO-002 Fingerprint Web Server")

    def whatweb():
        default("Launch command in WhatWeb")
        c = "whatweb " + lib.globals.TARGET + ""
        try:
            os.system(c)
        except:
            error("Error in WhatWeb command")

    whatweb()
    print("\n")
    
def info003():
    info("INFO-003 Review Webserver Metafiles for Information Leakage")
    print("\n")
    
def info004():
    info("INFO-004 Enumerate Applications on Webserver")
    print("\n")

def info005():
    info("INFO-005 Review webpage comments and metadata for information leakage")
    print("\n")

def info006():
    info("INFO-006 Identify application entry points")
    print("\n")

def info007():
    info("INFO-007 Map execution paths through application")
    print("\n")

def info008():
    info("INFO-008 Fingerprint Web Application Framework")
    print("\n")

def info009():
    info("INFO-009 Fingerprint Web Application")
    print("\n")

def info010():
    info("INFO-010 Map Application Architecture")
    print("\n")

def main():
    info001()
    info002()
    info003()
    info004()
    info005()
    info006()
    info007()
    info008()
    info009()
    info010()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        error("User aborted session" + "\n")