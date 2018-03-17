from positivevalue import ValorPositivo
from decimal import Decimal

class ItemVenda:
    valor = ValorPositivo()
    quantidade = ValorPositivo()

    def __init__(self, valor, quantidade):
        self.valor = valor
        self.quantidade = quantidade

    def get_preco_total(self):
        return self.valor * self.quantidade
    


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