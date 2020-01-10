#!/bin/bash

RED='\033[0;36m'
DarkGray='\033[1;30m'

_green() {
    printf '\033[1;31;32m'
    printf -- "%b" "$1"
    printf '\033[0m'
}

_red() {
    printf '\033[1;31;31m'
    printf -- "%b" "$1"
    printf '\033[0m'
}

_yellow() {
    printf '\033[1;31;33m'
    printf -- "%b" "$1"
    printf '\033[0m'
}

_purple() {
    printf "\033[0;35m$1"
}

_orange() {
    printf "\033[0;33m$1"
}

_Cyan() {
    printf "\033[0;36m$1"
}

_blue() {
    printf "\033[0;34m$1"
}

helpFunction()
{
   echo ""
   echo "Usage: $0 -a parameterA -b parameterB -c parameterC"
   echo -e "\t-a Description of what is parameterA"
   echo -e "\t-b Description of what is parameterB"
   echo -e "\t-c Description of what is parameterC"
   exit 1 # Exit script after printing help
}

# while getopts "a:b:c:" opt
# do
#    case "$opt" in
#       a ) parameterA="$OPTARG" ;;
#       b ) parameterB="$OPTARG" ;;
#       c ) parameterC="$OPTARG" ;;
#       ? ) helpFunction ;; # Print helpFunction in case parameter is non-existent
#    esac
# done

# # Print helpFunction in case parameters are empty
# if [ -z "$parameterA" ] || [ -z "$parameterB" ] || [ -z "$parameterC" ]
# then
#    echo "Some or all of the parameters are empty";
#    helpFunction
# fi


parse_input()
{
    local OPTIND
    while getopts "p:a:" OPTION
    do
        case "$opt" in
        a ) parameterA="$OPTARG" ;;
        p ) parameterB="$OPTARG" ;;
        esac
    done 
    _green "parameterA= ${parameterA} parameterB = ${parameterB}"   
}


 main(){
    _green "hey\n"
}


parse_input "$@"
main

# string='300-400'
# if [[ ! $string == *"-"* ]]; then
#   echo "It's there!"
# fi


# IP_WHITE_LIST=$parameterA
# echo $IP_WHITE_LIST
# # Begin script in case all parameters are correct
# _Cyan "$parameterA\n"
# _Cyan "$parameterB\n"
# _Cyan "$parameterC\n"




# Black        0;30     Dark Gray     1;30
# Red          0;31     Light Red     1;31
# Green        0;32     Light Green   1;32
# Brown/Orange 0;33     Yellow        1;33
# Blue         0;34     Light Blue    1;34
# Purple       0;35     Light Purple  1;35
# Cyan         0;36     Light Cyan    1;36
# Light Gray   0;37     White         1;37

# i=0;
# NC='\033[0m' # No Color
# WHITE='\033[0;107m'
# BIGreen='\033[1;92m' 
# printf "I ${DarkGray}love${NC} Stack Overflow\n"
# echo -e "I ${RED}love${NC} Stack Overflow"
# while [ $i -lt 8 ];
# do
# #    echo $i;
#    color1="\033[0;3"${i}"m"
#    color2="\033[1;3"${i}"m"
#    echo -e "I ${color1}love${WHITE} Stack Overflow"
#    echo -e "I ${color2}love${BIGreen} Stack Overflow"
# #    i=`expr $i + 1`;
#    # let i+=1; //这些都是让i自增的方式
# #    ((i++));
#    i=$[$i+1];
#    # i=$(( $i + 1 ))
# done
