n = int(input())


def primo(n, x):
    if x == 1:
        return True
    elif x == 0:
        return False
    elif n % x == 0:
        return False
    else:
        return primo(n, x - 1)


while True:
    aux = str(n)[::-1]
    if str(n) == aux:
        if primo(n, n - 1):
            print(n)
            break
    n += 1
