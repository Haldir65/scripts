#!/bin/bash
set -e
set -x

TARGET_FILE=${PWD}/some.zip

DOWN_LOAD_URL="https://github.com/v2ray/v2ray-core/releases/download/v4.21.3/v2ray-linux-mips.zip"

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

function checkFileExists(){
    ## 文件不存在
    if [ ! -f $TARGET_FILE ]; then
        _Cyan "file not exists, start downloading\n"
        wget -O $TARGET_FILE ${DOWN_LOAD_URL}
    else
        _Cyan "file exists\n"    
    fi
}

checkFileExists