#!/bin/bash
set -e
#set -x

IPSET_WHILTE_LIST="whitelist"
IPSET="/sbin/ipset"
TMPFILE=$(mktemp)

HOME_IP_RANGE = ['a','b','c','d']


. $(dirname "$0")/functions.sh




function processExistingTables() {
    local IPSET_OUTPUT="${IPSET} list ${IPSET_WHILTE_LIST}"
    local myarr = ($(echo IPSET_OUTPUT | awk '{if (NR>8) print $1 }' | awk -F '.' '{ printf "%s%s\n", $1, $2}' | sort | uniq))
    local array=( 'one' 'two' 'three' )
    
    for i in "${HOME_IP_RANGE[@]}"
    do
        echo $i
    done
}


function addMyHomeIpRangeToIpset(){

}

function main(){
    _green "this is imported funtions working \n"
    processExistingTables


    _red "yes imported is working\n"
}

function _batch_set_add(){
    ipset create spambots iphash
    iptables -A INPUT -m set --match-set spambots src -j DROP
    while read ip; do ipset add spambots "$ip"; done < ip_addresses.txt
}


main
