#include <Python.h>
#include <stdio.h> // for printf(3)

int main(int argc,char** argv,char** envp) {
	printf("Hello from C!\n");
	Py_Initialize();
	PyRun_SimpleString(
		"print('Hello, World from python!')\n"
		"import time\n"
		"time.sleep(6)\n"
		"print('python woke up!')\n"
	);
	Py_Finalize();
	return 0;
}
