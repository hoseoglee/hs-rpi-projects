#!/bin/sh

git -C ~/hs-rpi-projects/rpi-tool/ add .
git -C ~/hs-rpi-projects/rpi-tool/ commit -am update
git -C ~/hs-rpi-projects/rpi-tool/ push
