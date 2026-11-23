""" your_own_exception_type.py """


class MyError(Exception):
    def __init__(self, url: str):
        self.url = url


try:
    raise MyError("https://google.com")
except MyError as e:
    # print(f"yes, got MyError and url is {e.url}")
    print(e)
