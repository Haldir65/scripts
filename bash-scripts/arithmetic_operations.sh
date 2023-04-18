#!/usr/bin/env bash
source ./functions.sh

## 基本的加减乘除

function _show_basic_actions(){
    let NUMBER1=10
    let NUMBER2=3

    # Addition => + operator
    let ADD=$NUMBER1+$NUMBER2
    _green "Addition of two numbers : ${ADD} \n"

    # Subtraction => - operator
    let SUB=$NUMBER1-$NUMBER2
    _red "Subtraction of two numbers : ${SUB} \n"

    # Multiply => * operator
    let MUL=$NUMBER1*$NUMBER2
    _blue "Multiply two numbers : ${MUL} \n"

    # Divide => / operator
    let DIV=$NUMBER1/$NUMBER2
    _purple "Division of two numbers : ${DIV} \n"

    # Remainder => % operator
    let REM=$NUMBER1%$NUMBER2
    _Cyan "Remainder of two numbers : ${REM} \n"

    # Exponent => ** operator
    let EXPO=$NUMBER1**$NUMBER2
    _purple "Exponent of two numbers : ${EXPO} \n"

    echo $1
    echo $2

    let a=$1
    let b=$2

    echo ${a}
    echo ${b}

    let Mul2=$a*$b
    _yellow "Multiple result is $Mul2 \n"
}


function _sleep_time(){
    _orange "will sleep for $1m or $1h "
    # let hour="${$1}h"
    # let min="${$1}m"
    # let second="${$1}s"
    # _green "hour = ${hour} \n"
    # _green "second = ${second} \n"
    # _green "min = ${min} \n"
    # sleep $second
}   

function main() {
    _show_basic_actions $1 $2
    _sleep_time $1
}

main $1 $2

##  bash arithmetic_operations.sh 7 10


# let a = $1
# let b = $2
# _yellow "a = ${a} b = ${b}"
# let Mul2=$a*$b
# _yellow "Multiple i s $Mul2"
