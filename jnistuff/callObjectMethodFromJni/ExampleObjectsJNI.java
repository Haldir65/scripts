package com.baeldung.jni;

public class ExampleObjectsJNI {

    static {
        System.loadLibrary("native");
    }
    
    public static void main(String[] args) {
        ExampleObjectsJNI instance = new ExampleObjectsJNI();
        UserData newUser = instance.createUser("John Sammy", 450.67);
        System.out.println("hey");
        instance.printUserData(newUser);
        System.out.println("hey "+newUser.getUserInfo());
    }
    
    public native UserData createUser(String name, double balance);
    
    public native String printUserData(UserData user);

}
