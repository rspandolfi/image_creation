#!/bin/bash

# Installs on top of Raspbian Jessie

apt-get update

# Set up text editor
apt-get install -y vim
cp vimrc ~/.vimrc

# Install basic dev packages
apt-get install -y python-dev=2.7.9-1
apt-get install -y python-pip

# Install dependencies
pip install -I pymavlink==2.0.5 monotonic==0.6 pyserial==3.1.1

# Install aircraft communication packages
pip install -I dronekit==2.8.0 mavproxy==1.5.1

