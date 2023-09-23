class MyException(Exception):
    def __init__(self, url: str):
        self.url = url


try:
    raise MyException("https://google.com")
except MyException as e:
    # print(f"yes, got MyException and url is {e.url}")
    print(e)
