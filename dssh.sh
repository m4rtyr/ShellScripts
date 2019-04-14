#!/bin/bash


################
#
# Author: silentcat
# Date: 2018-07-11
# Description: Performs
# an SSH connection to a DigitalOcean
# droplet by correlating its name to an IP.
#
###############

if [[ $1 == "" ]]
then
	echo "Argument required: name of droplet."
	exit
fi

port=22

if [[ $2 != "" ]]
then
	port="$2"
fi

name=$(doctl compute droplet list | grep "$1" | awk '{ print $3 }')

if [[ $name == "" ]]
then
	echo "No droplet with name found."
	exit
fi

ssh silentcat@${name} -p $port
