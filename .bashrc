#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='\[\033[01;32m\]\u@\h \W\$\[\033[00m\] '



### ALIAS PERSO ###

alias gg="ping gentoo.org"
alias ll="ls -l"
alias reseau="nmap -sL 192.168.1.1-255"
alias reseau-virt="nmap -sL 192.168.100.1-255"
alias vi="vim"
alias cpu--="sudo cpupower --cpu all frequency-set -g powersave"
alias cpu+-="sudo cpupower --cpu all frequency-set -g schedutil"
alias cpu++="sudo cpupower --cpu all frequency-set -g performance"
alias cpu="cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"
alias ssh-rpi="ssh thib@176.139.132.55 -p 52415"
alias music="ncmpcpp"
