/**
 * @author Dmitrijs Lobanovskis
 * @since 03/03/2016.
 */
package com.example;
import java.lang.reflect.Field;

public class Main {



    public static void main(String[] args) throws Exception{

        SomeClass someClass = new SomeClass();
        System.out.println(someClass);

        Field field = someClass.getClass().getDeclaredField("str");
        field.setAccessible(true);

        field.set(someClass, "There you are");


        System.out.println(someClass);
    }



}