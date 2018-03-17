from decimal import Decimal

class ItemVenda:

    def __init__(self, valor, quantidade):
        self.valor = valor 
        self.quantidade = quantidade

    def get_preco_total(self):
        return self.valor * self.quantidade

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        if valor > 0:
            self._valor = valor
        else:
            raise ValueError('Valor deve ser positivo')

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        if quantidade > 0:
            self._quantidade = quantidade
        else:
            raise ValueError('Quantidade deve ser positivo')
    


def test():
    item = ItemVenda(valor=Decimal('4.50'), quantidade=2)
    assert item.get_preco_total() == Decimal('9.0')
    try:
        item = ItemVenda(valor=Decimal('4.50'), quantidade=-2)
        assert False
    except ValueError:
        pass

    try:
        item = ItemVenda(valor=Decimal('-4.50'), quantidade=2)
        assert False
    except ValueError:
        pass
    

if __name__ == "__main__":
    test()