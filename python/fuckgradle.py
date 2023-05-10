#!/usr/bin/env python3


from inspect import CO_ITERABLE_COROUTINE
import logging ,os , fileinput
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove
import re
import mmap

## [python print with color](https://stackoverflow.com/a/65860612)
class colors: # You may need to change color settings
    RED = '\033[31m'
    ENDC = '\033[m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'

def _red(str):
    print(colors.RED + str + colors.ENDC)

def _green(str):
    print(colors.GREEN + str + colors.ENDC)

def _yellow(str):
    print(colors.YELLOW + str + colors.ENDC)

def _blue(str):
    print(colors.BLUE + str + colors.ENDC)


# create logger

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


## target files
LARGE_GRADLE_FILE = "build.gradle"
GRADLE_WRAPPER_FILES = "gradle/wrapper/gradle-wrapper.properties"
APP_BUILD_GRADLE_FILE = "app/build.gradle"


## ext.kotlin_version = '1.3.61'


KOTLIN_VERSION="1.8.21"
EXT_KOTLIN_PATTERN="ext.kotlin_version"
EXT_KOTLIN_PATTERN_REPLACEMENT="    ext.kotlin_version = '{0}'".format(KOTLIN_VERSION)


GRALDE_PATTERN="classpath 'com.android.tools.build:gradle:" ## implementation 'com.android.tools.build:gradle:4.1.1' in gradle plugin shouldn't match
GRALDE_PATTERN_REPLACEMENT="classpath 'com.android.tools.build:gradle:8.0.1'"

JETBRAIN_GRALDE_PATTERN="classpath 'org.jetbrains.kotlin:kotlin-gradle-plugin:" ## implementation 'com.android.tools.build:gradle:4.1.1' in gradle plugin shouldn't match
JETBRAIN_GRALDE_PATTERN_REPLACEMENT="classpath 'org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version'"

GRADLE_WRAPPER_PATTERN="distributionUrl=https\://services.gradle.org/distributions/"
GRADLE_WRAPPER_PATTERN_ALTER="distributionUrl=https://services.gradle.org/distributions/"
GRADLE_WRAPPER_PATTERN_REPLACEMENT="distributionUrl=https\://services.gradle.org/distributions/gradle-8.0.2-all.zip"


COMPILESDK_PATTERN="compileSdkVersion"
COMPILESDK_PATTERN_REPLACEMENT="    compileSdkVersion 33"

TARGETSDK_PATTERN="targetSdkVersion"
TARGETSDK_PATTERN_REPLACEMENT="    targetSdkVersion 29"


MIN_SDK_VERSION_PATTERN="minSdkVersion"
MIN_SDK_VERSION_PATTERN_REPLACEMENT="minSdkVersion 27"


BUILD_TOOLS_PATTERN="buildToolsVersion"
BUILD_TOOLS_PATTERN_REPLACEMENT="    buildToolsVersion '33.0.2'"

DNK_PATTERN = "ndkVersion"
NDK_PATTERN_REPLACEMENT = "ndkVersion '25.1.8937393'"
MAVEN_CENTRAL = "mavenCentral()"
JCENTER = "jcenter()"
GOOGLE = "google()"



COMPILE_SUPPORT_V7_PATTERN="com.android.support:appcompat-v7"
COMPILE_SUPPORT_V7_PATTERN_REPLACEMENT="        implementation 'com.android.support:appcompat-v7:28.0.0'"

COMPILE_SUPPORT_RECYCLER_VIEW_PATTERN="com.android.support:recyclerview-v7"
COMPILE_SUPPORT_RECYCLER_VIEW_PATTERN_REPLACEMENT="        implementation 'com.android.support:recyclerview-v7:28.0.0'"

RECYCLERVIEW_PATTERN_ANDROIDX="androidx.recyclerview:recyclerview"
RECYCLERVIEW_PATTERN_ANDROIDX_REPLACEMENT="implementation 'androidx.recyclerview:recyclerview:1.3.0'"


CONSTRAINT_LAYOUT="androidx.constraintlayout:constraintlayout"
CONSTRAINT_LAYOUT_REPLACEMENT="    implementation 'androidx.constraintlayout:constraintlayout:2.1.4'"

CONSTRAINT_LAYOUT_SUPPORT="com.android.support.constraint:constraint-layout"
CONSTRAINT_LAYOUT_SUPPORT_REPLACEMENT="    implementation 'com.android.support.constraint:constraint-layout:2.0.4'"


