#!/bin/bash

source ./functions.sh


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


# parse_input "$@"
# main

#!/bin/bash

SHORT=p:,:,r
LONG=tutorial1:,tutorial2:,help
OPTS=$(getopt -a -n class --options $SHORT --longoptions $LONG -- "$@")

eval set -- "$OPTS"

while :
do
  case "$1" in
    -p | --tutorial1 )
      tutorial1="$2"
      shift 2
      ;;
    -q | --tutorial2 )
      tutorial2="$2"
      shift 2
      ;;
    -r | --help)
      "This is a class script"
      exit 2
      ;;
    --)
      shift;
      break
      ;;
    *)
      echo "Unexpected option: $1"
      ;;
  esac
done

echo $tutorial1, $tutorial2
# ) 

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
