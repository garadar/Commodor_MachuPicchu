#!/bin/bash 

echo "Hello World!"
apptainer pull docker://ghcr.io/apptainer/lolcow
apptainer exec lolcow_latest.sif cowsay "Commodor MachuPicchu invading $HOSTNAME"
