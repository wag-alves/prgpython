
def fact (num):
    acumulador = 1
    if num > 99:
        return f'Número inválido, informe um valor abaixo de 99! '
    if num > 0:
        while num >= 1:
            print(num)
            acumulador = acumulador * num 
            num -= 1
            if num >= 1:
                print('x')
            else:
                print('=')
        print(acumulador)

    elif num == 0:
        print(f'O fatorial de 0 é 1. ')

    else:
        print(f'Não é definido o fatorial de números negativos. ')

fa = int(input(f'Fale um número: '))
print(fact(fa))