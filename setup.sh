#!/bin/bash

# Colors
GREEN="\033[1;92m"
CYAN="\033[1;96m"
MAGENTA="\033[1;35m"
YELLOW="\033[1;33m"
RED="\033[1;91m"
RESET="\033[0m"

# Kill any running apt/dpkg/pkg processes to avoid lock issues
pkill -9 apt
pkill -9 dpkg
pkill -9 pkg
rm -rf /data/data/com.termux/cache/apt/archives/lock
rm -rf /data/data/com.termux/files/usr/var/lib/dpkg/lock
rm -rf /data/data/com.termux/files/usr/var/lib/dpkg/lock-frontend
sleep 2

# Update & Install Dependencies
echo ""

echo -e "${CYAN}[+] git Installing....${RESET}"
echo -e "${GREEN}"
pkg install git -y
echo -e "${RESET}"

echo -e "${CYAN}[+] python Installing....${RESET}"
echo -e "${GREEN}"
pkg install python -y
echo -e "${RESET}"

echo -e "${CYAN}[+] p7zip Installing....${RESET}"
echo -e "${GREEN}"
pkg install p7zip -y
echo -e "${RESET}"

sleep 2
python BruteZip.py


