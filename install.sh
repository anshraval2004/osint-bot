#!/bin/bash

echo "Installing CYBER X TOOL..."

# Termux
pkg install python -y 2>/dev/null

# Kali/Linux
sudo apt update && sudo apt install python3 python3-pip -y 2>/dev/null

# Install Python dependencies
pip3 install -r requirements.txt 2>/dev/null

chmod +x osint.py

# Move to PATH
mv osint.py $PREFIX/bin/cyberx 2>/dev/null || sudo mv osint.py /usr/local/bin/cyberx

echo "Installation complete! Run: cyberx"
