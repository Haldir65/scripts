#!/bin/bash

make clean

rm -rf lib/*
mkdir -p lib
javac com/example/Main2.java com/example/SomeClass.java -d target/

# javac ExampleObjectsJNI.java UserData.java
# mkdir -p com/baeldung/jni

# mv ExampleObjectsJNI.class com/baeldung/jni/ExampleObjectsJNI.class
# mv UserData.class com/baeldung/jni/UserData.class

## javac -h . ExampleObjectsJNI.java UserData.java 可以创建头文件
## javac 编译多个java文件 javac Main.java pojo.java xxx.java 

## build dylib on macos
g++ -c -fPIC -I${JAVA_HOME}/include -I${JAVA_HOME}/include/darwin jni/Reflecting.cpp -o reflecting.o
g++ -dynamiclib -o lib/libnative.dylib reflecting.o -lc

HERE=$(pwd)
##java -cp target -Djava.library.path=${HERE}/lib com.exmaple.Main2
java -cp target:. -Djava.library.path=${HERE}/lib com.example.Main2