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

IGNORE_DIRS=(AwesomeProject C InstantGLSL shadowsocks-android testapplication)


_update_all_git_repo_in_curdir(){
    _green "==we will start update all git repo in curdir ==  \n"
    mydir=`ls`
    for eachfile in $mydir
    do
        if [ -d "$eachfile" ] && [ -d "$eachfile"/.git ]; then
            if [[ " ${IGNORE_DIRS[@]} " =~ " ${eachfile} " ]]; then
                _yellow "== skip directory "${eachfile}" because it was in IGNORE_DIRS\n"
                 # whatever you want to do when arr contains value
            else
                cd $eachfile
                ##git status
                _green "== entering "${eachfile}" ====\n"
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
                _green "== leaving "${eachfile}" ==== \n"
                cd ..
            fi
        fi
    done
    _green "completed! \n"
}

_update_all_git_repo_in_curdir
# var="name"
# array=(nam3 name sa name)
# for i in ${array[@]}
# do
#    [ "$i" == "$var" ] && echo "yes"
# done

# value=nam3
# if [[ " ${array[@]} " =~ " ${value} " ]]; then
#     # whatever you want to do when arr contains value
#     echo "contains "${value}
# fi
# value=nsasa
# if [[ ! " ${array[@]} " =~ " ${value} " ]]; then
#     echo "not containes arr "$value
#     # whatever you want to do when arr doesn't contain value
# fi
