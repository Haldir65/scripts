#!/usr/bin/env bash
# sed 's/\<server=\///g;s/\/114.114.114.114\>//'  direct.txt > direct3.txt
# awk '{ printf "server=/%s/119.29.29.29\n", $1 }' direct3.txt > direct5.txt

## or you can can simpley call replace
# sed 's/\/114.114.114.114\>/\/119.29.29.29/'  direct.txt > direct6.txt


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


python3 /Users/jingweima/Documents/github/scripts/python/fuckgradle.py
sed -i --  's/compile /implementation /g' app/build.gradle
sed -i --  's/testCompile /testImplementation /g' app/build.gradle
sed -i --  's/androidTestCompile /androidTestImplementation /g' app/build.gradle




##excludeDomain
