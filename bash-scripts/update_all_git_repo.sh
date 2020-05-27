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



_update_all_git_repo_in_curdir(){
    _green "we will start update all git repo in curdir \n"
    mydir=`ls`
    for eachfile in $mydir
    do
        if [ -d "$eachfile" ] && [ -d "$eachfile"/.git ]; then
            cd $eachfile
            ##git status
            if [ -z "$(git status --porcelain)" ]; then 
            # Working directory clean
                _yellow "nothing has changed in $eachfile\n"
                git pull
            else 
                _red "something has changed in $eachfile\n"
                git stash
                git pull
                git stash pop
                echo "end of push"
            fi
            cd ..
        fi
    done
    _green "completed! \n"
}

_update_all_git_repo_in_curdir

