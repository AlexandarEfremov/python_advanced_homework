class store_results:
    _NAME_ = "results.txt"

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        with open(self._NAME_, "a") as log_file:
            log_file.write(f"Function {self.func.__name__} was called. Result: {self.func(*args, **kwargs)}")


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b

add(2, 2)

mult(6, 4)