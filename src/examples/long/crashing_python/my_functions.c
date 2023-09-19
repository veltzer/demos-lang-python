#include <stdio.h>

int square(int i) {
	//return i * i;
	//return i / 0;
	*(char*)0=0;
	return 4;
}
