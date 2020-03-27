/**
 * @author Dmitrijs Lobanovskis
 * @since 03/03/2016.
 */
package com.example;

public class SomeClass {


    static {
        System.loadLibrary("native");
    }

    public native void setOut0(String str);
    public native void say();

    private final String str;
   

    SomeClass(){
        this.str = "This is the string that never changes!";
    }

    public String getStr() {
        return str;
    }

    @Override
    public String toString() {
        return "Class name: " + getClass() + " Value: " + getStr();
    }
}