class selfclsmethod(object):            # um novo tipo de método pro python
                                        # o método irá receber automaticamente a instância e a classe atual
    def __init__(self, method):
        self.method = method

    def __get__(self, obj, type):
        def new_method( *args, **kwargs ):
            return self.method( obj, type, *args, **kwargs)
        return new_method



class Exemplo:

    @selfclsmethod
    def test(self, cls):
        return self, cls

    @classmethod
    def test_class(cls):
        return cls


def test():
    exm = Exemplo()
    assert exm.test_class() == Exemplo
    assert exm.test() == (exm, Exemplo)


if __name__ == '__main__':
    test()