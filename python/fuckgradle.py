#!/usr/bin/env python3


import logging ,os , fileinput
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove
import re
import mmap
# create logger

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


## target files
LARGE_GRADLE_FILE = "build.gradle"
GRADLE_WRAPPER_FILES = "gradle/wrapper/gradle-wrapper.properties"
APP_BUILD_GRADLE_FILE = "app/build.gradle"


## ext.kotlin_version = '1.3.61'

EXT_KOTLIN_PATTERN="ext.kotlin_version"
EXT_KOTLIN_PATTERN_REPLACEMENT="    ext.kotlin_version = '1.4.21'"


GRALDE_PATTERN="classpath 'com.android.tools.build:gradle:" ## implementation 'com.android.tools.build:gradle:4.1.1' in gradle plugin shouldn't match
GRALDE_PATTERN_REPLACEMENT="classpath 'com.android.tools.build:gradle:4.1.1'"



GRADLE_WRAPPER_PATTERN="distributionUrl=https\://services.gradle.org/distributions/"
GRADLE_WRAPPER_PATTERN_REPLACEMENT="distributionUrl=https\://services.gradle.org/distributions/gradle-6.5-bin.zip"


COMPILESDK_PATTERN="compileSdkVersion"
COMPILESDK_PATTERN_REPLACEMENT="    compileSdkVersion 30"

BUILD_TOOLS_PATTERN="buildToolsVersion"
BUILD_TOOLS_PATTERN_REPLACEMENT="    buildToolsVersion '30.0.3'"

DNK_PATTERN = "ndkVersion"
NDK_PATTERN_REPLACEMENT = "ndkVersion '22.0.7026061'"

COMPILE_SUPPORT_V7_PATTERN="com.android.support:appcompat-v7"
COMPILE_SUPPORT_V7_PATTERN_REPLACEMENT="        implementation 'com.android.support:appcompat-v7:28.0.0'"

COMPILE_SUPPORT_RECYCLER_VIEW_PATTERN="com.android.support:recyclerview-v7"
COMPILE_SUPPORT_RECYCLER_VIEW_PATTERN_REPLACEMENT="        implementation 'com.android.support:recyclerview-v7:28.0.0'"

RECYCLERVIEW_PATTERN_ANDROIDX="androidx.recyclerview:recyclerview"
RECYCLERVIEW_PATTERN_ANDROIDX_REPLACEMENT="implementation 'androidx.recyclerview:recyclerview:1.1.0'"


CONSTRAINT_LAYOUT="androidx.constraintlayout:constraintlayout"
CONSTRAINT_LAYOUT_REPLACEMENT="    implementation 'androidx.constraintlayout:constraintlayout:2.0.4'"




GLIDE_PATTERN="com.github.bumptech.glide:glide"
GLIDE_PATTERN_REPLACEMENT="    implementation 'com.github.bumptech.glide:glide:4.11.0'"

GLIDE_COMPILER="com.github.bumptech.glide:compiler"
GLIDE_COMPILER_REPLACEMENT="annotationProcessor 'com.github.bumptech.glide:compiler:4.9.0'"

OKHTTP3_PATTERN="com.squareup.okhttp3:okhttp:"
OKHTTP3_PATTERN_REPLACEMENT="    implementation 'com.squareup.okhttp3:okhttp:3.11.0'"

RXJAVA_PATTERN="io.reactivex.rxjava2:rxjava"
RXJAVA_PATTERN_REPLACEMENT="    implementation 'io.reactivex.rxjava2:rxjava:2.2.6'"

RX_ANDROID_PATTERN="io.reactivex.rxjava2:rxandroid"
RX_ANDROID_PATTERN_REPLACEMENT="    implementation 'io.reactivex.rxjava2:rxandroid:2.1.1'"

RETROFIT_PATTERN="com.squareup.retrofit2:retrofit"
RETROFT_PATTERN_REPLACEMENT="    implementation 'com.squareup.retrofit2:retrofit:2.5.0'"


TEST_RUNNNER_PATTERN="com.android.support.test:runner"
TEST_RUNNNER_PATTERN_REPLACEMENT="    androidTestImplementation 'com.android.support.test:runner:1.0.2'"

ESPRESSO_LATEST_VERSION="3.3.0"

TEST_ESPRESSO_PATTERN="com.android.support.test.espresso:espresso-core"
TEST_ESPRESSO_PATTERN_REPLACEMENT="androidTestImplementation 'com.android.support.test.espresso:espresso-core:${ESPRESSO_LATEST_VERSION}'"

