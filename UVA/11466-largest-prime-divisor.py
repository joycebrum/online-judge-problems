from math import sqrt

def get_max_prime(n):
    i = 2
    primes = 0
    res = -1
    while i*i <= n:
        if n % i == 0:
            res = i
            primes += 1
        while n%i == 0:
            n /= i
        i += 1
    if n != 1 and res != -1:
        res = n
    elif primes == 1:
        res = -1
    return int(res)

if __name__ == '__main__':
    while True:
        n = abs(int(input()))
        if n == 0: break
        print(get_max_prime(n))
