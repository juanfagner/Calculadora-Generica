
from Calculadora import Calculadora

class TesteCalculadora():

    def __init__(self):
        self.cont = int(0)
        self.sucesso = int(0)

    def test_CalcularSoma(valor, *args):

        teste = Calculadora.CalcularSoma(*args)

        if teste == valor:
            print('\033[32m', 'Teste 1 - Sucesso!' + '\033[0;0m')

        else:
            print('\033[31m', 'Teste 1 - Falhou!' + '\033[0;0m')

        return 0

    def test_CalcularMedia(valor, *args):

        teste = float(Calculadora.CalcularMedia(*args))

        if teste == float(valor):

            print('\033[32m', 'Teste 1 - Sucesso!' + '\033[0;0m')

        else:
            print('\033[31m', 'Teste 1 - Falhou!' + '\033[0;0m')


        return 0

    def test_ePrimo(valor, num):

        teste = float(Calculadora.ePrimo(num))

        if teste == float(valor):
            print('\033[32m', 'Teste 1 - Sucesso!' + '\033[0;0m')

        else:
            print('\033[31m', 'Teste 1 - Falhou!' + '\033[0;0m')

        return 0

    def test_getBinario(valor, num):

        teste = int(Calculadora.getBinario(num))

        if teste == (valor):
            print('\033[32m', 'Teste 1 - Sucesso!' + '\033[0;0m')

        else:
            print('\033[31m', 'Teste 1 - Falhou!' + '\033[0;0m')

        return 0

    def test_ePalidromo(valor, num):

        teste = int(Calculadora.ePalidromo(num))

        if teste == (valor):
            print('\033[32m', 'Teste 1 - Sucesso!' + '\033[0;0m')

        else:
            print('\033[31m', 'Teste 1 - Falhou!' + '\033[0;0m')

        return 0

    def test_getNumerodeDigitos(valor, num):

        teste = (Calculadora.getNumerodeDigitos(num))


        if teste == valor:

            print('\033[32m', 'Teste 1 - Sucesso!' + '\033[0;0m')

        else:
            print('\033[31m', 'Teste 1 - Falhou!' + '\033[0;0m')

        return 0


if  __name__ == "__main__":
    print("Testes")
    teste = TesteCalculadora

    print("Teste de Soma:")
    teste.test_CalcularSoma(185, 8,12,20,60,30,55)
    teste.test_CalcularSoma(228, 10,35,54,27,59,43)
    print("================================")
    print("Teste de Media:")

    teste.test_CalcularMedia(6, 2, 6, 8, 4, 10)
    teste.test_CalcularMedia(30, 10, 20, 30, 40, 50)

    print("================================")
    print("Teste de Binario:")

    teste.test_getBinario(10, 2)
    teste.test_getBinario(1010, 10)

    print("================================")
    print("Teste de Numero de Digitos:")

    teste.test_getNumerodeDigitos(9, 123456789)
    teste.test_getNumerodeDigitos(15, 111112222233333)

    print("================================")
    print("Teste de Numero Primo:")

    teste.test_ePrimo(False, 81)
    teste.test_ePrimo(True, 227)

    print("================================")
    print("Teste de Palidromo:")

    teste.test_ePalidromo(87878787878, 87878787878)
    teste.test_ePalidromo(1234567890987654321, 1234567890987654321)