ANDROIDX_ANNOTATION_PATTERN="androidx.annotation:annotation"
ANDROIDX_ANNOTATION_PATTERN_REPLACEMENT="implementation 'androidx.annotation:annotation:1.2.0'"


GLIDE_PATTERN="com.github.bumptech.glide:glide"
GLIDE_PATTERN_REPLACEMENT="    implementation 'com.github.bumptech.glide:glide:4.12.0'"

GLIDE_COMPILER="com.github.bumptech.glide:compiler"
GLIDE_COMPILER_REPLACEMENT="annotationProcessor 'com.github.bumptech.glide:compiler:4.9.0'"

OKHTTP3_PATTERN="com.squareup.okhttp3:okhttp:"
OKHTTP3_PATTERN_REPLACEMENT="    implementation 'com.squareup.okhttp3:okhttp:4.10.0'"

RXJAVA_PATTERN="io.reactivex.rxjava2:rxjava"
RXJAVA_PATTERN_REPLACEMENT="    implementation 'io.reactivex.rxjava2:rxjava:2.2.17'"

RX_ANDROID_PATTERN="io.reactivex.rxjava2:rxandroid"
RX_ANDROID_PATTERN_REPLACEMENT="    implementation 'io.reactivex.rxjava2:rxandroid:2.1.1'"


RETROFIT_PATTERN="com.squareup.retrofit2:retrofit"
RETROFT_PATTERN_REPLACEMENT="    implementation 'com.squareup.retrofit2:retrofit:2.9.0'"

RETROFIT_GSON_PATTERN="com.squareup.retrofit2:converter-gson"
RETROFT_GSON_PATTERN_REPLACEMENT="implementation 'com.squareup.retrofit2:converter-gson:2.9.0'"


TEST_RUNNNER_PATTERN="com.android.support.test:runner"
TEST_RUNNNER_PATTERN_REPLACEMENT="    androidTestImplementation 'com.android.support.test:runner:1.0.2'"

ESPRESSO_LATEST_VERSION="3.5.1"

TEST_ESPRESSO_PATTERN="com.android.support.test.espresso:espresso-core"
TEST_ESPRESSO_PATTERN_REPLACEMENT="androidTestImplementation 'com.android.support.test.espresso:espresso-core:{0}'".format(ESPRESSO_LATEST_VERSION)

TEST_ESPRESSO_PATTERN_X="androidx.test.espresso:espresso-core"
TEST_ESPRESSO_PATTERN_X_REPLACEMENT="androidTestImplementation 'androidx.test.espresso:espresso-core:{0}'".format(ESPRESSO_LATEST_VERSION)


TEST_JUNIT_PATTERN="androidx.test.ext:junit"
TEST_JUNIT_PATTERN_REPLACEMENT="androidTestImplementation 'androidx.test.ext:junit:1.1.5'"

ANDROID_SUPPORT_DESIGN_PATTERN="com.android.support:design:"
ANDROID_SUPPORT_DESIGN_PATTERN_REPLACEMENT="    implementation 'com.android.support:design:28.0.0'"

ANDROID_SUPPORT_GRIDLAYOUT_PATTERN="com.android.support:gridlayout-v7"
ANDROID_SUPPORT_GRIDLAYOUT_PATTERN_REPLACEMENT="    implementation 'com.android.support:gridlayout-v7:28.0.0'"

ANDROID_SUPPORT_PALETTE_PATTERN="com.android.support:palette-v7"
ANDROID_SUPPORT_PALETTE_PATTERN_REPLACEMENT="    implementation 'com.android.support:palette-v7:28.0.0'"


ANDROID_SUPPORT_V4_PATTERN="com.android.support:support-v4:"
ANDROID_SUPPORT_V4_REPLACEMENT="    implementation 'com.android.support:support-v4:28.0.0'"


JUNIT_PATTER="junit:junit:"
JUNIT_PATTER_REPLACE_MENT="    testImplementation 'junit:junit:4.13.2'"

ANDROIDX_APPCOMPAT="androidx.appcompat:appcompat"
ANDROIDX_APPCOMPAT_REPLACEMENT="    implementation 'androidx.appcompat:appcompat:1.6.1'"

GOOGLE_MATERIAL="com.google.android.material:material"
GOOGLE_MATERIAL_REPLACEMENT="    implementation 'com.google.android.material:material:1.8.0'"

KOTLINX_COROUTINE_PATTERN="org.jetbrains.kotlinx:kotlinx-coroutines-android"
KOTLINX_COROUTINE_PATTERN_REPLACEMENT="implementation 'org.jetbrains.kotlinx:kotlinx-coroutines-android:1.6.4'"