TEST_ESPRESSO_PATTERN_X="androidx.test.espresso:espresso-core"
TEST_ESPRESSO_PATTERN_X_REPLACEMENT="androidTestImplementation 'androidx.test.espresso:espresso-core:${ESPRESSO_LATEST_VERSION}'"


TEST_JUNIT_PATTERN="androidx.test.ext:junit"
TEST_JUNIT_PATTERN_REPLACEMENT="androidTestImplementation 'androidx.test.ext:junit:1.1.2'"

ANDROID_SUPPORT_DESIGN_PATTERN="com.android.support:design:"
ANDROID_SUPPORT_DESIGN_PATTERN_REPLACEMENT="    implementation 'com.android.support:design:28.0.0'"

ANDROID_SUPPORT_GRIDLAYOUT_PATTERN="com.android.support:gridlayout-v7"
ANDROID_SUPPORT_GRIDLAYOUT_PATTERN_REPLACEMENT="    implementation 'com.android.support:gridlayout-v7:28.0.0'"

ANDROID_SUPPORT_PALETTE_PATTERN="com.android.support:palette-v7"
ANDROID_SUPPORT_PALETTE_PATTERN_REPLACEMENT="    implementation 'com.android.support:palette-v7:28.0.0'"


ANDROID_SUPPORT_V4_PATTERN="com.android.support:support-v4:"
ANDROID_SUPPORT_V4_REPLACEMENT="    implementation 'com.android.support:support-v4:28.0.0'"


JUNIT_PATTER="junit:junit:"
JUNIT_PATTER_REPLACE_MENT="    testImplementation 'junit:junit:4.13.1'"

ANDROIDX_APPCOMPAT="androidx.appcompat:appcompat"
ANDROIDX_APPCOMPAT_REPLACEMENT="    implementation 'androidx.appcompat:appcompat:1.2.0'"

GOOGLE_MATERIAL="com.google.android.material:material"
GOOGLE_MATERIAL_REPLACEMENT="    implementation 'com.google.android.material:material:1.2.1'"

KOTLINX_COROUTINE_PATTERN="org.jetbrains.kotlinx:kotlinx-coroutines-android"
KOTLINX_COROUTINE_PATTERN_REPLACEMENT="implementation 'org.jetbrains.kotlinx:kotlinx-coroutines-android:1.3.0'"

ANDROID_KTX_PATTERN="androidx.core:core-ktx"
ANDROID_KTX_PATTERN_REPLACEMENT="implementation 'androidx.core:core-ktx:1.3.2'"

CARD_VIEW_PATTERN_SUPPORT="com.android.support:cardview"
CARD_VIEW_PATTERN_SUPPORT_REPLACEMENT="implementation 'com.android.support:cardview-v7:28.0.0'"

CARD_VIEW_PATTERN="androidx.cardview:cardview"
CARD_VIEW_PATTERN_REPLACEMENT="    implementation 'androidx.cardview:cardview:1.0.0'"


REPLACEMENT_DICT_1 = {EXT_KOTLIN_PATTERN:EXT_KOTLIN_PATTERN_REPLACEMENT
            ,GRALDE_PATTERN:GRALDE_PATTERN_REPLACEMENT}


REPLACEMENT_DICT_2 = {GRADLE_WRAPPER_PATTERN:GRADLE_WRAPPER_PATTERN_REPLACEMENT}

