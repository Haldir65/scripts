#!/usr/bin/env python3


import logging ,os , fileinput
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove
import re
# create logger

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


## target files
LARGE_GRADLE_FILE = "build.gradle"
GRADLE_WRAPPER_FILES = "gradle/wrapper/gradle-wrapper.properties"
APP_BUILD_GRADLE_FILE = "app/build.gradle"


## ext.kotlin_version = '1.3.61'

EXT_KOTLIN_PATTERN="ext.kotlin_version"
EXT_KOTLIN_PATTERN_REPLACEMENT="    ext.kotlin_version = '1.4.10'"


GRALDE_PATTERN="com.android.tools.build:gradle"
GRALDE_PATTERN_REPLACEMENT="        classpath 'com.android.tools.build:gradle:4.0.0'"


GRADLE_WRAPPER_PATTERN="distributionUrl=https\://services.gradle.org/distributions/"
GRADLE_WRAPPER_PATTERN_REPLACEMENT="distributionUrl=https\://services.gradle.org/distributions/gradle-6.2-bin.zip"


COMPILESDK_PATTERN="compileSdkVersion"
COMPILESDK_PATTERN_REPLACEMENT="    compileSdkVersion 30"

BUILD_TOOLS_PATTERN="buildToolsVersion"
BUILD_TOOLS_PATTERN_REPLACEMENT="    buildToolsVersion '30.0.2'"

COMPILE_SUPPORT_V7_PATTERN="com.android.support:appcompat-v7"
COMPILE_SUPPORT_V7_PATTERN_REPLACEMENT="        implementation 'com.android.support:appcompat-v7:28.0.0'"

COMPILE_SUPPORT_RECYCLER_VIEW_PATTERN="com.android.support:recyclerview-v7"
COMPILE_SUPPORT_RECYCLER_VIEW_PATTERN_REPLACEMENT="        implementation 'com.android.support:recyclerview-v7:28.0.0'"

CONSTRAINT_LAYOUT="com.android.support.constraint:constraint-layout"
CONSTRAINT_LAYOUT_REPLACEMENT="    implementation 'com.android.support.constraint:constraint-layout:1.1.3'"

GLIDE_PATTERN="com.github.bumptech.glide:glide"
GLIDE_PATTERN_REPLACEMENT="    implementation 'com.github.bumptech.glide:glide:4.11.0'"

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

TEST_ESPRESSO_PATTERN="com.android.support.test.espresso:espresso-core"
TEST_ESPRESSO_PATTERN_REPLACEMENT="    androidTestImplementation 'com.android.support.test.espresso:espresso-core:3.0.2'"

ANDROID_SUPPORT_DESIGN_PATTERN="com.android.support:design:"
ANDROID_SUPPORT_DESIGN_PATTERN_REPLACEMENT="    implementation 'com.android.support:design:28.0.0'"


JUNIT_PATTER="junit:junit:"
JUNIT_PATTER_REPLACE_MENT="    testImplementation 'junit:junit:4.13'"

ANDROIDX_APPCOMPAT="androidx.appcompat:appcompat"
ANDROIDX_APPCOMPAT_REPLACEMENT="    implementation 'androidx.appcompat:appcompat:1.2.0'"

GOOGLE_MATERIAL="com.google.android.material:material"
GOOGLE_MATERIAL_REPLACEMENT="    implementation 'com.google.android.material:material:1.2.1'"



REPLACEMENT_DICT_1 = {EXT_KOTLIN_PATTERN:EXT_KOTLIN_PATTERN_REPLACEMENT
            ,GRALDE_PATTERN:GRALDE_PATTERN_REPLACEMENT}


REPLACEMENT_DICT_2 = {GRADLE_WRAPPER_PATTERN:GRADLE_WRAPPER_PATTERN_REPLACEMENT}

REPLACEMENT_DICT_3 = {COMPILESDK_PATTERN:COMPILESDK_PATTERN_REPLACEMENT,
    BUILD_TOOLS_PATTERN:BUILD_TOOLS_PATTERN_REPLACEMENT,
    COMPILE_SUPPORT_V7_PATTERN:COMPILE_SUPPORT_V7_PATTERN_REPLACEMENT,
    CONSTRAINT_LAYOUT:CONSTRAINT_LAYOUT_REPLACEMENT,
    ANDROIDX_APPCOMPAT:ANDROIDX_APPCOMPAT_REPLACEMENT,
    GOOGLE_MATERIAL:GOOGLE_MATERIAL_REPLACEMENT,
    JUNIT_PATTER:JUNIT_PATTER_REPLACE_MENT,
    TEST_RUNNNER_PATTERN:TEST_RUNNNER_PATTERN_REPLACEMENT,
    TEST_ESPRESSO_PATTERN:TEST_ESPRESSO_PATTERN_REPLACEMENT,
    GLIDE_PATTERN:GLIDE_PATTERN_REPLACEMENT,
    OKHTTP3_PATTERN:OKHTTP3_PATTERN_REPLACEMENT,
    RXJAVA_PATTERN:RXJAVA_PATTERN_REPLACEMENT,
    RX_ANDROID_PATTERN:RX_ANDROID_PATTERN_REPLACEMENT,
    RETROFIT_PATTERN:RETROFT_PATTERN_REPLACEMENT,
    COMPILE_SUPPORT_RECYCLER_VIEW_PATTERN:COMPILE_SUPPORT_RECYCLER_VIEW_PATTERN_REPLACEMENT,
    GRALDE_PATTERN:GRALDE_PATTERN_REPLACEMENT,
    ANDROID_SUPPORT_DESIGN_PATTERN:ANDROID_SUPPORT_DESIGN_PATTERN_REPLACEMENT
    }


def replace(file_path, userdict):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            keys = userdict.keys()
            for line in old_file:
                found = False
                for key in keys:
                    if key in line :
                        new_file.write(userdict[key])
                        new_file.write('\n')
                        # print ('found key  {0}, replace with {1}'.format(key , userdict[key]))
                        found = True
                        break
                    else:
                        pass
                        # print("failed to found {0} in {1} ".format(key, line))
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


def maybe_multiple_module():
    dirs = os.listdir()
    pwd = os.getcwd()
    for file in dirs:
        abspath = os.path.join(pwd,file)
        if (os.path.isdir(file) and os.path.exists(abspath)):
            gradlefile = os.path.join(abspath,"build.gradle")
            if(os.path.exists(gradlefile)):
                # print('file  {0}  exists '.format(gradlefile))
                replace(gradlefile,REPLACEMENT_DICT_3)
            gradle_wrapper_file = os.path.join(abspath,"gradle/wrapper/gradle-wrapper.properties")
            if(os.path.exists(gradle_wrapper_file)):
                # print('file  {0}  exists '.format(gradlefile))
                replace(gradle_wrapper_file,REPLACEMENT_DICT_2)


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
        print ('File {0} {1}'.format(APP_BUILD_GRADLE_FILE,"not exists"))
    maybe_multiple_module()


if __name__ == "__main__":
    main()