KOTLINX_COROUTINE_CORE_PATTERN="org.jetbrains.kotlinx:kotlinx-coroutines-core"
KOTLINX_COROUTINE_CORE_PATTERN_REPLACEMENT="implementation 'org.jetbrains.kotlinx:kotlinx-coroutines-core:1.6.4'"

KOTLIN_REFLECT_PATTERN="org.jetbrains.kotlin:kotlin-reflect"
KOTLIN_REFLECT_PATTERN_REPLACEMENT="implementation 'org.jetbrains.kotlin:kotlin-reflect:1.7.20'"

KOTLINX_ATOMIC_FU_PATTERN="org.jetbrains.kotlinx:atomicfu"
KOTLINX_ATOMIC_FU_PATTERN_REPLACEMENT="implementation 'org.jetbrains.kotlinx:atomicfu:0.18.5'"

JETBRAIN_KOTLIN_STDLIB_7="org.jetbrains.kotlin:kotlin-stdlib-jdk7:"
JETBRAIN_KOTLIN_STDLIB_8="implementation \"org.jetbrains.kotlin:kotlin-stdlib-jdk8:$kotlin_version\""

ANDROID_KTX_PATTERN="androidx.core:core-ktx"
ANDROID_KTX_PATTERN_REPLACEMENT="implementation 'androidx.core:core-ktx:1.10.0'"

ANDROID_ACTIVITY_KTX_PATTERN="androidx.activity:activity-ktx"
ANDROID_ACTIVITY_KTX_PATTERNN_REPLACEMENT="implementation 'androidx.activity:activity-ktx:1.7.1'"

CARD_VIEW_PATTERN_SUPPORT="com.android.support:cardview"
CARD_VIEW_PATTERN_SUPPORT_REPLACEMENT="implementation 'com.android.support:cardview-v7:28.0.0'"

CARD_VIEW_PATTERN="androidx.cardview:cardview"
CARD_VIEW_PATTERN_REPLACEMENT="implementation 'androidx.cardview:cardview:1.0.0'"

FRAGMENT_KTX = "androidx.fragment:fragment-ktx:"
FRAGMENT_KTX_REPLACEMENT = "implementation 'androidx.fragment:fragment-ktx:1.5.6'"

NAVIGATION_FRAGMENT_KTX_PATTERN="androidx.navigation:navigation-fragment-ktx"
NAVIGATION_FRAGMENT_KTX_PATTERN_REPLACEMENT="implementation 'androidx.navigation:navigation-fragment-ktx:2.5.3'"

NAVIGATION_UI_KTX_PATTERN="androidx.navigation:navigation-ui-ktx"
NAVIGATION_UI_KTX_PATTERN_REPLACEMENT="implementation 'androidx.navigation:navigation-ui-ktx:2.5.3'"

lifecycle_version = "2.6.1"
arch_version = "2.1.0"


COMPILE_OPTION_17_HERE_DOCUMENT = """
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_17
        targetCompatibility JavaVersion.VERSION_17
    }

    kotlinOptions {
        jvmTarget = JavaVersion.VERSION_17
    }
"""

JAVA_TOOL_CHAIN_17 = """
    java {
        toolchain.languageVersion.set(JavaLanguageVersion.of(17))
    }
"""

ENABLE_VIEWBINDING_HERE_DOCUMENT = """
    buildFeatures {
        viewBinding true
        buildConfig false
    }
"""

ANDROID_LIFE_LIVEDATA_PATTERN="androidx.lifecycle:lifecycle-livedata-ktx:"
ANDROID_LIFE_LIVEDATA_PATTERN_REPLACEMENT="implementation 'androidx.lifecycle:lifecycle-livedata-ktx:{0}'".format(lifecycle_version)


LIFECYCLE_VIEWMODEL_KTX_PATTERN="androidx.lifecycle:lifecycle-viewmodel-ktx:"
LIFECYCLE_VIEWMODEL_KTX_PATTERN_REPLACE_MENT="implementation 'androidx.lifecycle:lifecycle-viewmodel-ktx:{0}'".format(lifecycle_version)

LIFECYCLE_VIEWMODEL_PATTERN="androidx.lifecycle:lifecycle-viewmodel:"
LIFECYCLE_VIEWMODEL_PATTERN_REPLACE_MENT="implementation 'androidx.lifecycle:lifecycle-viewmodel:{0}'".format(lifecycle_version)

