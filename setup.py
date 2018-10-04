#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import platform
import shutil
import subprocess
import sys

# if our command option is true then install stuff
if(len(sys.argv) != 2 or sys.argv[1] != "install"):
    print("** OASS Installer **")
    print("** Written by: Javier Olmedo (@JJavierOlmedo) **")
    print("** Visit: https://hackpuntes.com **")
    print("\nTo install, run: `# setup.py install'")
    exit()

if(os.getuid() != 0):
    print("** OASS Installer **")
    print("[!] Please execute as root: `$ sudo python3 setup.py install'")
    exit()

platformOS = platform.system()
if platformOS not in  ["Linux", "Darwin"]:
    print("[!] Sorry this installer is not designed for %s (only Linux and Mac)"
          ". Please install the Python dependencies manually." % platformOS)
    exit()

def install(prefix):
    destdir = "%s/share/oass" % prefix
    bindir = "%s/bin" % prefix
    print("[*] Copying OASS into the %s directory..." % destdir)
    subprocess.Popen("cp -rf . %s" % destdir, shell=True).wait()

    print("[*] Installing OASS runner to %s..." % bindir)
    subprocess.Popen("echo \#!/bin/bash > %s/oass" % bindir, shell=True).wait()
    subprocess.Popen("echo cd {0} >> {1}/oass".format(destdir, bindir), shell=True).wait()
    subprocess.Popen("echo exec python3 oass $@ >> %s/oass" % bindir, shell=True).wait()
    subprocess.Popen("chmod +x %s/oass" % bindir, shell=True).wait()

    print("[*] Installing OASS updater to %s..." % bindir)
    subprocess.Popen("cp {0}/oassupdate {1}/".format(destdir, bindir), shell=True).wait()
    subprocess.Popen("chmod +x %s/oassupdate" % bindir, shell=True).wait()

    if not os.path.isdir("/etc/oass/"):
        print("[*] Creating oass config dir /etc/oass./..")
        os.makedirs("/etc/oass/")
    if not os.path.isfile("/etc/oass/oass.config"):
        print("[*] Installing default OASS config to /etc/oass./..")
        #shutil.copyfile("src/core/config.baseline", "/etc/oass/oass.config")

    print("[*] We are now finished! To run OASS, type `oass'...")

# if linux then run installer
if platformOS == "Linux":
    print("[*] Installing dependencies...")

    # if we trigger on sources.list then we know its ubuntu
    if os.path.isfile("/etc/apt/sources.list"):

        # force install of debian packages
        subprocess.Popen("apt-get -y install "
                         "git apache2 python-requests libapache2-mod-php "
                         "python-pymssql build-essential python-pexpect "
                         "python-pefile python-crypto python-openssl", shell=True).wait()

    # If pacman.conf exists, we have a Arch based system
    elif os.path.isfile("/etc/pacman.conf"):
        subprocess.Popen("pacman -S --noconfirm --needed git python2 "
                         "python2-beautifulsoup3 python2-pexpect python2-crypto", shell=True).wait()

        subprocess.Popen("wget https://github.com/erocarrera/pefile/archive/master.zip", shell=True).wait()
        subprocess.Popen("unzip master.zip", shell=True).wait()
        subprocess.Popen("chmod a+x pefile-master/setup.py", shell=True).wait()
        subprocess.Popen("rm -rf pefile-master*", shell=True).wait()

    # if dnf.conf is there, we are dealing with a >= fedora 22 - added thanks to whoismath pr
    elif os.path.isfile("/etc/dnf/dnf.conf"):
        subprocess.Popen("dnf -y install git python-pexpect python-pefile python-crypto pyOpenSSL", shell=True).wait()

    # if sources.list or pacman.conf is not available then we're running
    # something offset
    else:
        print("[!] You're not running a Debian, Fedora or Arch variant. Installer not finished for this type of Linux distro.")
        print("[!] Install git, python-pexpect, python-crypto, python-openssl, python-pefile manually for all of OASS dependancies.")
        sys.exit()

    if os.path.isdir("/usr/share/oass"):
        print("[!] OASS is already installed in /usr/share/oass. Remove and start again.")
        sys.exit()

    if not os.path.isfile("/usr/bin/git"):
        print("[-] Install failed. GIT is not installed. OASS will not continue.")
        print("[!] Install GIT and run the installer again.")
        sys.exit()

    try:
        install(prefix="/usr")
    except Exception as e:
        print("[!] Error installing OASS", e)

if platformOS == 'Darwin':
    print("[*] Installing dependencies...")
    subprocess.Popen("easy_install pexpect pycrypto pyopenssl pefile", shell=True).wait()
    try:
        install(prefix="/usr/local")
    except Exception as e:
        print("[!] Error installing OASS", e)