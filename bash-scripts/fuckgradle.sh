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

_using_sed_on_file(){
   gfile=$1
   if [ -f $gfile ];then
      sed -i --  's/compile /implementation /g' $gfile
      sed -i -- 's/testCompile /testImplementation /g' $gfile
      sed -i -- 's/androidCompile /androidTestImplementation /g' $gfile
      if [ -f ${gfile}-- ]; then
          #echo "exists"
          rm -rf ${gfile}--
      fi
   fi
}

_maybe_multiple_module(){
    mydir=`ls`
    for eachfile in $mydir
    do
        if [ -d "$eachfile" ] && [ -f "$eachfile"/build.gradle ]; then
            echo $eachfile/build.gradle
            _using_sed_on_file $eachfile/build.gradle
        fi
    done
}


echo "The script you are running has basename `basename "$0"`, dirname `dirname "$0"`"
echo "The present working directory is `pwd`"
THE_DIR_CONTAINING_THIS_SCRIPT=`dirname "$0"`
parentdir="$(dirname "$THE_DIR_CONTAINING_THIS_SCRIPT")"

## todo , change to abspath of python source file path
python3 $parentdir/python/fuckgradle.py


TARGET=app/build.gradle
if [ -f $TARGET ];then
   echo "sed start"
   _using_sed_on_file $TARGET
fi

_maybe_multiple_module




##excludeDomain
