#!/bin/bash

rm -rf native com_baeldung_jni_ExampleObjectsJNI.o

mkdir -p native
javac ExampleObjectsJNI.java UserData.java
mkdir -p com/baeldung/jni

mv ExampleObjectsJNI.class com/baeldung/jni/ExampleObjectsJNI.class
mv UserData.class com/baeldung/jni/UserData.class

## javac -h . ExampleObjectsJNI.java UserData.java 可以创建头文件
## javac 编译多个java文件 javac Main.java pojo.java xxx.java 

## build dylib on macos
g++ -c -fPIC -I${JAVA_HOME}/include -I${JAVA_HOME}/include/darwin com_baeldung_jni_ExampleObjectsJNI.cpp -o com_baeldung_jni_ExampleObjectsJNI.o
g++ -dynamiclib -o libnative.dylib com_baeldung_jni_ExampleObjectsJNI.o -lc

mv libnative.dylib native

HERE=$(pwd)
java -cp . -Djava.library.path=${HERE}/native com.baeldung.jni.ExampleObjectsJNI
