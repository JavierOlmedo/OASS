#!/usr/bin/python3

from lib.functions import *
import lib.globals
import requests
import sys
import re
import os

def info001():
    information("INFO-001 Conduct search engine discovery/reconnaissance for information leakage")

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
    information("INFO-002 Fingerprint Web Server")

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
    information("INFO-003 Review Webserver Metafiles for Information Leakage")
    print("\n")
    
def info004():
    information("INFO-004 Enumerate Applications on Webserver")
    print("\n")

def info005():
    information("INFO-005 Review webpage comments and metadata for information leakage")
    print("\n")

def info006():
    information("INFO-006 Identify application entry points")
    print("\n")

def info007():
    information("INFO-007 Map execution paths through application")
    print("\n")

def info008():
    information("INFO-008 Fingerprint Web Application Framework")
    print("\n")

def info009():
    information("INFO-009 Fingerprint Web Application")
    print("\n")

def info010():
    information("INFO-010 Map Application Architecture")
    print("\n")