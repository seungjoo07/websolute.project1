
def recursive(n):
    if n == 1:
        return 0

    print('현재 n=', n)
    return n * factorial(n - 1);



def factorial(n):
    if n == 1:
        return 1
    else :
        return n * factorial(n - 1);


def sub(n):
    print('호출')
    if n <= 1:
        return n

    ''' '''
    return sub(n-1) + sub(n-2)


def asterisk(i):
    if i > 1:
        asterisk(i/2)
        asterisk(i/2)
    print("*", end='')

if __name__ == '__main__':
    print(sub(3))