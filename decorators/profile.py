import time
from profile2 import profile


@profile
def espera(segundos):
    time.sleep(segundos)


def test():
    espera(1)
    espera(3)
    for key, value in espera.estatisticas.items():
        print('{}={:.2f}'.format(key, value))


if __name__ == '__main__':
    test()