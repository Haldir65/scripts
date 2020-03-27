default:jnisample

java: dirmake
	@echo "modifying a final file using plain java reflect"
	javac com/example/Main.java com/example/SomeClass.java -d target/
	java -cp target com.example.Main

jnisample: dirmake
	sh demo.sh

dirmake:
	mkdir -p jni target lib

.PHONY:
	clean jnisample

clean:
	rm -rf *.class
	rm -rf target/*
	rm -rf lib/*
	rm -rf *.o