LIFECYCLE_LIVE_DATA_PATTERN="androidx.lifecycle:lifecycle-livedata:"
LIFECYCLE_LIVE_DATA_PATTERN_REPLACE_MENT="implementation 'androidx.lifecycle:lifecycle-livedata:{0}'".format(lifecycle_version)

LIFECYCLE_RUNTIME_PATTERN="androidx.lifecycle:lifecycle-runtime:"
LIFECYCLE_RUNTIME_PATTERN_REPLACE_MENT="implementation 'androidx.lifecycle:lifecycle-runtime:{0}'".format(lifecycle_version)

LIFECYCLE_RUNTIME_KTX_PATTERN="androidx.lifecycle:lifecycle-runtime-ktx:"
LIFECYCLE_RUNTIME_KTX_PATTERN_REPLACE_MENT="implementation 'androidx.lifecycle:lifecycle-runtime-ktx:{0}'".format(lifecycle_version)


LIFECYCLE_SM_SAVED_STATE_PATTERN="androidx.lifecycle:lifecycle-viewmodel-savedstate:"
LIFECYCLE_SM_SAVED_STATE_PATTERN_REPLACE_MENT="implementation 'androidx.lifecycle:lifecycle-viewmodel-savedstate:{0}'".format(lifecycle_version)

ANDROIDX_ROOM_RUNTIME="androidx.room:room-runtime:"
ANDROIDX_ROOM_RUNTIME_REPLACE_MENT="implementation 'androidx.room:room-runtime:2.5.1'"


EXO_PLAYER_CORE="com.google.android.exoplayer:exoplayer-core"
EXO_PLAYER_CORE_REPLACE_MENT="implementation 'com.google.android.exoplayer:exoplayer-core:2.15.1'"

EXO_PLAYER_UI="'com.google.android.exoplayer:exoplayer-ui";
EXO_PLAYER_UI_REPLACE_MENT="implementation 'com.google.android.exoplayer:exoplayer-ui:2.15.1'";

REPLACEMENT_DICT_1 = {EXT_KOTLIN_PATTERN:EXT_KOTLIN_PATTERN_REPLACEMENT
            ,GRALDE_PATTERN:GRALDE_PATTERN_REPLACEMENT,
            JETBRAIN_GRALDE_PATTERN:JETBRAIN_GRALDE_PATTERN_REPLACEMENT}


REPLACEMENT_DICT_2 = {GRADLE_WRAPPER_PATTERN:GRADLE_WRAPPER_PATTERN_REPLACEMENT,
                      GRADLE_WRAPPER_PATTERN_ALTER:GRADLE_WRAPPER_PATTERN_REPLACEMENT
                    }

