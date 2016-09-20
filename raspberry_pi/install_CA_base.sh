#!/bin/bash

# Installs on top of Raspbian Jessie
HOME=/home/pi

# Requires name of drone as argument
if [ $# -ne 1 ]; then
    echo $0: Usage: install_CA_base.sh drone_name
    exit 1
fi
name=$1

apt-get update

# Set up text editor
apt-get install -y vim
cp configurations/vimrc $HOME/.vimrc

# Install basic dev packages
apt-get install -y python-dev=2.7.9-1
apt-get install -y python-pip
apt-get install -y screen

# Install dependencies
pip install -I pymavlink==2.0.6 monotonic==1.2 pyserial==3.1.1

# Install aircraft communication packages
pip install -I dronekit==2.9.0 mavproxy==1.5.2

# Disable OS use of serial console and enable companion computer use
echo "Disabling serial console..."
raspi-config nonint do_serial 1
sed -Ei 's/enable_uart=0/enable_uart=1/g' /boot/config.txt

# Setup the host name and configure to connect to Frog automatically
echo "Running network setup..."
python configurations/network_setup.py $name

# Create custom aircraft directory structure
echo "Creating ~/custom_aircraft..."
mkdir -p $HOME/custom_aircraft/startup_scripts
mkdir $HOME/custom_aircraft/logs
echo "#!/bin/bash

for s in ~/custom_aircraft/startup_scripts/*.sh
do
	. \"\$s\"
done" > ~/custom_aircraft/run_directory.sh

ln -s $HOME/custom_aircraft/run_directory.sh $HOME/custom_aircraft/startup
chmod +x $HOME/custom_aircraft/run_directory.sh
cp startup_scripts/* $HOME/custom_aircraft/startup_scripts
cp configurations/mavinit.scr $HOME/.mavinit.scr
chmod +x $HOME/custom_aircraft/*.sh
chown -R pi $HOME/custom_aircraft

# Add startup scripts to boot
if (crontab -l | grep /home/pi/custom_aircraft/startup); 
then
    echo "Crontab already has startup link...";
else
    echo "Adding startup link to crontab...";
    (crontab -l ; echo \
        "@reboot sudo -iu pi /home/pi/custom_aircraft/startup") | \
    crontab -;
fi;
