import time
from functools import wraps

def profile(func):

    func.estatisticas = {}

    @wraps(func)
    def new_func(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        duracao = time.time() - inicio
        print("função: {}. Duração: {} segundos".format(func.__name__, duracao))
        func.estatisticas[args] = duracao
        return resultado
    return new_func