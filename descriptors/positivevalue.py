class ValorPositivo:

    def __set_name__(self, owner, nome):
        self.nome = '_' + nome

    def __get__(self, obj, objtype):
        if obj is None:
            return self
        return getattr(obj, self.nome)

    def __set__(self, obj, valor):
        if valor < 0:
            raise ValueError('O valor deve maior que zero')
        setattr(obj, self.nome, valor)


