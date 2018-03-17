from positivevalue import ValorPositivo

class MetaPositivo(type):

    def __new__(mcls, name, base, namespace):
        atributos = namespace.get('__atributos_positivos__', [])
        for atributo in atributos:
            namespace[atributo] = ValorPositivo(atributo)

        if '__init__' not in namespace:
            def __init__(self, **kwargs):
                for attr, value in kwargs.items():
                    if attr not in atributos:
                        raise TypeError('parâmetro inválido')
                    setattr(self, attr, value)
            namespace['__init__'] = __init__

        return super().__new__(mcls, name, base, namespace)


class Model(metaclass=MetaPositivo):
    pass