REPLACEMENT_DICT_3 = {COMPILESDK_PATTERN:COMPILESDK_PATTERN_REPLACEMENT,
    BUILD_TOOLS_PATTERN:BUILD_TOOLS_PATTERN_REPLACEMENT,
    COMPILE_SUPPORT_V7_PATTERN:COMPILE_SUPPORT_V7_PATTERN_REPLACEMENT,
    RECYCLERVIEW_PATTERN_ANDROIDX:RECYCLERVIEW_PATTERN_ANDROIDX_REPLACEMENT,
    CONSTRAINT_LAYOUT:CONSTRAINT_LAYOUT_REPLACEMENT,
    ANDROIDX_APPCOMPAT:ANDROIDX_APPCOMPAT_REPLACEMENT,
    GOOGLE_MATERIAL:GOOGLE_MATERIAL_REPLACEMENT,
    CARD_VIEW_PATTERN_SUPPORT:CARD_VIEW_PATTERN_SUPPORT_REPLACEMENT,
    CARD_VIEW_PATTERN:CARD_VIEW_PATTERN_REPLACEMENT,
    JUNIT_PATTER:JUNIT_PATTER_REPLACE_MENT,
    TEST_RUNNNER_PATTERN:TEST_RUNNNER_PATTERN_REPLACEMENT,
    GLIDE_PATTERN:GLIDE_PATTERN_REPLACEMENT,
    OKHTTP3_PATTERN:OKHTTP3_PATTERN_REPLACEMENT,
    RXJAVA_PATTERN:RXJAVA_PATTERN_REPLACEMENT,
    RX_ANDROID_PATTERN:RX_ANDROID_PATTERN_REPLACEMENT,
    RETROFIT_PATTERN:RETROFT_PATTERN_REPLACEMENT,
    COMPILE_SUPPORT_RECYCLER_VIEW_PATTERN:COMPILE_SUPPORT_RECYCLER_VIEW_PATTERN_REPLACEMENT,
    GRALDE_PATTERN:GRALDE_PATTERN_REPLACEMENT,
    ANDROID_SUPPORT_DESIGN_PATTERN:ANDROID_SUPPORT_DESIGN_PATTERN_REPLACEMENT,
    ANDROID_SUPPORT_V4_PATTERN:ANDROID_SUPPORT_V4_REPLACEMENT,
    DNK_PATTERN:NDK_PATTERN_REPLACEMENT,
    TEST_JUNIT_PATTERN:TEST_JUNIT_PATTERN_REPLACEMENT,
    ANDROID_KTX_PATTERN:ANDROID_KTX_PATTERN_REPLACEMENT,
    KOTLINX_COROUTINE_PATTERN:KOTLINX_COROUTINE_PATTERN_REPLACEMENT,
    ANDROID_SUPPORT_GRIDLAYOUT_PATTERN:ANDROID_SUPPORT_GRIDLAYOUT_PATTERN_REPLACEMENT,
    ANDROID_SUPPORT_PALETTE_PATTERN:ANDROID_SUPPORT_PALETTE_PATTERN_REPLACEMENT
    }

def ndkVersionIsMissingInDefaultConfig(file_path):
    with open(file_path, 'rb', 0) as file,\
        mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
        if (s.find(b'defaultConfig') != -1 and s.find(b'ndkVersion') == -1 and s.find(b'CMakeLists.txt') !=-1):
            return True
        else:
            return False

## if(file_path.__contains__("gradle")):
 ##       print ('required ndkversion {0} for file {1} '.format(ndkVersionMissing(file_path),file_path))            


def workAroundForAndroidTestExcludeLine(oldLine):
    if oldLine.endswith('{\n') and "(" and ","  and (TEST_ESPRESSO_PATTERN or TEST_ESPRESSO_PATTERN_X) in oldLine: #  androidTestImplementation('com.android.support.test.espresso:espresso-core:2.2.2', {
        latest_version = ESPRESSO_LATEST_VERSION
        startIndex = oldLine.index(':')
        endIndex = oldLine.rindex("'")
        newLine = latest_version.join([oldLine[:startIndex+1],oldLine[endIndex:]])
        newLine = newLine.replace("androidTestCompile", "androidTestImplementation")
        #print("we take special care for espresso ,replace  line {0} to {1}".format(oldLine,newLine))
        # print("{0} workaroundFor AndroidTestExclude end!".format(oldLine));
        return newLine ,True
    else:
        return oldLine ,False   


def joinStrings(num_space):
    r = ''
    for i in range(0,num_space):
        r +=(' ')
    return r

def replace(file_path, userdict):
    #Create temp file
    fh, abs_path = mkstemp()
    needInsertNdkVersion = ndkVersionIsMissingInDefaultConfig(file_path)
    with fdopen(fh,'w',encoding='utf-8') as new_file:
        with open(file_path,'r',encoding='utf-8') as old_file:
            keys = userdict.keys()
            for line in old_file:
                found = False
                for key in keys:
                    if key in line :
                        white_space_num = line.index(line.lstrip())
                        content_to_write = joinStrings(white_space_num)+userdict[key].lstrip()
                        new_file.write(content_to_write)
                        new_file.write('\n')
                        # print ('found key  {0}, replace with {1}'.format(key , userdict[key]))
                        found = True
                        break
                    else:
                        pass
                        # print("failed to found {0} in {1} ".format(key, line))
                if not found:
                    # print("not found at line {0}".format(line))
                    exludePattern ,foundExclude = workAroundForAndroidTestExcludeLine(line)
                    if foundExclude:
                        new_file.write(exludePattern)
                        found = True
                    if needInsertNdkVersion and "compileSdkVersion" in line:
                        new_file.write(line)
                        white_space_num = line.index(line.lstrip())
                        content_to_write = joinStrings(white_space_num)+NDK_PATTERN_REPLACEMENT
                        new_file.write(content_to_write)
                        new_file.write('\n')
                        print("add {0} to android block of file {1} automaticly ".format(NDK_PATTERN_REPLACEMENT,file_path))
                        found = True;
                if not found:
                    new_file.write(line)

    #Copy the file permissions from the old file to the new file
    copymode(file_path, abs_path)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)

