""" Dr. Lothar"""


def lothar(n):
    count = 0
    while n != 1:
        aux = int(n % 2)
        if aux == 0:
            n = (n / 2)
        else:
            n = (n * 3 + 1)
        count = count + 1
    return count


if __name__ == '__main__':
    n = int(input())
    print(lothar(n))
