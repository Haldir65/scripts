package com.me;
import java.lang.System;

public class Hello {
    public native void say();
    public native void say2();
    public native int pageSize();
    public native boolean tryLock();
    public native boolean reKey(String input);
    public native String mmapID();


    public static void main(String[] args) {
        System.loadLibrary("native");
        Hello hello = new Hello();
        hello.say();
        hello.say2();
        int size = hello.pageSize();
        System.out.println("size from jni is  " + size );
        boolean lockResult =  hello.tryLock();
        System.out.println("lockResult from jni is  " + lockResult );
        boolean reKey = hello.reKey(" ==== text from java === ");
        System.out.println("reKey from jni is  " + reKey );
        String mmapID = hello.mmapID();
        System.out.println("mmapID from jni is  " + mmapID );

    }
}