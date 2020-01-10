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

EXCLUDE_DOMAIN_FILE="exclude.domains"
DOMAIN_TEMP_FILE="domain.file.tmp"
DOMAIN_FILE="domain.txt"


function excludeDomain(){
    touch ${EXCLUDE_DOMAIN_FILE}
    touch ${DOMAIN_TEMP_FILE}
    touch ${DOMAIN_FILE}
     # Delete exclude domains
    if [ ! -z $EXCLUDE_DOMAIN_FILE ]; then
        for line in $(cat $EXCLUDE_DOMAIN_FILE)
        do
            cat $DOMAIN_TEMP_FILE | grep -vF -f $EXCLUDE_DOMAIN_FILE > $DOMAIN_FILE
        done
        printf 'Domains in exclude domain file '$EXCLUDE_DOMAIN_FILE'... ' && _green 'Deleted\n'
    else
        cat $DOMAIN_TEMP_FILE > $DOMAIN_FILE
    fi
}

##excludeDomain