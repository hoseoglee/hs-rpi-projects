#!/usr/bin/env bash
# install python 3.7
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.7

python3.7 --version

sudo rm /usr/bin/python
sudo ln -s /usr/bin/python3 /usr/bin/python