REPLACEMENT_DICT_3 = {COMPILESDK_PATTERN:COMPILESDK_PATTERN_REPLACEMENT,
    MIN_SDK_VERSION_PATTERN:MIN_SDK_VERSION_PATTERN_REPLACEMENT,
    TARGETSDK_PATTERN:TARGETSDK_PATTERN_REPLACEMENT,
    BUILD_TOOLS_PATTERN:BUILD_TOOLS_PATTERN_REPLACEMENT,
    COMPILE_SUPPORT_V7_PATTERN:COMPILE_SUPPORT_V7_PATTERN_REPLACEMENT,
    JETBRAIN_KOTLIN_STDLIB_7:JETBRAIN_KOTLIN_STDLIB_8,
    RECYCLERVIEW_PATTERN_ANDROIDX:RECYCLERVIEW_PATTERN_ANDROIDX_REPLACEMENT,
    CONSTRAINT_LAYOUT:CONSTRAINT_LAYOUT_REPLACEMENT,
    CONSTRAINT_LAYOUT_SUPPORT:CONSTRAINT_LAYOUT_SUPPORT_REPLACEMENT,
    ANDROIDX_APPCOMPAT:ANDROIDX_APPCOMPAT_REPLACEMENT,
    ANDROIDX_ANNOTATION_PATTERN:ANDROIDX_ANNOTATION_PATTERN_REPLACEMENT,
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
    RETROFIT_GSON_PATTERN:RETROFT_GSON_PATTERN_REPLACEMENT,
    COMPILE_SUPPORT_RECYCLER_VIEW_PATTERN:COMPILE_SUPPORT_RECYCLER_VIEW_PATTERN_REPLACEMENT,
    GRALDE_PATTERN:GRALDE_PATTERN_REPLACEMENT,
    ANDROID_SUPPORT_DESIGN_PATTERN:ANDROID_SUPPORT_DESIGN_PATTERN_REPLACEMENT,
    ANDROID_SUPPORT_V4_PATTERN:ANDROID_SUPPORT_V4_REPLACEMENT,
    DNK_PATTERN:NDK_PATTERN_REPLACEMENT,
    TEST_JUNIT_PATTERN:TEST_JUNIT_PATTERN_REPLACEMENT,
    ANDROID_KTX_PATTERN:ANDROID_KTX_PATTERN_REPLACEMENT,
    ANDROID_LIFE_LIVEDATA_PATTERN:ANDROID_LIFE_LIVEDATA_PATTERN_REPLACEMENT,
    ANDROID_ACTIVITY_KTX_PATTERN:ANDROID_ACTIVITY_KTX_PATTERNN_REPLACEMENT,
    KOTLINX_COROUTINE_PATTERN:KOTLINX_COROUTINE_PATTERN_REPLACEMENT,
    KOTLIN_REFLECT_PATTERN:KOTLIN_REFLECT_PATTERN_REPLACEMENT,
    KOTLINX_ATOMIC_FU_PATTERN:KOTLINX_ATOMIC_FU_PATTERN_REPLACEMENT,
    ANDROID_SUPPORT_GRIDLAYOUT_PATTERN:ANDROID_SUPPORT_GRIDLAYOUT_PATTERN_REPLACEMENT,
    ANDROID_SUPPORT_PALETTE_PATTERN:ANDROID_SUPPORT_PALETTE_PATTERN_REPLACEMENT,
    NAVIGATION_FRAGMENT_KTX_PATTERN:NAVIGATION_FRAGMENT_KTX_PATTERN_REPLACEMENT,
    FRAGMENT_KTX:FRAGMENT_KTX_REPLACEMENT,
    NAVIGATION_UI_KTX_PATTERN:NAVIGATION_UI_KTX_PATTERN_REPLACEMENT,
    LIFECYCLE_VIEWMODEL_KTX_PATTERN:LIFECYCLE_VIEWMODEL_KTX_PATTERN_REPLACE_MENT,
    LIFECYCLE_VIEWMODEL_PATTERN:LIFECYCLE_VIEWMODEL_PATTERN_REPLACE_MENT,
    LIFECYCLE_LIVE_DATA_PATTERN:LIFECYCLE_LIVE_DATA_PATTERN_REPLACE_MENT,
    LIFECYCLE_RUNTIME_PATTERN:LIFECYCLE_RUNTIME_PATTERN_REPLACE_MENT,
    LIFECYCLE_RUNTIME_KTX_PATTERN:LIFECYCLE_RUNTIME_KTX_PATTERN_REPLACE_MENT,
    LIFECYCLE_SM_SAVED_STATE_PATTERN:LIFECYCLE_SM_SAVED_STATE_PATTERN_REPLACE_MENT,
    ANDROIDX_ROOM_RUNTIME:ANDROIDX_ROOM_RUNTIME_REPLACE_MENT,
    EXO_PLAYER_CORE:EXO_PLAYER_CORE_REPLACE_MENT,
    EXO_PLAYER_UI:EXO_PLAYER_UI_REPLACE_MENT
    }


def compat_api_or_implementation(line, newline,filename):
    if('api' in line):
        return newline.replace('implementation', 'api')
    else:
        return newline


def readFileContent(file_abspath):
    with open(file_abspath,"r",encoding='utf-8') as f:
        content = f.read()
        return content


def text_file_contains_keywords(file_abspath,keywords):
    with open(file_abspath,"r",encoding='utf-8') as f:
        content = f.read()
        for kwd in keywords:
            if not kwd in content:
                return False
        return True

def buildToolsVersionIsMissingInandroidBlock(file_path):
    with open(file_path, 'rb', 0) as file,\
        mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
        if (s.find(b'compileSdkVersion') != -1 and s.find(b'buildToolsVersion') == -1 and s.find(b'defaultConfig') !=-1):
            return True
        else:
            return False        

