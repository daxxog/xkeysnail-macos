#!/bin/bash
set -x
pwd
sudo xhost + && sleep 3 && sudo systemctl restart xkeysnail
sudo systemctl status xkeysnail
