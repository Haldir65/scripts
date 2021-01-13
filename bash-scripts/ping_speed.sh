#!/bin/zsh
## use zsh since it support float comparasion natively

. $(dirname "$0")/functions.sh

DOMAIN=www.baidu.com
OPTIMAL_LATENCY=1000 ## ms

function _ping_host (){
    latency=$( ping -c 4 $DOMAIN | tail -1| awk '{print $4}' | cut -d '/' -f 2)
    _green "current latency is $latency \n"
    if (( $latency < $OPTIMAL_LATENCY ));then
        _green "low latency to $DOMAIN\n "
    else
        _yellow "horrible latency to $DOMAIN\n"
    fi
    ## Just use ksh (ksh93 precisely) or zsh, which both natively support floating point arithmetics:
    # bash support integer comparasion only
}

function main(){
    _read_file_line_by_line `pwd`/functions.sh
}


main








