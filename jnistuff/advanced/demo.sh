#!/bin/bash

rm -rf native com_baeldung_jni_ExampleParametersJNI.o

mkdir -p native
javac ExampleParametersJNI.java
mkdir -p com/baeldung/jni

mv ExampleParametersJNI.class com/baeldung/jni/ExampleParametersJNI.class
## javac -h . HelloWorldJNI.java create header file

## build dylib on macos
g++ -c -fPIC -I${JAVA_HOME}/include -I${JAVA_HOME}/include/darwin com_baeldung_jni_ExampleParametersJNI.cpp -o com_baeldung_jni_ExampleParametersJNI.o
g++ -dynamiclib -o libnative.dylib com_baeldung_jni_ExampleParametersJNI.o -lc

mv libnative.dylib native

HERE=$(pwd)
java -cp . -Djava.library.path=${HERE}/native com.baeldung.jni.ExampleParametersJNI
