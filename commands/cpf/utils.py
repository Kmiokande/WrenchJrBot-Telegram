import random


def new_random():
    return random.randrange(10)


def new_cpf():
    n1 = new_random()
    n2 = new_random()
    n3 = new_random()
    n4 = new_random()
    n5 = new_random()
    n6 = new_random()
    n7 = new_random()
    n8 = new_random()
    n9 = new_random()

    # Contas e mais contas, dividi pra fica mais bonitinho
    a1 = n9 * 2
    a2 = n8 * 3
    a3 = n7 * 4
    a4 = n6 * 5
    a5 = n5 * 6
    a6 = n4 * 7
    a7 = n3 * 8
    a8 = n2 * 9
    a9 = n1 * 10

    # Soma os resultados de todas as contas anteriores e faz
    # outra continha.. tudo regra do cpf, para ele ser valido :P
    d1 = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9
    d1 = 11 - (d1 % 11)

    if d1 >= 10:
        d1 = 0

    # Mesma coisa da de cima so que agora pra variavel d2
    a1 = d1 * 2
    a2 = n9 * 3
    a3 = n8 * 4
    a4 = n7 * 5
    a5 = n6 * 6
    a6 = n5 * 7
    a7 = n4 * 8
    a8 = n3 * 9
    a9 = n2 * 10
    a10 = n1 * 11

    # ... rola a barra de rolagem pra cima que tu vai entender :P
    d2 = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10
    d2 = 11 - (d2 % 11)

    if d2 >= 10:
        d2 = 0

    return f"{n1}{n2}{n3}.{n4}{n5}{n6}.{n7}{n8}{n9}-{d1}{d2}"
