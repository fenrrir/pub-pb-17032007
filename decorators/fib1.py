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
