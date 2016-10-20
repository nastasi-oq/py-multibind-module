ALL: nativelib test run-test

MAJ=1
MIN=1
PAT=0

nativelib.h:
	sed -i "s/^#define NATIVE_VERS .*/#define NATIVE_VERS \"$(MAJ).$(MIN).$(PAT)\"/g" nativelib.h 

nativelib: nativelib.h
	gcc -c -Wall -Werror -fpic native.c
	gcc -shared -Wl,-soname,libnative.so.$(MAJ).$(MIN).$(PAT) -o libnative.so.$(MAJ).$(MIN).$(PAT) -lc native.o
	ln -s libnative.so.$(MAJ).$(MIN).$(PAT) libnative.so.$(MAJ).$(MIN)
	ln -s libnative.so.$(MAJ).$(MIN) libnative.so.$(MAJ)
	ln -s libnative.so.$(MAJ) libnative.so

test: test.c
	gcc -o test -L . test.c -l native

run-test:
	@LD_LIBRARY_PATH=. ./test

clean:
	rm -f native.o *.so.* *.so test

get-soname:
	readelf -a  libnative.so.$(MAJ).$(MIN).$(PAT) | grep soname

help:
	@echo "make"
	@echo "make clean"
	@echo "make run-test"
	@echo "make get-soname"

.PHONY: ALL run-test clean get-soname nativelib.h
