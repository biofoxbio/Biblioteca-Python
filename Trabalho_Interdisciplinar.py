
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL ''')
opcao = int(input('Sua opção: '))


if opcao == 1:
    num = input('Digite um numero Binário: ')

    n = len(num) - 1

    decimal = 0

    for d in num:

        decimal = decimal + int(d) * 2 ** n

        n = n - 1

    print(f'O Binário {num} é igual a {decimal} em decimal')


elif opcao == 2:
    num = input('Digite um numero Octal: ')

    n = len(num) - 1

    decimal = 0

    for d in num:

        decimal = decimal + int(d) * 8 ** n

        n = n - 1

    print(f'O Octal {num} é igual a {decimal} em decimal')


elif opcao == 3:

    num = input('Digite um numero Hexadecimal: ')

    n = len(num) - 1

    decimal = 0

    for d in num:

        if d == 'a':
            d = 10

        if d == 'b':
            d = 11

        if d == 'c':
            d = 12

        if d == 'd':
            d = 13

        if d == 'e':
            d = 14

        if d == 'f':
            d = 15

        decimal = decimal + int(d) * 16 ** n

        n = n - 1

    print(f'O Hexadecimal {num} é igual a {decimal} em decimal')
