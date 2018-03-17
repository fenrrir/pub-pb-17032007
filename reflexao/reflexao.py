# coding: utf-8

class Cliente:
    """ Representa um cliente """

    def __init__(self, nome, endereco):
        """ Nome e endereço requeridos """
        self.nome = nome
        self.endereco = endereco

    def get_dados_bancarios(self):
        """ Retorna os dados bancários do cliente """
        raise NotImplemented()



def test():
    cliente = Cliente(nome="Walter White", endereco="Albuquerque")
    print("Possui atributo? {}".format(hasattr(cliente, "nome")))
    setattr(cliente, "nome", "Pinkman")
    print("Nome: {}".format(getattr(cliente, "nome")))
    print("\n## Dados do objeto ##")

    for attr in vars(cliente):
        valor_atributo = getattr(cliente, attr)
        print("\t{} = {}".format(attr, repr(valor_atributo)))



if __name__ == "__main__":
    test()