def primo(num):
    if num == 1:
        return False
    if num in (2, 3):
        return True
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

def main():
    try:
        valor = int(input(f'Digite um número inteiro: '))
        for i in range(1, valor+1):
            if primo(i):
                print(f'{i} é primo! ')
    except ValueError:
        print(f'Você deve digitar um número inteiro! ')

if __name__ == '__main__':
    main()