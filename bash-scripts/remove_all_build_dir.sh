
#!/bin/bash
set -e
source ./functions.sh


function removeBuildDir(){
    if [ -d ${1}app/build ] ; then
        rm -rf ${1}app/build
        echo "${1}app/build removed"
    fi
}

_green "remove all app/build dir , usage :\n bash $0"
_green "\n or you can simply use one command"
_green "\n find . -type d -name 'build' -exec rm -r {} \;"

rootdir=`pwd`
for i in `ls -d */`; do cd ${rootdir}/${i} && removeBuildDir ${rootdir}/${i} && cd ..;done



_blue "done"


## for directory
#for i in `ls -d */`; do cd ${i} && fuckgradle.sh && cd ..;done

## for file ends with .gz
#for i in `ls *.gz`; do echo ${i};done

##对每一个文件夹进行操作
##for i in `ls -d */`; do echo ${i} && cd ${i} && fuckgradle.sh && cd ..;done

#!/bin/bash
# declare an array called array and define 3 vales
# array=( one two three )
# for i in "${array[@]}"
# do
# 	echo $i
# done
