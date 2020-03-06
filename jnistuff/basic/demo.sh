#!/bin/bash

rm -rf native com com_baeldung_jni_HelloWorldJNI.o

mkdir -p native
javac HelloWorldJNI.java
mkdir -p com/baeldung/jni

mv HelloWorldJNI.class com/baeldung/jni/HelloWorldJNI.class
## javac -h . HelloWorldJNI.java create header file

## build dylib on macos
g++ -c -fPIC -I${JAVA_HOME}/include -I${JAVA_HOME}/include/darwin com_baeldung_jni_HelloWorldJNI.cpp -o com_baeldung_jni_HelloWorldJNI.o
g++ -dynamiclib -o libnative.dylib com_baeldung_jni_HelloWorldJNI.o -lc

mv libnative.dylib native

HERE=$(pwd)
java -cp . -Djava.library.path=${HERE}/native com.baeldung.jni.HelloWorldJNI
