
class Calculadora:

    def CalcularSoma(*args):

        soma = 0
        for elem in args:
            soma += elem
        return soma

    def CalcularMedia(*args):

        total = Calculadora.CalcularSoma(*args)
        return ("{0:4.1f}".format(total/len(args)))


    def ePrimo(num):
        if (num % 2) == 0 and num > 2:
            return False
        for i in range(3, (num - 1)):
            if (num % i) == 0:
                return False
            return num

    def getBinario(num):
        return ("{0:b}".format(num))

    def ePalidromo(num):
        x = str([num])
        x2 = x[::-1]
        novonum = int(x2[1:len(x2)-1])
        if novonum == num:
            return novonum
        else:
            return False

    def getNumerodeDigitos(num):
        return len(str(num))



