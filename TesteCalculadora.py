
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
    teste.test_CalcularSoma(10, 2,3,5)
    teste.test_CalcularSoma(10, 1,3,5)
    print("================================")
    print("Teste de Media:")

    teste.test_CalcularMedia(3, 1, 6, 3, 4, 5)
    teste.test_CalcularMedia(3, 1, 2, 3, 4, 5)

    print("================================")
    print("Teste de Binario:")

    teste.test_getBinario(10, 2)
    teste.test_getBinario(1011, 25)

    print("================================")
    print("Teste de Numero de Digitos:")

    teste.test_getNumerodeDigitos(5, 12345)
    teste.test_getNumerodeDigitos(3, 4123)

    print("================================")
    print("Teste de Numero Primo:")

    teste.test_ePrimo(11, 7)
    teste.test_ePrimo(227, 227)

    print("================================")
    print("Teste de Palidromo:")

    teste.test_ePalidromo(7217, 7137)
    teste.test_ePalidromo(7117, 7117)












