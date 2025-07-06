class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file  # Return the file object, not self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Usage - we get the file object directly
with FileManager('test.txt', 'w') as f:
    f.write("Hello World")  # f is the file object, not FileManager
    f.write("Another line")
