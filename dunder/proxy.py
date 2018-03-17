# coding: utf-8

class Exemplo:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def metodo(self):
        return self.a, self.b


class Proxy: # Padrão de projeto

    def __init__(self, obj):
        self.obj = obj

    def __getattr__(self, atributo):
        print('capturando acesso a atributo: {}'.format(atributo))
        return getattr(self.obj, atributo)


def test():
    exm = Exemplo(1, 2)
    proxy_exm = Proxy(exm)
    assert proxy_exm.a == 1
    assert proxy_exm.b == 2
    assert proxy_exm.metodo() == (1,2)

if __name__ == '__main__':
    test()