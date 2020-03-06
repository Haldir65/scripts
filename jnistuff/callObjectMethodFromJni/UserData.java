package com.baeldung.jni;

public class UserData {
    
    public String name;
    public double balance;

    public UserData(){
        System.out.println("UserData constructor called!");// from jni this is not called
    }
    
    public String getUserInfo() {
        System.out.println("getUserInfo called!");
        return "[name]=" + name + ", [balance]=" + balance;
    }
}
