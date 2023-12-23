Readers Writer Lock.
	Write a readers writer lock.
	Write a python object which will be used by thread authors.
	It will have the following methods:
		ReaderEnter
		ReaderLeave
		WriterEnter
		WriterLeave
	A thread author will use it this way:
	If the thread is a reader:
		rwl.ReaderEnter()
		[do some reading of the data]
		rwl.ReaderLeave()
	And the same for the writer...

	* Write some threads to show that your object works.
