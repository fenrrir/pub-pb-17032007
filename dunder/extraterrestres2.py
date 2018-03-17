

class Extraterrestre:
    contador = 0

    def __init__(self):
        self.__class__.contador += 1

    def __init_subclass__(cls, *args, **kwargs):
        super().__init_subclass__(*args, **kwargs)
        cls.contador = 0


e1 = Extraterrestre()
e2 = Extraterrestre()

assert Extraterrestre.contador == 2

class Marciano(Extraterrestre):
    pass


m1 = Marciano()
print(Extraterrestre.contador)
print(Marciano.contador)
assert Extraterrestre.contador == 3
