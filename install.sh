#!/bin/bash

echo "  ____           _____ _____ ";
echo " / __ \   /\    / ____/ ____|";
echo "| |  | | /  \  | (___| (___  ";
echo "| |  | |/ /\ \  \___ \\___ \ ";
echo "| |__| / ____ \ ____) |___) |";
echo " \____/_/    \_\_____/_____/ ";
echo "     Installation Script     ";                           

function install () {
    case "$(uname -a)" in
        *Debian*|*Ubuntu*)
            installDebian;
            ;;
        *)
            echo "Unable to detect operating system that is compatible with OASS...";
            ;;
    esac
    echo "";
    echo "OASS Installation Complete";
}

install;