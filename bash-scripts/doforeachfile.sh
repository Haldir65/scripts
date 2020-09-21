
#!/bin/bash
set -e

echo "usage : bash $0 /abs/path/of/bash/script or command"

function entrance(){
    kcommand=$1
    for i in `ls -d */`; 
        do cd ${i} 
        $kcommand
        cd -;
    done
}

entrance $1


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