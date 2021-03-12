#!/bin/bash
. $(dirname "$0")/functions.sh

# Define the menu list here

## https://github.com/garypang13/OpenWrt/blob/master/onekey/compile.sh

function _show_all_options()
{
    echo "
1. X86_64
2. K2p
3. RedMi_AC2100
4. r2s
5. r4s
6. newifi-d2
7. XY-C5
8. Exit
"

while :; do

read -p "你想要编译哪个固件？ " CHOOSE

case $CHOOSE in
	1)
		firmware="x86_64"
		echo "this is awesome"
	break
	;;
	2)
		firmware="phicomm-k2p"
	break
	;;
	3)
		firmware="redmi-ac2100"
	break
	;;
	4)
		firmware="nanopi-r2s"
	break
	;;
	5)
		firmware="nanopi-r4s"
	break
	;;
	6)
		firmware="newifi-d2"
	break
	;;
	7)
		firmware="XY-C5"
	break
	;;
	8)	exit 0
	;;

esac
done
}



function main(){
	_show_all_options
}

main
_green "selected firmware is $firmware " 
_green "\n"