#include "com_baeldung_jni_HelloWorldJNI.h"
#include <iostream>

/*
 * Class:     com_baeldung_jni_HelloWorldJNI
 * Method:    sayHello
 * Signature: ()V
 */
JNIEXPORT void JNICALL Java_com_baeldung_jni_HelloWorldJNI_sayHello
(JNIEnv* env, jobject thisObject) {
    std::string hello = "greeting from c++ code  !";
    std::cout << hello << std::endl;
}


