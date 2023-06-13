goal:
    0. WHERE IS kotlinc?
    ## on mac ,it is bundled with android studio plugin
    /Applications/Android\ Studio.app/Contents/plugins/Kotlin/kotlinc


    ## windows:
        IntelliJ IDEA
    打开 [IDEA 安装目录]/plugins/Kotlin/kotlinc 并把这个目录拷到外面某个路径不含空格的地方。

    Android Studio
    打开 [用户目录]/[Android Studio 配置文件]/config/plugins/Kotlin/kotlinc 并把这个目录拷到外面某个路径不含空格的地方。
    ## https://zhuanlan.zhihu.com/p/26942123




tldr:
```shell
cp /Applications/Android\ Studio.app/Contents/plugins/Kotlin/kotlinc .
chmod +x kotlinc/bin/kotlin
chmod +x ......


## 加入环境变量
export PATH=$PATH:`pwd`/kotlinc/bin

type:
kotlinc
to enter REPL

```js
 kotlinc
Welcome to Kotlin version 1.8.20-release (JRE 11.0.17+8)
Type :help for help, :quit for quit
>>> println(Date())
error: unresolved reference: Date
println(Date())
        ^
>>> println(java.util.Date())
Tue Jun 13 11:07:28 CST 2023
>>>
```

https://stackoverflow.com/questions/14733566/how-to-run-kotlin-class-from-the-command-line

even with one click
https://medium.com/@agavatar/programming-with-kotlin-in-visual-studio-code-1d745d6b4ad1
## run kt file
You can compile using kotlinc as follows:

$ kotlinc hello.kt -include-runtime -d hello.jar

and then you can run jar file as follows:

$ java -jar hello.jar


    1. write kotlin file in vscode 
    
    2. kotlin scripting