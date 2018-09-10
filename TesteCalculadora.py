
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




teste = TesteCalculadora
teste.test_ePalidromo(7117, 7117)
teste.test_ePalidromo(7127, 7117)
teste.test_ePrimo(7, 7)
teste.test_ePrimo(7, 11)
teste.test_getNumerodeDigitos(5, 12345)
teste.test_getNumerodeDigitos(3, 4123)
teste.test_getBinario(10, 2)
teste.test_getBinario(1011, 25)
teste.test_CalcularMedia(3, 1,2,3,4,5)
teste.test_CalcularMedia(3, 1,1,3,4,5)
teste.test_CalcularSoma(10, 2,3,5)
teste.test_CalcularSoma(10, 1,3,5)






