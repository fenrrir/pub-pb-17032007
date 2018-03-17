from decimal import Decimal
from metapositivo import Model





class ItemVenda(Model):
    __atributos_positivos__ = ('valor', 'quantidade')

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

    try:
        item = ItemVenda(naodefinido=1)
        assert False
    except TypeError:
        pass
    print(vars(item))
    

if __name__ == "__main__":
    test()