def ndkVersionIsMissingInDefaultConfig(file_path):
    with open(file_path, 'rb', 0) as file,\
        mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
        if (s.find(b'defaultConfig') != -1 and s.find(b'ndkVersion') == -1 and (s.find(b'CMakeLists.txt') !=-1 or s.find(b'externalNativeBuild') !=-1)):
            return True
        else:
            return False

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
    elif TEST_ESPRESSO_PATTERN in oldLine:
        latest_version = ESPRESSO_LATEST_VERSION
        startIndex = oldLine.rindex(':')
        endIndex = oldLine.rindex("'")
        newLine = latest_version.join([oldLine[:startIndex+1],oldLine[endIndex:]])
        newLine = newLine.replace("androidTestCompile", "androidTestImplementation")
        return newLine ,True
    elif TEST_ESPRESSO_PATTERN_X in oldLine:
        latest_version = ESPRESSO_LATEST_VERSION
        startIndex = oldLine.rindex(':')
        endIndex = oldLine.rindex("'")
        newLine = latest_version.join([oldLine[:startIndex+1],oldLine[endIndex:]])
        newLine = newLine.replace("androidTestCompile", "androidTestImplementation")
        return newLine ,True
    else:
        return oldLine ,False


def joinStrings(num_space):
    r = ''
    for i in range(0,num_space):
        r +=(' ')
    return r

## unused , just for template
def template_for_replace_certain_word_in_file(file_path):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w',encoding='utf-8') as new_file:
        with open(file_path,'r',encoding='utf-8') as old_file:
            for line in old_file:
                # new_file.write(line.replace(pattern, subst))
                new_file.write(line)
    #Copy the file permissions from the old file to the new file
    copymode(file_path, abs_path)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)

def line_count_of_text_file(file_path):
    with open(file = file_path,encoding='utf-8') as f:
        count = sum(1 for _ in f)
        return count



def handle_gradle_wrapper_file(file_path):
    #Create temp file
    fh, abs_path = mkstemp()
    userdict = REPLACEMENT_DICT_2
    keys = userdict.keys()
    linecount = line_count_of_text_file(file_path= file_path)
    with fdopen(fh,'w',encoding='utf-8') as new_file:
        with open(file_path,'r',encoding='utf-8') as old_file:
            for index, line in enumerate(old_file):
                white_space_num = line.index(line.lstrip())
                key = next((x for x in keys if x in line), None) ## firstOccurence in list
                if key:
                    new_file.write(joinStrings(white_space_num)+userdict[key].lstrip())
                    if not (index == linecount -1) :
                        new_file.write("\n") ## skip write line break if this is last line
                else:
                    new_file.write(line)
    #Copy the file permissions from the old file to the new file
    copymode(file_path, abs_path)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)


def handle_large_build_gradle_file(file_path):
    userdict = REPLACEMENT_DICT_1
    keys = userdict.keys()
    fh, abs_path = mkstemp()
    fcontent = readFileContent(file_abspath= file_path)
    needInsertMavenCentral = MAVEN_CENTRAL not in fcontent
    needInsertGoogle =  GOOGLE not in fcontent
    with fdopen(fh,'w',encoding='utf-8') as new_file:
        with open(file_path,'r',encoding='utf-8') as old_file:
            for line in old_file:
                white_space_num = line.index(line.lstrip())
                key = next((x for x in keys if x in line), None) ## firstOccurence in list
                if key:
                    content_to_write = joinStrings(white_space_num)+userdict[key].lstrip()
                    new_file.write(content_to_write)
                    new_file.write('\n')
                    pass
                elif JCENTER in line:
                    _green("removing JCENTER from file {0} automaticly now that jcenter is closed ".format(file_path))
                    pass ## 
                elif "repositories" in line and (needInsertGoogle or needInsertMavenCentral):
                    new_file.write(line)
                    if needInsertGoogle:
                        new_file.write(joinStrings(white_space_num+4)+GOOGLE)
                        new_file.write('\n')
                    if needInsertMavenCentral:
                        new_file.write(joinStrings(white_space_num+4)+MAVEN_CENTRAL)
                    new_file.write('\n')
                else:
                    new_file.write(line)
    #Copy the file permissions from the old file to the new file
    copymode(file_path, abs_path)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)

def add_essential_libs_if_non_found(filecontent,file,dict):
    for k, v in reversed(dict.items()):
        if not k in filecontent:
            file.write(joinStrings(4)+v.lstrip())
            file.write('\n')

