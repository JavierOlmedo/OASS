#!/bin/bash

echo "  ____           _____ _____ ";
echo " / __ \   /\    / ____/ ____|";
echo "| |  | | /  \  | (___| (___  ";
echo "| |  | |/ /\ \  \___ \\___ \ ";
echo "| |__| / ____ \ ____) |___) |";
echo " \____/_/    \_\_____/_____/ ";
echo "     Installation Script     ";
                              
function installDebian () {
    sudo apt-get update;
    sudo apt-get -y install git python2.7 python-pip postgresql apache2;
    pip2 install requests psutil;
    installMSF;
}

function installFedora () {
    sudo yum -y install git python-pip;
    pip2 install requests psutil;
    installMSF;
}

function installMSF () {
    if [[ ! "$(which msfconsole)" = */* ]]; then
        curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
            chmod 755 msfinstall && \
            ./msfinstall;
        rm msfinstall;
    fi
}

function install () {
    case "$(uname -a)" in
        *Debian*|*Ubuntu*)
            installDebian;
            ;;
        *Fedora*)
            installFedora;
            ;;
        *)
            echo "Unable to detect operating system that is compatible with OASS...";
            ;;
    esac
    echo "";
    echo "Installation Complete";
}

install;