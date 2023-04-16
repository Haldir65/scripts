
#!/bin/bash
set -e
# set -x

## tldr 
## failed

echo "1 . aim: usually we have multiple header for an http request, so try to use an for each to add head to a single curl call"




declare -a HEADERS=("\"accept: */*\"" 
            "\"accept-encoding: gzip, deflate, br\"" 
            "\"accept-language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7\""
            "\"dnt: 1\"" 
            "\"sec-ch-ua-mobile: ?0\""
            "\"sec-fetch-dest: script\""
            "\"sec-fetch-mode: no-cors\""
            "\"sec-fetch-site: cross-site\""
"\"user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36\"")


function _here_doc(){
    cat << _EOF_
    "-H accept-encoding: gzip, deflate, br"
    "accept-language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
_EOF_
}

function dumb_concat(){
    local url=$1
    args=""
    echo "1. prepare to make request to $url"
    for i in "${HEADERS[@]}"
    do
    args+="-H $i "
    # echo "$i"
    done
    # echo "result is ==="
    # echo "cur -i -X GET $args"
    # echo "result is ==="
    prefix="\'"
    suffix="\'"
    # args=${args#"$prefix"}
    # args=${args%"$suffix"}
    echo "$args"
    
    curl -i -X GET "$args" $url
    echo $args


    # prefix="hell"
    # suffix="ld"
    # string="hello-world"
    # foo=${string#"$prefix"}
    # foo=${foo%"$suffix"}
    # echo "${foo}"
}


function main() {
    # curl $(_here_doc) $1
     curl -i -X GET --compressed --http2-prior-knowledge -H "accept: */*"  -H "accept-language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7" -H "dnt: 1" -H "sec-ch-ua-mobile: ?0" -H "sec-fetch-dest: script" -H "sec-fetch-mode: no-cors" -H "sec-fetch-site: cross-site" -H "user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36" $1
}



main $1


