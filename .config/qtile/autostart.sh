#!/bin/sh
xbacklight -set 20
pulseaudio -D &
nitrogen --restore &
redshift-gtk &
nm-applet &
flameshot &
keepassxc &
synapse --startup &
picom --config .config/picom/picom.conf &
xautolock -time 5 -locker slock &
lxqt-policykit-agent &
