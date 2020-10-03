def primes_fact(p, n, f):
    if p > n: return 0
    if p == n: return 1
    multiples = int(n/p) + primes_fact(p*f, n, f)
    return multiples
    

def divides_fac(m, n):
    i = 2
    k = 0
    while i*i <= m:
        k = 1
        primes = 0
        if m % i == 0:
            primes = primes_fact(i, n, i)
        while m % i == 0:
            if k > primes: return False
            m /= i
            k += 1
        i += 1
    if int(m) != 1:
        if m <= n: return True
        else: return False
    else: return True

if __name__ == '__main__':
    while True:
        try:
            line = input().strip().split()
            if not line: break
            n, m = int(line[0]), int(line[1])
            if divides_fac(m, n): print(m, 'divides', str(n) + '!')
            else: print(m, 'does not divide', str(n) + '!')
                
        except EOFError:
            break
