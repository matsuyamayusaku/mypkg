#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch mypkg random_anpan.launch.py > /tmp/mypkg2.log

cat /tmp/mypkg2.log |
grep 'Listen: 10'
