### open this project in intelij idea

## 1. gradle文件的import 不像其他语言那么轻松
```agsl
lol.gradle

project.ext.lolFunction = {
   println it
}
build.gradle

apply from: 'lol.gradle'

ext.lolFunction(1)    
// 或者不加ext直接调用
lolFunction(1)                                                             
                                                         
```


https://docs.gradle.org/current/userguide/writing_build_scripts.html
https://docs.gradle.org/current/userguide/kotlin_dsl.html
https://www.tutorialspoint.com/groovy/groovy_optionals.htm