from decimal import Decimal

class ItemVenda:

    def __init__(self, valor, quantidade):      # Por que não definir tudo como privado no Java?
        self.valor = valor
        self.quantidade = quantidade

    def get_preco_total(self):
        return self.valor * self.quantidade


def test():
    item = ItemVenda(valor=Decimal('4.50'), quantidade=2)
    assert item.get_preco_total() == Decimal('9.0')
    item = ItemVenda(valor=Decimal('4.50'), quantidade=-2)
    assert item.get_preco_total() == Decimal('-9.0')
    item = ItemVenda(valor=Decimal('-4.50'), quantidade=2)
    assert item.get_preco_total() == Decimal('-9.0')

if __name__ == "__main__":
    test()