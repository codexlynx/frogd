#!/bin/bash

if [[ `whoami` != "root" ]]; then
	echo "Attempting to re-run as root..."
	exit
fi

echo "Installation of AP-Jumper"
echo "--------------------------"
echo ""
echo "Installing boot script..."

mv ./apjumper /etc/init.d/
chmod +x /etc/init.d/apjumper
service apjumper start

echo "--------------------------"
echo ""
echo "Installed!"
