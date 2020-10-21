import sys

def print_fractions(n, f):
    print(len(f))
    i = 0
    while i < len(f):
        print('1/' + str(n), '=', '1/' + str(f[i]['x']), '+', '1/' + str(f[i]['y']))
        i += 1

def get_fractions(k):
    fractions = []

    for y in range(k+1, 2*k +1):
        x = k*y/(y-k)
        if x - int(x) == 0:
            fractions.append({'x': int(x), 'y': y})    
    return fractions

if __name__ == '__main__':
    while True:
        try:
            line = sys.stdin.readline().strip()
            if not line: break
            n = int(line)
            fractions = get_fractions(n)
            print_fractions(n, fractions)
        except EOFError:
            break
