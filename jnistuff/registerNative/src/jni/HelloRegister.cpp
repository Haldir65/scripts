#include <jni.h>
#include <iostream>
#include <string>

JavaVM* g_jvm;

using namespace std;

// Method define start
void sayHello(){
   std::cout << "Hello there! from dynamic register" << std::endl;
}

void sayHello2(){
   std::cout << "Hello again \n how do " << std::endl;
}


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

namespace mmkv {
    #define MMKV_JNI static

   MMKV_JNI jint pageSize(JNIEnv *env, jclass type) {
        return 2210;
    }

    MMKV_JNI jboolean tryLock(JNIEnv *env, jobject instance) {
        return jboolean(true);
    }

    MMKV_JNI jboolean reKey(JNIEnv *env, jobject instance, jstring cryptKey) {
        std::string newKey;
        if (cryptKey) {
            newKey = jstring2string(env, cryptKey);
            std::cout << "cryptkey is " << newKey << std::endl;
        }
        return (jboolean) false;
    }

    MMKV_JNI jstring mmapID(JNIEnv *env, jobject instance) {
            std::string s("string from jni");
           return string2jstring(env, s);
    }


}

// Method define end

static const char * classPathName = "com/me/Hello";


static JNINativeMethod methods[] = {
    //java类native方法名|方法签名|Native实现方法名
	{"say","()V",(void*)sayHello},
    {"say2","()V",(void*)sayHello2},
    {"pageSize", "()I", (void *) mmkv::pageSize},
    {"tryLock", "()Z", (void *) mmkv::tryLock},
    {"reKey", "(Ljava/lang/String;)Z", (void *) mmkv::reKey},
    {"mmapID", "()Ljava/lang/String;", (void *) mmkv::mmapID},

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