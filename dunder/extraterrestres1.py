

class Extraterrestre:
    contador = 0

    def __init__(self):
        self.__class__.contador += 1


e1 = Extraterrestre()
e2 = Extraterrestre()

assert Extraterrestre.contador == 2

class Marciano(Extraterrestre):
    pass


m1 = Marciano()
assert Extraterrestre.contador == 2
assert Marciano.contador == 1, Marciano.contador
