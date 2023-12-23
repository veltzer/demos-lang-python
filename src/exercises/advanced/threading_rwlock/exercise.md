# Readers Writer Lock

* Write a readers writer lock.

* Write a python object which will be used by thread authors.

* It will have the following methods:
```python
class ReadersWrier Lock:
    def ReaderEnter():
        pass
    def ReaderLeave():
        pass
    def WriterEnter():
        pass
    def WriterLeave():
        pass
```

* A thread author will use it this way:
	If the thread is a reader:
    ```python
		rwl.ReaderEnter()
		[do some reading of the data]
		rwl.ReaderLeave()
    ```
	And the same for the writer...

* Write some threads to show that your object works.
