def get_coefficient(i, k):
    c = 1
    for j in range(1, i+1):
        c *= (k + 1 - j)/j
    c = round(c)
    if c == 1: return ''
    return str(c)

def get_binomial(a, b, k):
    res = ''
    for i in range(0, k+1):
        if i > 0: res += '+'
        c = get_coefficient(i, k)
        if c:
            res += c + '*'
        
        if k - i > 0:
            if k - i == 1: res += a
            else: res += a + '^' + str(k-i)
        if k - i > 0 and i > 0:
            res += '*'
        if i > 0:
            if i == 1: res += b
            else: res += b + '^' + str(i)
    return res

if __name__ == '__main__':
    tests = int(input().strip())
    for i in range(0, tests):
        binomial = input().strip()
        k = int(binomial[binomial.find('^') + 1:])
        a = binomial[1:binomial.find('+')]
        b = binomial[binomial.find('+') + 1 : binomial.find(')')]
        print('Case', str(i+1) + ':', get_binomial(a,b,k))