def dedicatedCallToReplaceAppBuildFile(file_path, userdict):
    #Create temp file
    fh, abs_path = mkstemp()
    fcontent = readFileContent(file_abspath= file_path)
    if "com.android.tools.build:gradle" in fcontent:
        _green('file {0} is large build file ,should not go this way'.format(file_path))
        return
    needInsertbuildToolsVersion = BUILD_TOOLS_PATTERN not in fcontent
    needInsertJava17 = "JavaVersion.VERSION_17" not in fcontent and "JavaVersion.VERSION_11" not in fcontent
    needInsertViewBiding = "viewBinding" not in fcontent
    needInsertNdkVersion = ndkVersionIsMissingInDefaultConfig(file_path)
    needInsertToolChainsVersion = "toolchain.languageVersion" not in fcontent
    # _green("needInsertToolChainsVersion for {0} is {1}".format(file_path,needInsertToolChainsVersion))
    with fdopen(fh,'w',encoding='utf-8') as new_file:
        with open(file_path,'r',encoding='utf-8') as old_file:
            keys = userdict.keys()
            for line in old_file:
                white_space_num = line.index(line.lstrip())
                key = next((x for x in keys if x in line), None) ## firstOccurence in list  
                if key:
                    content_to_write = joinStrings(white_space_num)+compat_api_or_implementation(line = line , newline = userdict[key].lstrip(),filename=file_path)
                    new_file.write(content_to_write)
                    new_file.write('\n')
                elif "JavaVersion.VERSION_11" in line:
                    new_file.write(line.replace("VERSION_11","VERSION_17"))
                    if not line.endswith("\n"):
                        new_file.write('\n')
                elif "kotlin-android-extensions" in line:
                    _yellow("remove kotlin-android-extensions in {0} ".format(file_path))
                    pass
                else:
                    new_file.write(line)
                if COMPILESDK_PATTERN in line and (needInsertbuildToolsVersion or needInsertNdkVersion or needInsertViewBiding or needInsertJava17 or needInsertToolChainsVersion) :
                    new_file.write('\n')  
                    if needInsertbuildToolsVersion: ## ndkVersion followed by compileVersion
                        new_file.write(joinStrings(white_space_num)+BUILD_TOOLS_PATTERN_REPLACEMENT.lstrip())  
                        _green("add {0} to android block of file {1} automaticly ".format(BUILD_TOOLS_PATTERN_REPLACEMENT,file_path)) 
                        new_file.write('\n')
                    if needInsertNdkVersion: ## ndkVersion followed by compileVersion
                        new_file.write(joinStrings(white_space_num)+NDK_PATTERN_REPLACEMENT)  
                        _green("add {0} to android block of file {1} automaticly ".format(NDK_PATTERN_REPLACEMENT,file_path)) 
                        new_file.write('\n')
                    if needInsertViewBiding:
                        new_file.write(joinStrings(white_space_num)+ENABLE_VIEWBINDING_HERE_DOCUMENT)
                        _green("add {0} to android block of file {1} automaticly ".format(ENABLE_VIEWBINDING_HERE_DOCUMENT,file_path)) 
                        new_file.write('\n')
                    if needInsertJava17:
                        new_file.write(joinStrings(white_space_num)+COMPILE_OPTION_17_HERE_DOCUMENT)
                        _green("add {0} to android block of file {1} automaticly ".format(COMPILE_OPTION_17_HERE_DOCUMENT,file_path))
                        new_file.write('\n')
                    if needInsertToolChainsVersion:
                        new_file.write(joinStrings(white_space_num)+JAVA_TOOL_CHAIN_17)
                        _green("add {0} to android block of file {1} automaticly ".format(JAVA_TOOL_CHAIN_17,file_path))
                        new_file.write('\n')
                ## add core dependency if non detected
                if "dependencies" in line:
                    add_essential_libs_if_non_found(filecontent = fcontent, file= new_file,dict=
                    {
                        KOTLINX_COROUTINE_PATTERN:KOTLINX_COROUTINE_PATTERN_REPLACEMENT,
                        KOTLINX_COROUTINE_CORE_PATTERN:KOTLINX_COROUTINE_CORE_PATTERN_REPLACEMENT,
                        CARD_VIEW_PATTERN:CARD_VIEW_PATTERN_REPLACEMENT,
                        ANDROID_ACTIVITY_KTX_PATTERN:ANDROID_ACTIVITY_KTX_PATTERNN_REPLACEMENT,
                        ANDROID_KTX_PATTERN:ANDROID_KTX_PATTERN_REPLACEMENT
                    } )
    #Copy the file permissions from the old file to the new file
    copymode(file_path, abs_path)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)

def filter_large_gradle(path):
    _yellow("==start==")
    # replace(LARGE_GRADLE_FILE,REPLACEMENT_DICT_1)
    handle_large_build_gradle_file(file_path=path)
    ## now that jcenter is gone, remove it
    _yellow("==end==")


