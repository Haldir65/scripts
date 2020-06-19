
#!/bin/bash
set -e

## for directory
#for i in `ls -d */`; do cd ${i} && fuckgradle.sh && cd ..;done

## for file ends with .gz
#for i in `ls *.gz`; do echo ${i};done

##对每一个文件夹进行操作
##for i in `ls -d */`; do echo ${i} && cd ${i} && fuckgradle.sh && cd ..;done