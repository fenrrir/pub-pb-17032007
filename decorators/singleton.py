

def singleton(cls, cache={}):
    def new_constructor(*args, **kwargs):
        if not cls in cache:
            cache[cls]  = cls(*args, **kwargs)
        return cache[cls]
    return new_constructor



@singleton
class Exemplo:
    pass


def test():
    assert Exemplo() == Exemplo()


if __name__ == '__main__':
    test()
