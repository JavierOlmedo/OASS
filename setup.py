#!/usr/bin/python3
# -*- coding: utf-8 -*-

import platform
import shutil
import subprocess
import sys
import os

if(len(sys.argv) != 2 or sys.argv[1] != "install"):
    print("** OASS Installer **")
    print("** Written by: Javier Olmedo (@JJavierOlmedo) **")
    print("** Visit: https://hackpuntes.com **")
    print("\nTo install, run: `# setup.py install'")
    sys.exit()

if(os.getuid() != 0):
    print("** OASS Installer **")
    print("[!] Please execute as root: `$ sudo python3 setup.py install'")
    sys.exit()

if("Kali" not in platform.linux_distribution()):
    print("Sorry, this installer is only designed for Kali Linux")
    sys.exit()

def install():
    destdir = "/usr/share/oass"
    bindir = "/usr/bin"
    print("[*] Copying OASS into the /usr/share directory...")
    subprocess.Popen("cp -rf . /usr/share/oass", shell=True).wait()

    print("[*] Installing OASS runner to /usr/share..." % bindir)
    subprocess.Popen("echo \#!/bin/bash > /usr/share/oass", shell=True).wait()
    subprocess.Popen("echo cd {0} >> {1}/oass".format(destdir, bindir), shell=True).wait()
    subprocess.Popen("echo exec python3 oass.py $@ >> /usr/share/oass", shell=True).wait()
    subprocess.Popen("chmod +x /usr/share/oass", shell=True).wait()

    if(not os.path.isdir("/etc/oass/")):
        print("[*] Creating oass config dir /etc/oass./..")
        os.makedirs("/etc/oass/")
    if(not os.path.isfile("/etc/oass/oass.config")):
        print("[*] Installing default OASS config to /etc/oass./..")

    print("[*] We are now finished! To run OASS, type `oass'...")

print("Installing dependencies...")


subprocess.Popen("apt-get -y install "
                 "git apache2 python-requests libapache2-mod-php "
                 "python-pymssql build-essential python-pexpect "
                 "python-pefile python-crypto python-openssl", shell=True).wait()

if os.path.isdir("/usr/share/oass"):
    print("OASS is already installed in /usr/share/oass. Remove and start again.")
    sys.exit()

try:
    install()
except Exception as e:
    print("Error installing OASS", e)