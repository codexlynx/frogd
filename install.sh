#!/bin/bash

if [[ `whoami` != "root" ]]; then
	echo "Attempting to re-run as root..."
	exit
fi

echo "Installation of WAPJumper"
echo "--------------------------"
echo "Installing boot script..."

cp ./wapjumper /etc/init.d/
chmod +x /etc/init.d/wapjumper
update-rc.d wapjumper defaults
update-rc.d wapjumper disable
service wapjumper start

echo "--------------------------"
echo "Installed!"
