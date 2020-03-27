#include <jni.h>
#include <iostream>
#include <string>

JavaVM* g_jvm;

using namespace std;

static string jstring2string(JNIEnv *env, jstring str) {
    if (str) {
        const char *kstr = env->GetStringUTFChars(str, nullptr);
        if (kstr) {
            string result(kstr);
            env->ReleaseStringUTFChars(str, kstr);
            return result;
        }
    }
    return "";
}

static jstring string2jstring(JNIEnv *env, const string &str) {
    return env->NewStringUTF(str.c_str());
}



/*
 * The following three functions implement setter methods for
 * java.lang.System.{in, out, err}. They are natively implemented
 * because they violate the semantics of the language (i.e. set final
 * variable).
 */
// JNIEXPORT void JNICALL
// Java_java_lang_System_setOut0(JNIEnv *env, jclass cla, jobject stream)
// {
//     jfieldID fid =
//         (*env)->GetStaticFieldID(env,cla,"out","Ljava/io/PrintStream;");
//     if (fid == 0)
//         return;
//     (*env)->SetStaticObjectField(env,cla,fid,stream);
// }


void setOut0(JNIEnv *env, jobject obj, jstring str_){
    jclass cls = env->GetObjectClass(obj);
   // jclass cls = env->FindClass("com/example/SomeClass"); //也行

    
    jfieldID fieldId = env->GetFieldID(cls,"str","Ljava/lang/String;");
    if(fieldId == NULL) {
        std::cout << "failed to find jfieldID" << std::endl;
        return;
    }

    std:string arg = jstring2string(env, str_);
    std::cout << "setout0 called! with arguments " << arg << std::endl;
    
    // jstring jstr = env->NewStringUTF("123");
    env->SetObjectField(obj, fieldId, str_);
}


// Method define start
void sayHello(){
   std::cout << "Hello there! we will modify java final field from jni!" << std::endl;
}




// Method define end

static const char * classPathName = "com/example/SomeClass";


static JNINativeMethod methods[] = {
    //java类native方法名|方法签名|Native实现方法名
	{"say","()V",(void*)sayHello},
	{"setOut0","(Ljava/lang/String;)V",(void*)setOut0},
};

JNIEXPORT jint JNI_OnLoad(JavaVM *vm, void *reserved)
{
    JNIEnv* env;
    // 1.获取JNI环境对象
    if (JNI_OK != vm->GetEnv(reinterpret_cast<void**> (&env),JNI_VERSION_1_6)) {
        //LOGW("JNI_OnLoad could not get JNI env");
        return JNI_ERR;
    }
    g_jvm = vm;
    // 2.获取Java Native类
    jclass clazz = env->FindClass(classPathName);
    if (clazz == NULL) {
        return JNI_ERR;
    }
    // 3.调用RegisterNatives注册Native方法
    if (env->RegisterNatives(clazz, methods, sizeof(methods)/sizeof((methods)[0])) < 0) {
        return JNI_ERR;
    }
    return JNI_VERSION_1_6;
}