def filter_gradle_wrapper():
    _yellow("==start==")
    # replace(GRADLE_WRAPPER_FILES,REPLACEMENT_DICT_2)
    handle_gradle_wrapper_file(file_path = GRADLE_WRAPPER_FILES)
    _yellow("==end==")


def filter_app_build_gradle():
    _yellow("==start==")
    dedicatedCallToReplaceAppBuildFile(APP_BUILD_GRADLE_FILE,REPLACEMENT_DICT_3)
    _yellow("==end==")

def handle_one_android_app(dirPath):
    gradlefile = os.path.join(dirPath,"build.gradle")
    gradle_wrapper_file = os.path.join(dirPath,"gradle/wrapper/gradle-wrapper.properties")
    inner_gradle_file = os.path.join(dirPath,"app/build.gradle")
    if(os.path.exists(gradlefile)):
        # print('file  {0}  exists '.format(gradlefile))
        ## 1. this is a module fo android application
        if(text_file_contains_keywords(gradlefile,["com.android.application","dependencies"])):
            dedicatedCallToReplaceAppBuildFile(gradlefile,REPLACEMENT_DICT_3)
        ## 2. this is a  module for android library
        elif(text_file_contains_keywords(gradlefile,["com.android.library","dependencies"])):
            dedicatedCallToReplaceAppBuildFile(gradlefile,REPLACEMENT_DICT_3)
        ## 3. this is an large android build.gradle file
        elif (text_file_contains_keywords(gradlefile,["buildscript","allprojects"])):
            # replace(gradlefile,REPLACEMENT_DICT_1)
            handle_large_build_gradle_file(gradlefile)
    if(os.path.exists(gradle_wrapper_file)):
        # print('file  {0}  exists '.format(gradlefile))
        # replace(gradle_wrapper_file,REPLACEMENT_DICT_2)
        handle_gradle_wrapper_file(gradle_wrapper_file)
    if(os.path.exists(inner_gradle_file)):
        # print('file  {0}  exists '.format(gradlefile))
        dedicatedCallToReplaceAppBuildFile(inner_gradle_file,REPLACEMENT_DICT_3)


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
            if(os.path.exists(gradlefile)):
                fcontent = readFileContent(file_abspath = gradlefile)
                if("compileSdkVersion" in fcontent):
                    _green ('start processing  {0} '.format(os.path.abspath(gradlefile)))
                    dedicatedCallToReplaceAppBuildFile(os.path.abspath(gradlefile),REPLACEMENT_DICT_3)
                    _green ('end processing  {0} '.format(os.path.abspath(gradlefile)))

def thisProjectHasTomlAndShouldAbort():
    if os.path.exists('gradle/libs.versions.toml'):
        _yellow('this project has toml file at \n\n{0} \n\nskip all action'.format(os.path.join(os.getcwd(),'gradle/libs.versions.toml')))
        return True
    elif os.path.exists('buildSrc') and os.path.isdir('buildSrc'):
        _yellow('this project has buildSrc folder at \n\n{0} \n\nskip all action'.format(os.path.join(os.getcwd(),'buildSrc')))
        return True
    else: return False

def main():

    ## 1.0 . abort if this project has toml structure
    if(thisProjectHasTomlAndShouldAbort()):
        return
    ## 1. process large build.gradle file
    if(os.path.exists(LARGE_GRADLE_FILE)):
        _green ('start processing File {0} {1}'.format(LARGE_GRADLE_FILE,"===="))
        filter_large_gradle(LARGE_GRADLE_FILE)
    else:
        _green ('File {0} {1}'.format(LARGE_GRADLE_FILE,"not exists"))

    ## 2. process gradle-warpper.properities file
    if(os.path.exists(GRADLE_WRAPPER_FILES)):
        _green ('start processing File {0} {1}'.format(GRADLE_WRAPPER_FILES,"===="))
        filter_gradle_wrapper()
    else:
        _green ('File {0} {1}'.format(GRADLE_WRAPPER_FILES,"not exists"))

    ### 3. process app/build.gradle file
    if(os.path.exists(APP_BUILD_GRADLE_FILE)):
        _green ('start processing File {0} {1}'.format(APP_BUILD_GRADLE_FILE,"===="))
        filter_app_build_gradle()
    else:
        maybe_module_not_called_app()
        _green ('File {0} {1}'.format(APP_BUILD_GRADLE_FILE,"not exists"))

    ### 4. may be there are more than one build.gradle file, for instance, on build.gradle file per module
    maybe_multiple_module()


if __name__ == "__main__":
    main()



