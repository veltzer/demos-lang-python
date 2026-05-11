.PHONY: all
all: libadd_bad_link.so libadd.so libadd_full.so

libadd_bad_link.so: add_wrap.cc
	gcc -shared -o libadd_bad_link.so add_wrap.cc
#	gcc -shared -Xlinker --no-undefined -o libadd_bad_link.so add_wrap.cc
libadd.so: add.cc
	gcc -shared -o libadd.so add.cc
libadd_full.so: add_wrap.cc libadd.so
	gcc -shared -o libadd_full.so add_wrap.cc -L. -ladd
#	gcc -shared -Xlinker --no-undefined -o libadd_full.so add_wrap.cc -L. -ladd

.PHONY: clean
clean:
	rm -f *.so
