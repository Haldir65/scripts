#!/usr/bin/env bash
sed 's/\<server=\///g;s/\/114.114.114.114\>//'  direct.txt > direct3.txt
awk '{ printf "server=/%s/119.29.29.29\n", $1 }' direct3.txt > direct5.txt

## or you can can simpley call replace
# sed 's/\/114.114.114.114\>/\/119.29.29.29/'  direct.txt > direct6.txt
