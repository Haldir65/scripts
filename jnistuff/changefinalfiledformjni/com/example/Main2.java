/**
 * @author Dmitrijs Lobanovskis
 * @since 03/03/2016.
 */
package com.example;

public class Main2 {


    public static void main(String[] args) throws Exception{

        SomeClass someClass = new SomeClass();
        System.out.println(someClass);

        someClass.say();

        someClass.setOut0("say unmodifiable again?");

        System.out.println(someClass);
    }


    
}