from reflexao import Cliente

def test():
    c = Cliente(nome="Barry Allen", endereco="Central City")
    print(c)
    def to_string(self):
        return "<Nome='{}'. Endereco='{}'>".format(self.nome, self.endereco)
    Cliente.__str__ = to_string
    print(c)


if __name__ == "__main__":
    test()