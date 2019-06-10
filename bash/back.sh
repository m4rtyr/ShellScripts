#!/usr/bin/env bash

# @Author: S. Sharma <silentcat>
# @Date:   2019-04-13T19:41:26-05:00
# @Email:  silentcat@protonmail.com
# @Last modified by:   silentcat
# @Last modified time: 2019-04-13T20:07:50-05:00

num=1
if [[ $1 -ge $num ]]
then
  num=${1}
fi

prev_dir=$(pwd)
for (( i=0; i < $num; i++ )); do
  prev_dir="${prev_dir%/*}"
  if [[ $prev_dir == $HOME || $prev_dir == "" ]]
  then
    break
  fi
done

cd $prev_dir
