import sys
from math import sqrt
#------------------------ não mandar essa parte

orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f

orig_stdin = sys.stdin
fi = open('in.txt', 'r')
sys.stdin = fi

#------------------------
N = 10000000
P = [False]*10000001
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    P[2] = True
    for i in range(3, n, 2):
        if sieve[i]:
            P[i] = True

def goldbach(n):
    i = 2
    while i < n:
        if P[i] and P[n-i]:
            return i, n-i
        i += 1
    return -1, -1

if __name__ == '__main__':
    primes(N)
    while True:
        try:
            n = input()
            if not n: break
            n = int(n)
            if n < 8:
                print('Impossible.')
                continue
            res = ''
            if n % 2 == 0:
                res += '2 2'
                n -= 4
            else:
                res += '2 3'
                n -= 5
            a, b = goldbach(n)
            print(res, a, b)
        except EOFError:
            break
        
#------------------------ não mandar essa parte

sys.stdout = orig_stdout
f.close()

sys.stdin = orig_stdin
fi.close

#------------------------
