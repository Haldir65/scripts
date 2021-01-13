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

function _str_is_empty() {
    st=$1
    if [ -z "$1" ]; then
       return 1
    else
       return 0 
    fi
}

function file_exists() {
    if [ ! -f $1 ]; then
        return 0
    else
        return 1
    fi
}

_read_file_line_by_line() {
    filename="$1"
    while read name; do
        _green "$name\n"
    done < $filename
}