def filter_large_gradle():
    print("start==")
    replace(LARGE_GRADLE_FILE,REPLACEMENT_DICT_1)
    print("end==")


def filter_gradle_wrapper():
    print("start==")
    replace(GRADLE_WRAPPER_FILES,REPLACEMENT_DICT_2)
    print("end==")


def filter_app_build_gradle():
    print("start==")
    replace(APP_BUILD_GRADLE_FILE,REPLACEMENT_DICT_3)
    print("start==")

def handle_one_android_app(dirPath):
    gradlefile = os.path.join(dirPath,"build.gradle")
    gradle_wrapper_file = os.path.join(dirPath,"gradle/wrapper/gradle-wrapper.properties")
    inner_gradle_file = os.path.join(dirPath,"app/build.gradle")
    if(os.path.exists(gradlefile)):
        # print('file  {0}  exists '.format(gradlefile))
        replace(gradlefile,REPLACEMENT_DICT_1)
    if(os.path.exists(gradle_wrapper_file)):
        # print('file  {0}  exists '.format(gradlefile))
        replace(gradle_wrapper_file,REPLACEMENT_DICT_2)
    if(os.path.exists(inner_gradle_file)):
        # print('file  {0}  exists '.format(gradlefile))
        replace(inner_gradle_file,REPLACEMENT_DICT_3)



def maybe_multiple_module():
    dirs = os.listdir()
    pwd = os.getcwd()
    for file in dirs:
        abspath = os.path.join(pwd,file)
        if (os.path.isdir(file) and os.path.exists(abspath)):
            gradlefile = os.path.join(abspath,"build.gradle")
            gradle_wrapper_file = os.path.join(abspath,"gradle/wrapper/gradle-wrapper.properties")
            if(os.path.exists(gradlefile) or os.path.exists(gradle_wrapper_file)):
                handle_one_android_app(abspath)
            #     # print('file  {0}  exists '.format(gradlefile))
            #     replace(gradlefile,REPLACEMENT_DICT_3)
            # if(os.path.exists(gradle_wrapper_file)):
            #     # print('file  {0}  exists '.format(gradlefile))
            #     replace(gradle_wrapper_file,REPLACEMENT_DICT_2)

def maybe_module_not_called_app():
    dirs = os.listdir()
    pwd = os.getcwd()
    for file in dirs:
        abspath = os.path.join(pwd,file)
        if (os.path.isdir(file) and os.path.exists(abspath)):
            gradlefile = os.path.join(abspath,"build.gradle")
            if(os.path.exists(gradlefile) ):
                print ('start processing  {0} '.format(os.path.abspath(gradlefile)))
                replace(os.path.abspath(gradlefile),REPLACEMENT_DICT_3)
                print ('end processing  {0} '.format(os.path.abspath(gradlefile)))

def main():
    if(os.path.exists(LARGE_GRADLE_FILE)):
        print ('start processing File {0} {1}'.format(LARGE_GRADLE_FILE,"===="))
        filter_large_gradle()
    else:
        print ('File {0} {1}'.format(LARGE_GRADLE_FILE,"not exists"))

    if(os.path.exists(GRADLE_WRAPPER_FILES)):
        print ('start processing File {0} {1}'.format(GRADLE_WRAPPER_FILES,"===="))
        filter_gradle_wrapper()
    else:
        print ('File {0} {1}'.format(GRADLE_WRAPPER_FILES,"not exists"))

    if(os.path.exists(APP_BUILD_GRADLE_FILE)):
        print ('start processing File {0} {1}'.format(APP_BUILD_GRADLE_FILE,"===="))
        filter_app_build_gradle()
    else:
        maybe_module_not_called_app()    
        print ('File {0} {1}'.format(APP_BUILD_GRADLE_FILE,"not exists"))
    maybe_multiple_module()


if __name__ == "__main__":
    main()



