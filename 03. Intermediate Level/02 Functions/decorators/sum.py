class Decorator(object):
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        if any([isinstance(i, str) for i in args]):
            return "All arguments must be int"
        return self.func(*args, **kwargs)

@Decorator
def sum(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        return "All arguments must be int"
    return a + b

if __name__ == "__main__":
    print("sum(1, 2) = ", sum(1, 2))
    print("sum(1, 2) = ", sum("1", "2"))