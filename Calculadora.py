
class Calculadora:

    def CalcularSoma(*args):

        soma = 0
        for elem in args:
            soma += elem
        return soma

    def CalcularMedia(*args):

        total = Calculadora.CalcularSoma(*args)
        return ("{0:4.1f}".format(total/len(args)))


    def ePrimo(condicao):
        if (condicao % 2) == 0 and condicao > 2:
            return False
        for i in range(3, (condicao - 1)):
            if (condicao % i) == 0:
                return False
            return True

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



