#!/bin/bash
set -e
#set -x

source ./functions.sh


##
# returns 1 if not empty
##
function _check_file_is_not_empty(){
    local FILENAME=$1
    # Check if the file is empty
    if [ $(wc -l < "${FILENAME}") -eq 0 ]; then
       # _green "\nFile $FILENAME is empty \n"
        echo 0
    else
        #_green "\nFile $FILENAME is not empty\n"
        echo 1
    fi
}


function _read_all_contents_of_file_line_by_line(){
   local FILENAME=$1
   local file_empty=$(_check_file_is_not_empty ${FILENAME})
   # _red "$file_empty \n"
    if [[ "$file_empty" -eq 1 ]];then
        _green "\nFile $FILENAME is not empty \n"
    else
        _red "\nFile $FILENAME is empty\n"
    fi
}


function _list_all_file_ends_with_txt() {
    # for i in *.sh; do
    # [ -f "$i" ] || break
    #     _green "found file ${i} \n "
    # done
    for i in `find . -name "*.sh" -type f`; do
        # _green "$i\n"
        _read_all_contents_of_file_line_by_line "$i"
    done    
}


function main(){
    _list_all_file_ends_with_txt
    _green "all done\n"
}

main
