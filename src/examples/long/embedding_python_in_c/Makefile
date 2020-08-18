.PHONY: all
all: embed.elf

CONFIG:=python3-config
PYTHON_CFLAGS:=$(shell $(CONFIG) --cflags) -fPIE
PYTHON_LIBS:=$(shell $(CONFIG) --libs)

embed.elf: embed.c
	gcc -o $@ $< $(PYTHON_CFLAGS) $(PYTHON_LIBS) -lpython3.8

.PHONY: clean
clean:
	-rm -f embed.elf

.PHONY: debug
debug:
	$(info PYTHON_CFLAGS is $(PYTHON_CFLAGS))
	$(info PYTHON_LIBS is $(PYTHON_LIBS))
