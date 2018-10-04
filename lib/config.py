#!/usr/bin/python3

from lib.colors import Colors
from lib.functions import *
from shutil import which
import lib.globals
import sys
import os

def createFolderIfNotExist(s):
    if(not os.path.exists(s)):
        os.makedirs(s)

def createFileIfNotExist(s):
    if(not os.path.exists(s)):
        file = open (s, 'w')  
        file.close()

def fileIsEmpty(s):
    if(os.path.getsize(s) > 0):
        return False
    else:
        return True

def saveFile(path, s):
    file = open (path, 'w') 
    file.write(s)
    file.close()

def readFile(path):
    with open(path, 'r') as file:
        s = file.readline()
        file.close()
    return s

def checkSoftware(s):
    if(which(s) is not None):
        return True
    else:
        return False



def checkConfig():
    lib.globals.PATH = os.environ['HOME'] + "/.OASS"
    createFolderIfNotExist(lib.globals.PATH)

    if("info" in lib.globals.TESTS):
        lib.globals.HUNTERAPI = lib.globals.PATH + "/HUNTERAPI.txt"
        createFileIfNotExist(lib.globals.HUNTERAPI)


        if(fileIsEmpty(lib.globals.HUNTERAPI)):
            hunterAPI = input(Colors.BOLD + "Insert your Hunter.io API: ")
            saveFile(lib.globals.HUNTERAPI, hunterAPI)
        else:
            hunterAPI = readFile(lib.globals.HUNTERAPI)
            confirmHunterAPI = input (Colors.BOLD + "Do you use " + Colors.YELLOW + hunterAPI + Colors.DEFAULT + Colors.BOLD + " HunterAPI? y/n: ")
            if confirmHunterAPI != "y":
                hunterAPI = input(Colors.BOLD + "Insert your Hunter.io API: ")
                saveFile(lib.globals.HUNTERAPI, hunterAPI)

    if("crypst" in lib.globals.TESTS):
        if(not checkSoftware("sslscan")):
            print("sslscan")
        if(not checkSoftware("testssl")):
            default("Instalando testssl")
            c = "cd /usr/share/ && git clone --depth 1 https://github.com/drwetter/testssl.sh.git && cd testssl.sh && chmod +x testssl.sh"
            try:
                os.system(c)
            except:
                error("Error instlando testssl")
            
            saveFile("/usr/bin/testssl", '#!/bin/bash' + '\n' + 'cd /usr/share/testssl.sh/ && ./testssl.sh "$@"')
            

    


