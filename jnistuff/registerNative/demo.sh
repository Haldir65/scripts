#!/bin/bash

rm -rf  src/com/me/Hello.class src/*.o
CPPFLAG+="-std=c++14 -L. -Wall -pthread"
pushd src
javac com/me/Hello.java
rm -rf lib
mkdir -p lib

##mv HelloWorldJNI.class com/baeldung/jni/HelloWorldJNI.class
## javac -h . HelloWorldJNI.java create header file
## cd src && javah -d jni com.example.Hello  will create a jni folder in src
## and .h file like src/jni/com_example_Hello.h

## build dylib on macos
# g++ -c -fPIC -I${JAVA_HOME}/include -I${JAVA_HOME}/include/darwin jni/com_me_Hello.cpp -o com_me_Hello.o
# g++ -dynamiclib -o lib/libnative.dylib com_me_Hello.o -lc

g++ ${CPPFLAG} -c -fPIC -I${JAVA_HOME}/include -I${JAVA_HOME}/include/darwin jni/HelloRegister.cpp -o Helloregister.o
g++ ${CPPFLAG} -dynamiclib -o lib/libnative.dylib Helloregister.o -lc



HERE=$(pwd)
java -cp . -Djava.library.path=${HERE}/lib com.me.Hello
popd
