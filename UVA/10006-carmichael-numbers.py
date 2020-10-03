import sys
#------------------------ não mandar essa parte

orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f

orig_stdin = sys.stdin
fi = open('in.txt', 'r')
sys.stdin = fi

#------------------------
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

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a % b)

def power(x, y, mod):
    if y == 0: return 1
    temp = power(x, int(y/2), mod) % mod
    temp = (temp * temp) % mod
    if (y % 2 == 1):
        temp = (temp * x) % mod
    return temp

def is_carmichael(n):
    if P[n]: return False
    for a in range(2, n):
        if power(a, n, n) != a:
            return False
    return not P[n]
if __name__ == '__main__':
    primes(65001)
    while True:
        n = int(input().strip())
        if n == 0: break
        if is_carmichael(n):
            print('The number', n, 'is a Carmichael number.')
        else:
            print(n, 'is normal.')
        
#------------------------ não mandar essa parte

sys.stdout = orig_stdout
f.close()

sys.stdin = orig_stdin
fi.close
#------------------------
