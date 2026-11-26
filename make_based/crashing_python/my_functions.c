#include <stdio.h>

int square(int i) {
	//return i * i;
	//return i / 0;
	// cppcheck-suppress nullPointer // teaching: the crash inside the extension is what the example shows
	*(char*)0=0;
	return 4;
}
