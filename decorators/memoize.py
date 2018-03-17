from functools import wraps

def memoize(func): # first-class citizen
    cache = {} # closure
    @wraps(func)
    def new_func(*args, **kwargs): # função aninhada
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return new_func


@memoize
def fib(n):

    if n in (1, 2):
        return 1
    
    return fib(n-1) + fib(n - 2)


def test():
    assert fib(3) == 2
    assert fib(5) == 5
    assert fib(6) == 8
    assert fib(100) == 354224848179261915075

if __name__ == "__main__":
    test()